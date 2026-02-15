import json
import subprocess
import sys
from datetime import datetime

import numpy as np
import pandas as pd
import matplotlib
import seaborn
import scipy
import openai

from .config import RESULTS_DIR


def gpu_info() -> str:
    try:
        out = subprocess.check_output(
            "nvidia-smi --query-gpu=name,memory.total,memory.free --format=csv",
            shell=True,
            text=True,
        )
        return out.strip()
    except subprocess.CalledProcessError:
        return "NO_GPU"


def main() -> None:
    info = {
        "timestamp": datetime.utcnow().isoformat() + "Z",
        "python": sys.version,
        "numpy": np.__version__,
        "pandas": pd.__version__,
        "matplotlib": matplotlib.__version__,
        "seaborn": seaborn.__version__,
        "scipy": scipy.__version__,
        "openai": openai.__version__,
        "gpu": gpu_info(),
    }
    out_path = RESULTS_DIR / "metadata.json"
    out_path.parent.mkdir(parents=True, exist_ok=True)
    with out_path.open("w", encoding="utf-8") as f:
        json.dump(info, f, indent=2)
    print(f"Saved environment metadata to {out_path}")


if __name__ == "__main__":
    main()
