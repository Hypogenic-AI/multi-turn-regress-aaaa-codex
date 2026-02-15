import os
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DATASETS_DIR = ROOT / "datasets"
RESULTS_DIR = ROOT / "results"
LOGS_DIR = ROOT / "logs"
FIGURES_DIR = ROOT / "figures"

MODEL_NAME = os.getenv("MODEL_NAME", "gpt-4.1")
JUDGE_MODEL_NAME = os.getenv("JUDGE_MODEL_NAME", MODEL_NAME)

TEMPERATURE = float(os.getenv("TEMPERATURE", "0"))
MAX_TOKENS = int(os.getenv("MAX_TOKENS", "512"))

SEED = int(os.getenv("SEED", "42"))

OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

# Experiment sizes
JBB_SAMPLE_SIZE = int(os.getenv("JBB_SAMPLE_SIZE", "100"))
WJ_SAMPLE_SIZE = int(os.getenv("WJ_SAMPLE_SIZE", "100"))
MT_BENCH_SAMPLE_SIZE = int(os.getenv("MT_BENCH_SAMPLE_SIZE", "80"))

# Turn counts for safety drift
TURN_COUNTS = [int(x) for x in os.getenv("TURN_COUNTS", "1,3").split(",") if x.strip()]
