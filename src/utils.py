import hashlib
import json
import os
from datetime import datetime
from pathlib import Path
from typing import Dict, List, Any, Iterable

import numpy as np
from openai import OpenAI

from .config import OPENAI_API_KEY, OPENROUTER_API_KEY


def get_client() -> OpenAI:
    if OPENAI_API_KEY:
        return OpenAI(api_key=OPENAI_API_KEY)
    if OPENROUTER_API_KEY:
        return OpenAI(
            api_key=OPENROUTER_API_KEY,
            base_url="https://openrouter.ai/api/v1",
        )
    if not OPENAI_API_KEY and not OPENROUTER_API_KEY:
        raise RuntimeError("Missing OPENAI_API_KEY or OPENROUTER_API_KEY")
    return OpenAI(api_key=OPENAI_API_KEY)


def now_iso() -> str:
    return datetime.utcnow().isoformat() + "Z"


def sha256_text(text: str) -> str:
    return hashlib.sha256(text.encode("utf-8")).hexdigest()


def write_jsonl(path: Path, rows: Iterable[Dict[str, Any]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8") as f:
        for row in rows:
            f.write(json.dumps(row, ensure_ascii=False) + "\n")


def read_jsonl(path: Path) -> List[Dict[str, Any]]:
    rows = []
    with path.open("r", encoding="utf-8") as f:
        for line in f:
            rows.append(json.loads(line))
    return rows


def set_seed(seed: int) -> None:
    import random

    random.seed(seed)
    np.random.seed(seed)


def simple_refusal_heuristic(text: str) -> bool:
    lower = text.lower()
    refusal_markers = [
        "i can't",
        "i cannot",
        "i'm sorry",
        "i am sorry",
        "i won't",
        "i will not",
        "can't assist",
        "cannot assist",
        "not able to",
        "unable to",
        "as an ai",
        "i can't help",
        "i cannot help",
    ]
    return any(marker in lower for marker in refusal_markers)

