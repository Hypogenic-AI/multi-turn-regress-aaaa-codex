# Outline: Do Multi-Turn Conversations Regress to the Prior?

## Title
- Emphasize multi-turn safety drift and null/negative regression finding

## Abstract
- Problem: multi-turn robustness and prior regression
- Gap: turn-indexed evidence limited
- Approach: controlled turn-count comparison on safety + benign datasets using API eval
- Key results: JBB flat, WildJailbreak compliance down 0.40 (p=0.0047), MT-Bench slight nonsig drop
- Significance: multi-turn can strengthen refusals; need larger scale and attack ablations

## Introduction
- Hook: multi-turn is dominant interaction mode; safety drift risk
- Importance: deployment safety depends on turn robustness
- Gap: few turn-indexed measurements disentangling prior regression vs escalation
- Approach: compare turn count 1 vs 3 with matched final request; evaluate safety + benign
- Quant preview: WildJailbreak compliance 0.75→0.35; JBB flat; MT-Bench 0.80→0.75
- Contributions (3-4 bullets): dataset construction, controlled turn comparison, empirical findings

## Related Work
- Multi-turn jailbreaks (Crescendo, FITD, RACE, Tempest)
- Human red-teaming and datasets (MHJ, JBB-Behaviors, WildJailbreak)
- Drift/representation analyses and mitigation (RepE, Mediator, OnGoal, ICPO)
- Positioning: we measure turn-indexed drift with controlled baselines

## Methodology
- Problem formulation: test for regression via turn-indexed metrics
- Datasets and sampling
- Multi-turn construction with benign lead-ins
- Models and evaluation (gpt-4.1 gen + judge)
- Metrics: compliance, refusal, MT-Bench success
- Statistical tests: Wilcoxon

## Results
- Table: safety compliance/refusal by dataset and turn
- Table: MT-Bench success by turn
- Figure: three plots from results/plots
- Statistical analysis with p-values
- Comparison to baselines (single-turn)

## Discussion
- Interpretation: multi-turn can reinforce refusals
- Limitations: small N, single model/judge, no attack scripts, binary MT-Bench
- Broader implications: multi-turn safety evaluation needed

## Conclusion
- Summarize findings and future work

## References
- Use bib entries from literature review and datasets
