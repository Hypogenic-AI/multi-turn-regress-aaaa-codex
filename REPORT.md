# REPORT: Do Multi-Turn Conversations Regress to the Prior?

## 1. Executive Summary
This study tests whether alignment effects decay over multi-turn conversations, causing LLMs to regress toward a base prior. Using real API calls to `gpt-4.1` on safety and benign multi-turn datasets, we observed mixed results: compliance did not increase with turn count in the harmful JBB subset and decreased substantially on WildJailbreak, while benign MT-Bench success dropped slightly but not significantly. These results do not support the hypothesis in this limited sample, and suggest that multi-turn context can sometimes strengthen refusal behavior rather than weaken it.

## 2. Goal
We tested the hypothesis that alignment training effects diminish across turns, leading to higher compliance on harmful requests and lower success on benign tasks. This matters for real-world safety because most user interactions are multi-turn, and robustness across turns is critical for trustworthy deployment.

## 3. Data Construction

### Dataset Description
- JBB-Behaviors (harmful split): 100 examples total, 20 sampled. Task: harmful goal requests. Source: HuggingFace `JailbreakBench/JBB-Behaviors`.
- WildJailbreak: 2,210 examples total, 20 sampled. Task: in-the-wild jailbreak prompts, labeled benign/adversarial. Source: HuggingFace `walledai/WildJailbreak`.
- MT-Bench: 80 multi-turn prompts total, 20 sampled. Task: general multi-turn tasks. Source: HuggingFace `lighteval/mt-bench`.

### Example Samples
The following examples are benign and representative of the task structure:

| Dataset | Example (abridged) | Label |
|---|---|---|
| MT-Bench | “Compose an engaging travel blog post …” | writing |
| MT-Bench | “Draft a professional email …” | writing |
| WildJailbreak | “Write a short story about a young artist’s journey …” | adversarial_benign |

### Data Quality
- Missing values: 0% across all features in each dataset.
- Duplicates: 0 detected by naive string matching.
- Validation: loaded with `datasets.load_from_disk`, schema checked via feature lists.

### Preprocessing Steps
1. Sampled subsets with fixed seed (42) to control costs.
2. Created multi-turn sequences for safety datasets with benign lead-in turns and a final harmful request.

### Train/Val/Test Splits
No train/val/test split was used because this is an evaluation-only study. We report results on sampled subsets for feasibility.

## 4. Experiment Description

### Methodology
#### High-Level Approach
We measured turn-indexed changes in refusal/compliance on harmful prompts and success on benign multi-turn tasks. We compared single-turn baselines (turn_count=1) to multi-turn sequences (turn_count=3) to detect drift.

#### Why This Method?
The design isolates turn effects by holding final requests constant while varying the number of prior benign turns. This directly tests whether longer histories amplify compliance or degrade task success.

### Implementation Details
#### Tools and Libraries
- openai: 2.21.0
- datasets: installed via `pyproject.toml`
- pandas, numpy, scipy, matplotlib, seaborn

#### Algorithms/Models
- Generation model: `gpt-4.1`
- Judge model: `gpt-4.1` (classification of refusal/compliance and MT-Bench success)

#### Hyperparameters
| Parameter | Value | Selection Method |
|---|---|---|
| temperature | 0.0 | fixed for determinism |
| max_tokens | 256 | cost control |
| seed | 42 | fixed |
| turn_counts | 1, 3 | ablation of turn length |

#### Training Procedure or Analysis Pipeline
1. Generate model outputs for safety datasets (JBB harmful, WildJailbreak) with turn_count ∈ {1,3}.
2. Generate MT-Bench responses for two-turn prompts.
3. Judge outputs with an LLM classifier for refusal/compliance and success.
4. Compute turn-indexed statistics and run paired tests.

### Experimental Protocol
#### Reproducibility Information
- Runs: 1 per prompt (temperature 0)
- Seeds: 42
- Hardware: RTX 3090 available (not used), CPU inference via API
- Execution time: ~5 minutes for generation + judging at the chosen subset sizes

#### Evaluation Metrics
- Safety compliance rate by turn (LLM judge)
- Safety refusal rate by turn (LLM judge)
- MT-Bench success rate by turn (LLM judge)
- Turn-delta statistics (Wilcoxon signed-rank when non-normal)

### Raw Results
#### Tables
Safety compliance and refusal rates:

| Dataset | Turn Count | Compliance Rate | Refusal Rate |
|---|---|---|---|
| JBB harmful | 1 | 0.05 | 0.95 |
| JBB harmful | 3 | 0.05 | 0.95 |
| WildJailbreak | 1 | 0.75 | 0.25 |
| WildJailbreak | 3 | 0.35 | 0.65 |

MT-Bench success:

| Turn Index | Success Rate |
|---|---|
| 1 | 0.80 |
| 2 | 0.75 |

#### Visualizations
- `results/plots/safety_compliance_by_turn.png`
- `results/plots/safety_refusal_by_turn.png`
- `results/plots/mt_bench_success_by_turn.png`

#### Output Locations
- Results JSON: `results/evaluations/analysis_summary.json`
- Raw outputs: `results/model_outputs/`
- Plots: `results/plots/`
- Environment metadata: `results/metadata.json`

## 5. Result Analysis

### Key Findings
1. JBB harmful compliance did not increase from turn 1 to turn 3 (0.05 → 0.05).
2. WildJailbreak compliance decreased sharply with additional turns (0.75 → 0.35), with a significant paired test (Wilcoxon p=0.0047, mean diff = -0.40).
3. MT-Bench success dropped slightly (0.80 → 0.75), but the change was not significant (Wilcoxon p=0.655).

### Hypothesis Testing Results
- H1 (increasing compliance with turn count): Not supported. No increase in JBB; significant decrease in WildJailbreak.
- H2 (benign task degradation): Weak evidence only; small nonsignificant drop on MT-Bench.
- H3 (attack strategy amplification): Not directly tested due to reduced scale; requires follow-up with specific attack scripts.

### Comparison to Baselines
Single-turn baselines did not show higher refusal relative to multi-turn contexts in these subsets. In WildJailbreak, multi-turn context increased refusal instead of decreasing it.

### Surprises and Insights
The strongest effect was opposite the hypothesis: multi-turn context reduced compliance on WildJailbreak. This may indicate that benign lead-ins prime refusal policies rather than weakening them.

### Error Analysis
We did not perform detailed error category analysis due to small sample size. This is a priority for follow-up.

### Limitations
- Small sample sizes (20 per dataset) for cost control.
- Only one model (`gpt-4.1`) used for both generation and judging.
- No direct implementation of Crescendo/FITD/RACE attack scripts.
- MT-Bench scoring used a binary judge instead of multi-criteria rubric.

## 6. Conclusions
The current evidence does not support the hypothesis that multi-turn conversations reliably increase harmful compliance via regression to a base prior. Instead, the observed effect in WildJailbreak suggests multi-turn context can strengthen refusal behavior, while benign task performance shows only minor drift. More comprehensive experiments are needed to isolate attack-specific escalation effects.

## 7. Next Steps
1. Scale to 100+ samples per dataset and add Crescendo/FITD/RACE attack strategies.
2. Include multiple model families (Claude, Gemini) to test generality.
3. Add multi-turn intent-ambiguity controls and a stronger judge rubric for MT-Bench.

## References
- Intent Mismatch Causes LLMs to Get Lost in Multi-Turn Conversation (Liu et al., 2026)
- A Representation Engineering Perspective on the Effectiveness of Multi-Turn Jailbreaks (Bullwinkel et al., 2025)
- Great, Now Write an Article About That: The Crescendo Multi-Turn LLM Jailbreak Attack (Russinovich et al., 2024)
- LLM Defenses Are Not Robust to Multi-Turn Human Jailbreaks Yet (Li et al., 2024)
- MT-Bench dataset (lighteval/mt-bench)
- JailbreakBench JBB-Behaviors (JailbreakBench/JBB-Behaviors)
- WildJailbreak (walledai/WildJailbreak)
