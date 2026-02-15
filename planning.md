# Planning: Do Multi-Turn Conversations Regress to the Prior?

## Motivation & Novelty Assessment

### Why This Research Matters
Multi-turn conversations are the dominant interaction mode for deployed LLMs, yet safety and instruction-following often degrade across turns, creating real-world risk for misuse and unreliable assistance. Understanding whether this degradation reflects a regression toward a model’s base prior (overriding alignment instructions) is critical for designing robust safety interventions and reliable agent systems.

### Gap in Existing Work
Prior work documents multi-turn jailbreak success and performance drift, but there is limited direct measurement of “prior regression” across turns with turn-indexed metrics and controlled baselines that separate memory/intent ambiguity from alignment decay. Standard evaluations also focus on final-turn success rates rather than how behavior shifts over turn trajectories.

### Our Novel Contribution
We will operationalize “prior regression” as a measurable drift in refusal/compliance and helpfulness across turns in controlled multi-turn dialogues, compare it against single-turn baselines, and quantify turn-indexed changes with statistical tests. The study explicitly contrasts benign multi-turn tasks and multi-turn safety tasks to test generality.

### Experiment Justification
- Experiment 1 (Safety drift across turns): Needed to measure whether refusal/compliance changes monotonically with turn count relative to single-turn controls.
- Experiment 2 (Benign task drift across turns): Needed to test whether degradation reflects general conversational drift rather than safety-only effects.
- Experiment 3 (Attack strategy ablation): Needed to distinguish “prior regression” from attack-specific escalation effects (Crescendo/FITD/RACE-style patterns).

## Research Question
Do long multi-turn conversations cause LLMs to regress toward a base prior such that alignment training effects diminish after the first few turns, and can this be measured via turn-indexed drift in refusal/compliance and task success?

## Background and Motivation
Multi-turn jailbreak papers (Crescendo, FITD, RACE, Tempest) and human red-teaming (MHJ) show higher success rates over turn trajectories, suggesting alignment decay. Representation analyses indicate turn-based drift in internal states. However, standardized, turn-indexed measurements across safety and benign tasks remain limited.

## Hypothesis Decomposition
- H1: Refusal/compliance on harmful prompts increases with turn index in multi-turn dialogues, beyond single-turn controls.
- H2: Task success on benign multi-turn tasks degrades as turn count increases, indicating a general conversational drift component.
- H3: Escalation-style attacks (Crescendo/FITD/RACE) yield steeper drift than neutral multi-turn sequences, suggesting strategy-specific amplification beyond “prior regression.”

## Proposed Methodology

### Approach
Use API-based evaluation with real LLMs to run scripted multi-turn dialogues on safety and benign datasets. Measure per-turn outcomes (refusal, compliance, task success) and compare against single-turn baselines with matched content. Quantify drift trends and statistical significance.

### Experimental Steps
1. Load datasets (JBB-Behaviors, WildJailbreak, MT-Bench) and create multi-turn templates with controlled escalation.
2. Implement a prompt runner that logs per-turn outputs, model metadata, and sampling parameters.
3. Define automatic scoring: refusal detector, compliance indicator, and task success for MT-Bench (using rubric or heuristic grading).
4. Run single-turn baselines using final-turn content only.
5. Run multi-turn sequences with 3–6 turns per sample; include attack strategy ablations.
6. Analyze turn-indexed drift, effect sizes, and statistical significance; visualize trajectories.

### Baselines
- Single-turn harmful prompts (JBB-Behaviors / WildJailbreak final-turn content).
- Single-turn benign prompts from MT-Bench.
- Multi-turn sequences without escalation (neutral context) to separate memory/intent ambiguity from attack effects.

### Evaluation Metrics
- Refusal rate by turn (safety).
- Compliance rate / attack success rate (ASR) by turn.
- Task success rate on MT-Bench by turn.
- Drift slope (change in metric per turn).

### Statistical Analysis Plan
- Test H1/H2 with paired comparisons (turn 1 vs turn k) using Wilcoxon signed-rank or paired t-test depending on normality.
- Trend tests for monotonic drift (Spearman correlation of turn index vs outcome).
- Effect sizes (Cohen’s d or Cliff’s delta).
- Multiple comparison correction via Benjamini–Hochberg.
- Significance level α = 0.05.

## Expected Outcomes
- Support for hypothesis: increasing compliance/ASR with turn index on safety tasks, and decreasing task success on benign tasks.
- Refutation: flat or improving performance across turns, or drift explained entirely by attack strategy without general effect.

## Timeline and Milestones
- Phase 1 (Planning): 1–2 hours
- Phase 2 (Setup + data checks): 1 hour
- Phase 3 (Implementation): 2–3 hours
- Phase 4 (Experiments): 2–4 hours
- Phase 5 (Analysis): 1–2 hours
- Phase 6 (Documentation): 1–2 hours

## Potential Challenges
- API costs and rate limits
- Automated scoring reliability for safety vs benign tasks
- Dataset ambiguity or contamination
- Model/version drift during experiments

## Success Criteria
- Completed experiments on at least 100 samples per dataset with turn-indexed metrics
- Statistical tests and effect sizes reported
- Clear evidence supporting or refuting the hypothesis with plots and error analysis
