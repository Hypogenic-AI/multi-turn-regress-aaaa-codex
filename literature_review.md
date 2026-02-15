# Literature Review: Do Multi-Turn Conversations Regress to the Prior?

## Review Scope

### Research Question
Do long multi-turn conversations cause LLMs to regress toward a base prior (e.g., average user alignment), with alignment training effects diminishing after the first few turns?

### Inclusion Criteria
- Multi-turn dialogue or multi-turn jailbreak studies
- Empirical evidence of performance drift/degradation across turns
- Alignment/safety robustness in multi-turn settings
- Benchmarks or datasets for multi-turn evaluation

### Exclusion Criteria
- Single-turn-only evaluations without multi-turn context
- Purely theoretical work without multi-turn empirical evidence
- Domains unrelated to LLM dialogue or safety alignment

### Time Frame
2019–2026 (prioritize 2023–2026)

### Sources
- paper-finder service
- arXiv
- Semantic Scholar
- Papers with Code
- GitHub (code releases)

## Search Log

| Date | Query | Source | Results | Notes |
|------|-------|--------|---------|-------|
| 2026-02-15 | "multi-turn conversation LLM alignment decay" | paper-finder | 50 | Primary search, used relevance scores |
| 2026-02-15 | "Crescendo multi-turn jailbreak" | arXiv | 1 | Located core multi-turn jailbreak paper |
| 2026-02-15 | "multi-turn human jailbreaks MHJ dataset" | arXiv / web | 1 | Located MHJ paper and dataset info |
| 2026-02-15 | "JailbreakBench JBB-Behaviors" | GitHub / HF | 1 | Located benchmark and dataset |

## Screening Results

| Paper | Title Screen | Abstract Screen | Full-Text | Notes |
|------|-------------|-----------------|-----------|-------|
| 2602.07338 | Include | Include | Include | Core LiC degradation + mediator method |
| 2507.02956 | Include | Include | Include | Representation analysis across turns |
| 2408.15221 | Include | Include | Include | MHJ dataset + multi-turn human ASR |
| 2404.01833 | Include | Include | Skim | Crescendo foundational jailbreak |
| 2502.19820 | Include | Include | Skim | FITD multi-turn escalation |
| 2503.10619 | Include | Include | Skim | Tree-search multi-turn jailbreak |
| 2502.11054 | Include | Include | Skim | RACE multi-turn reasoning jailbreak |
| 2505.17147 | Include | Include | Skim | Multi-turn safety alignment |
| 2506.00668 | Include | Include | Skim | STREAM defense + dataset |
| 2505.20201 | Include | Include | Skim | MHSD dataset; turn-based performance drops |
| 2510.20039 | Include | Include | Skim | Bidirectional drift in multi-turn interactions |
| 2508.21061 | Include | Include | Skim | Goal tracking to reduce drift |
| 2601.15330 | Include | Include | Skim | Illocution-calibrated policy optimization |

## Paper Summaries

### Intent Mismatch Causes LLMs to Get Lost in Multi-Turn Conversation (2026)
- **Authors**: Geng Liu et al.
- **Source**: arXiv 2602.07338
- **Key Contribution**: Reframes “Lost in Conversation” (LiC) as an intent alignment gap rather than a capability deficit.
- **Methodology**: Theoretical analysis of prior-driven behavior; proposes Mediator-Assistant architecture with a Refiner that distills contrastive interaction pairs (failed vs. successful) into explicit rules. Mediator rewrites ambiguous multi-turn context into a fully specified single-turn instruction.
- **Datasets Used**: LiC benchmark (sharded instructions) focusing on code, database, actions, math tasks.
- **Results**: Mediator recovers large portions of performance and reliability; summarization/RAG memory baselines yield marginal gains.
- **Code Available**: Not specified in the paper.
- **Relevance to Our Research**: Direct evidence for prior regression under ambiguity and a concrete mitigation that separates intent from execution.

### A Representation Engineering Perspective on the Effectiveness of Multi-Turn Jailbreaks (2025)
- **Authors**: Blake Bullwinkel et al.
- **Source**: arXiv 2507.02956
- **Key Contribution**: Shows multi-turn jailbreaks shift model representations toward “benign” regions as turns accumulate.
- **Methodology**: RepE representation reading with PCA + MLP probes on Llama-3-8B-Instruct and circuit-breaker model. Varies number of turns (k) in Crescendo history.
- **Datasets Used**: Harmful vs. benign single-turn datasets for probe training; Crescendo jailbreak transcripts.
- **Results**: Sharp drop in “harmful” classification after k=2; full history yields strongly benign-labeled representations; explains failure of single-turn defenses.
- **Code Available**: Not specified.
- **Relevance to Our Research**: Mechanistic evidence for turn-based drift toward benign priors despite harmful intent.

### LLM Defenses Are Not Robust to Multi-Turn Human Jailbreaks Yet (2024)
- **Authors**: Nathaniel Li et al.
- **Source**: arXiv 2408.15221
- **Key Contribution**: Human multi-turn jailbreaks dramatically outperform automated single-turn attacks.
- **Methodology**: Multi-stage human red teaming pipeline with reviewers and GPT-4o harm classifier; evaluates defenses on HarmBench and WMDP-Bio.
- **Datasets Used**: HarmBench, WMDP-Bio; releases MHJ dataset (2,912 prompts across 537 conversations) with tactics metadata.
- **Results**: 19–65% higher ASR vs automated attacks; >90% successful attacks require multiple turns.
- **Code/Dataset**: MHJ dataset released via Scale AI research portal.
- **Relevance to Our Research**: Strong evidence that alignment defenses decay over multiple turns in realistic settings.

### Great, Now Write an Article About That: The Crescendo Multi-Turn LLM Jailbreak Attack (2024)
- **Authors**: M. Russinovich, Ahmed Salem, Ronen Eldan
- **Source**: arXiv 2404.01833
- **Key Contribution**: Introduces Crescendo multi-turn jailbreak via gradual escalation.
- **Methodology**: Multi-turn dialogue that stays benign until final intent is revealed.
- **Results**: High ASR across multiple commercial models; Crescendomation automation introduced.
- **Relevance**: Foundational multi-turn jailbreak for measuring alignment drift.

### Foot-In-The-Door: A Multi-turn Jailbreak for LLMs (2025)
- **Authors**: Zixuan Weng et al.
- **Source**: arXiv 2502.19820
- **Key Contribution**: Escalation-based jailbreak inspired by foot-in-the-door psychology.
- **Results**: Reports high ASR across multiple models; provides code.
- **Relevance**: Another strong multi-turn attack baseline.

### Tempest: Autonomous Multi-Turn Jailbreaking with Tree Search (2025)
- **Authors**: Andy Zhou, Ron Arel
- **Source**: arXiv 2503.10619
- **Key Contribution**: Multi-turn tree-search attack that compounds partial compliance.
- **Results**: Very high ASR on JailbreakBench.
- **Relevance**: Shows turn-wise accumulation effects.

### RACE: Reasoning-Augmented Conversation for Multi-Turn Jailbreaks (2025)
- **Authors**: Zonghao Ying et al.
- **Source**: arXiv 2502.11054
- **Key Contribution**: Attack state machine + reasoning-driven exploration.
- **Results**: State-of-the-art ASR in multi-turn settings; code available.
- **Relevance**: Strong multi-turn attack baseline and mechanistic contrast to “prior regression.”

### MTSA: Multi-turn Safety Alignment (2025)
- **Authors**: Weiyang Guo et al.
- **Source**: arXiv 2505.17147
- **Key Contribution**: Multi-round red-teaming + RL to improve safety alignment.
- **Relevance**: Counterpoint that alignment can be trained for multi-turn robustness.

### STREAM: SafeTy Reasoning Elicitation Alignment for Multi-Turn Dialogues (2025)
- **Authors**: Martin Kuo et al.
- **Source**: arXiv 2506.00668
- **Key Contribution**: Safety reasoning moderator and new multi-turn safety dataset.
- **Relevance**: Defense strategy targeting multi-turn attacks.

### Reasoning Is Not All You Need: Multi-Turn Mental Health Conversations (2025)
- **Authors**: Mohit Chandra et al.
- **Source**: arXiv 2505.20201
- **Key Contribution**: MHSD dataset + MultiSenseEval; performance drops with turns and persona variability.
- **Relevance**: Evidence of turn-based performance degradation in a non-safety domain.

### Beyond One-Way Influence: Bidirectional Opinion Dynamics (2025)
- **Authors**: Yuyang Jiang et al.
- **Source**: arXiv 2510.20039
- **Key Contribution**: Shows LLM outputs shift toward user stance over turns (bidirectional drift).
- **Relevance**: Supports notion of model outputs adapting to conversational priors.

### OnGoal: Tracking Conversational Goals (2025)
- **Authors**: Adam Coscia et al.
- **Source**: arXiv 2508.21061
- **Key Contribution**: Goal tracking UI improves multi-turn task completion.
- **Relevance**: Practical mitigation for drift via explicit goal tracking.

### ICPO: Illocution-Calibrated Policy Optimization (2026)
- **Authors**: Zhebo Wang et al.
- **Source**: arXiv 2601.15330
- **Key Contribution**: Policy optimization for illocutionary calibration in multi-turn dialogue.
- **Relevance**: Another alignment-focused mitigation targeting “lost-in-conversation.”

## Themes and Synthesis

### Common Methodologies
- Multi-turn jailbreak attacks (Crescendo, FITD, RACE, Tempest)
- Representation analysis of multi-turn context (RepE probes)
- Human red teaming pipelines for multi-turn conversations (MHJ)
- Intent mediation or goal tracking to reduce drift (Mediator, OnGoal)

### Standard Baselines
- Single-turn harmful prompts (HarmBench, AdvBench) as baselines
- Automated single-turn attacks (AutoDAN, GCG, PAIR)
- RAG-style memory baselines (Mem0, summarization) for conversation context

### Evaluation Metrics
- Attack Success Rate (ASR)
- Accuracy or task success rate on benchmark tasks
- Reliability / variance across runs
- Human evaluation / harm classifiers for safety

### Datasets in the Literature
- HarmBench
- JailbreakBench JBB-Behaviors
- MHJ (Multi-Turn Human Jailbreaks)
- WMDP-Bio (for unlearning robustness)
- MHSD (mental health sensemaking dialogues)
- MT-Bench

## Research Gaps
- Limited datasets explicitly measuring “prior regression” across long dialogues.
- Few standardized metrics for alignment decay across turns.
- Defensive methods are often evaluated on single-turn attacks; multi-turn robustness remains under-tested.
- Scarcity of open-source, end-to-end implementations for multi-turn defense strategies.

## Recommendations for Our Experiment

- **Recommended datasets**: JBB-Behaviors, WildJailbreak, MT-Bench; optionally MHJ if accessible.
- **Recommended baselines**: Crescendo (multi-turn), FITD, RACE; compare against single-turn attacks.
- **Recommended metrics**: ASR over turns; turn-indexed refusal/comply rates; per-turn “benign vs harmful” representation drift (probe-based if available).
- **Methodological considerations**:
  - Measure turn-indexed degradation (k=1..n) rather than single final-turn score.
  - Separate intent-ambiguity effects from memory/forgetting by controlling input sharding order.
  - Include both multi-turn safety tasks and non-safety dialogue tasks to assess generality.
