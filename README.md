# Multi-Turn Prior Regression Study

This project tests whether multi-turn conversations cause LLMs to regress toward a base prior, weakening alignment over turns. We evaluate `gpt-4.1` on safety and benign multi-turn datasets with turn-indexed metrics.

## Key Findings
- JBB harmful compliance stayed flat from turn 1 to turn 3.
- WildJailbreak compliance decreased from 0.75 to 0.35 with added turns.
- MT-Bench success dropped slightly (0.80 → 0.75) without statistical significance.

## How to Reproduce
1. Activate environment
```
source .venv/bin/activate
```
2. Run data checks
```
python -m src.data_checks
```
3. Run experiments (example sizes)
```
JBB_SAMPLE_SIZE=20 WJ_SAMPLE_SIZE=20 MT_BENCH_SAMPLE_SIZE=20 TURN_COUNTS=1,3 MAX_TOKENS=256 python -m src.run_experiments
```
4. Score outputs
```
MAX_TOKENS=256 python -m src.score_outputs
```
5. Analyze results
```
python -m src.analyze_results
```

## File Structure
- `src/`: experiment scripts
- `datasets/`: downloaded datasets
- `results/`: outputs, scores, plots, metadata
- `planning.md`: research plan
- `REPORT.md`: full report with results and analysis

See `REPORT.md` for detailed methodology, results, and limitations.
