# Resources Catalog

## Summary
This document catalogs all resources gathered for the research project, including papers, datasets, and code repositories.

### Papers
Total papers downloaded: 13

| Title | Authors | Year | File | Key Info |
|-------|---------|------|------|----------|
| Intent Mismatch Causes LLMs to Get Lost in Multi-Turn Conversation | Liu et al. | 2026 | `papers/must_read/2602.07338_intent_mismatch_multi_turn.pdf` | Mediator reduces LiC degradation |
| A Representation Engineering Perspective on the Effectiveness of Multi-Turn Jailbreaks | Bullwinkel et al. | 2025 | `papers/must_read/2507.02956_representation_engineering_multi_turn_jailbreaks.pdf` | Multi-turn shifts representations toward benign |
| Foot-In-The-Door: A Multi-turn Jailbreak for LLMs | Weng et al. | 2025 | `papers/should_read/2502.19820_foot_in_the_door_jailbreak.pdf` | Escalation attack, high ASR |
| Tempest: Autonomous Multi-Turn Jailbreaking with Tree Search | Zhou, Arel | 2025 | `papers/should_read/2503.10619_tempest_multi_turn_jailbreaking.pdf` | Tree-search multi-turn attack |
| Great, Now Write an Article About That (Crescendo) | Russinovich et al. | 2024 | `papers/should_read/2404.01833_crescendo_multiturn_jailbreak.pdf` | Canonical multi-turn jailbreak |
| RACE: Reasoning-Augmented Conversation | Ying et al. | 2025 | `papers/should_read/2502.11054_reasoning_augmented_conversation_race.pdf` | Multi-turn reasoning attack |
| MTSA: Multi-turn Safety Alignment | Guo et al. | 2025 | `papers/should_read/2505.17147_mtsa_multi_turn_safety_alignment.pdf` | Multi-round red-teaming alignment |
| STREAM: Safety Reasoning Elicitation Alignment | Kuo et al. | 2025 | `papers/should_read/2506.00668_stream_safety_reasoning_elicitation.pdf` | Safety dataset + moderator |
| Reasoning Is Not All You Need (MHSD) | Chandra et al. | 2025 | `papers/should_read/2505.20201_reasoning_not_all_you_need_mhsd.pdf` | MHSD dataset; multi-turn drop |
| Beyond One-Way Influence: Bidirectional Opinion Dynamics | Jiang et al. | 2025 | `papers/should_read/2510.20039_bidirectional_opinion_dynamics.pdf` | Multi-turn stance drift |
| LLM Defenses Are Not Robust to Multi-Turn Human Jailbreaks Yet | Li et al. | 2024 | `papers/should_read/2408.15221_llm_defenses_multi_turn_human_jailbreaks.pdf` | MHJ dataset; human ASR gap |
| OnGoal: Tracking Conversational Goals | Coscia et al. | 2025 | `papers/should_read/2508.21061_ongoal_goal_tracking.pdf` | Goal tracking UI |
| ICPO: Illocution-Calibrated Policy Optimization | Wang et al. | 2026 | `papers/should_read/2601.15330_icpo_illocution_calibrated_policy_optimization.pdf` | Illocution-calibrated alignment |

See `papers/README.md` for detailed descriptions.

### Datasets
Total datasets downloaded: 3

| Name | Source | Size | Task | Location | Notes |
|------|--------|------|------|----------|-------|
| JBB-Behaviors | HuggingFace | 200 examples | Jailbreak behaviors | `datasets/jbb_behaviors/` | Harmful/benign pairs |
| MT-Bench | HuggingFace | 80 prompts | Multi-turn eval | `datasets/mt_bench/` | Standard multi-turn prompts |
| WildJailbreak | HuggingFace | 2,210 examples | Real-world jailbreaks | `datasets/wildjailbreak/` | In-the-wild prompts |

See `datasets/README.md` for detailed descriptions.

### Code Repositories
Total repositories cloned: 4

| Name | URL | Purpose | Location | Notes |
|------|-----|---------|----------|-------|
| Foot-in-the-door-Jailbreak | https://github.com/Jinxiaolong1129/Foot-in-the-door-Jailbreak | FITD multi-turn attack | `code/foot-in-the-door-jailbreak/` | Includes prompts/data |
| RACE | https://github.com/NY1024/RACE | Multi-turn reasoning attack | `code/race/` | Partial release |
| Crescendomation | https://github.com/AIM-Intelligence/Automated-Multi-Turn-Jailbreaks | Automated Crescendo tactics | `code/crescendomation/` | OpenAI-style API |
| JailbreakBench | https://github.com/JailbreakBench/jailbreakbench | Benchmark and loaders | `code/jailbreakbench/` | Dataset + eval tooling |

See `code/README.md` for detailed descriptions.

## Resource Gathering Notes

### Search Strategy
- Used paper-finder for relevance-ranked paper discovery.
- Followed up with arXiv to download PDFs.
- Identified datasets and code via GitHub and HuggingFace.

### Selection Criteria
- Direct relevance to multi-turn degradation, alignment drift, or safety decay.
- Multi-turn evaluation focus.
- Availability of datasets or code to support experiments.

### Challenges Encountered
- Some datasets (e.g., MHJ) may require gated access via official release.
- Some code repositories are partial releases (RACE).

### Gaps and Workarounds
- If MHJ is inaccessible, use WildJailbreak + JBB-Behaviors + MT-Bench as substitutes.

## Recommendations for Experiment Design

1. **Primary dataset(s)**: JBB-Behaviors (control), WildJailbreak (in-the-wild), MT-Bench (multi-turn task prompts)
2. **Baseline methods**: Crescendo, FITD, RACE; single-turn attacks for control
3. **Evaluation metrics**: ASR over turns, refusal rate by turn, turn-indexed drift scores
4. **Code to adapt/reuse**: JailbreakBench evaluation harness; Crescendomation for automation
