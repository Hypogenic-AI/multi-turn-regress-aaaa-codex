# Downloaded Datasets

This directory contains datasets for the research project. Data files are NOT committed to git due to size. Follow the download instructions below.

## Dataset 1: JailbreakBench JBB-Behaviors

### Overview
- **Source**: HuggingFace `JailbreakBench/JBB-Behaviors`
- **Size**: 200 examples total (100 harmful + 100 benign)
- **Format**: HuggingFace Dataset
- **Task**: Jailbreak behavior/goal evaluation
- **Splits**: `harmful` (100), `benign` (100)
- **License**: See HuggingFace dataset card

### Download Instructions

**Using HuggingFace (recommended):**
```python
from datasets import load_dataset
jbb = load_dataset("JailbreakBench/JBB-Behaviors", "behaviors")
jbb.save_to_disk("datasets/jbb_behaviors")
```

### Loading the Dataset
```python
from datasets import load_from_disk
jbb = load_from_disk("datasets/jbb_behaviors")
```

### Sample Data
See `datasets/jbb_behaviors/samples.json`.

### Notes
- This is the core benchmark used by several jailbreak papers and is light-weight.

---

## Dataset 2: MT-Bench

### Overview
- **Source**: HuggingFace `lighteval/mt-bench`
- **Size**: 80 multi-turn prompts
- **Format**: HuggingFace Dataset
- **Task**: Multi-turn conversation evaluation
- **Splits**: `train` (80)
- **License**: See HuggingFace dataset card

### Download Instructions

**Using HuggingFace (recommended):**
```python
from datasets import load_dataset
mt = load_dataset("lighteval/mt-bench")
mt.save_to_disk("datasets/mt_bench")
```

### Loading the Dataset
```python
from datasets import load_from_disk
mt = load_from_disk("datasets/mt_bench")
```

### Sample Data
See `datasets/mt_bench/samples.json`.

---

## Dataset 3: WildJailbreak

### Overview
- **Source**: HuggingFace `walledai/WildJailbreak`
- **Size**: 2,210 examples
- **Format**: HuggingFace Dataset
- **Task**: Real-world jailbreak prompts
- **Splits**: `train` (2210)
- **License**: See HuggingFace dataset card

### Download Instructions

**Using HuggingFace (recommended):**
```python
from datasets import load_dataset
wj = load_dataset("walledai/WildJailbreak")
wj.save_to_disk("datasets/wildjailbreak")
```

### Loading the Dataset
```python
from datasets import load_from_disk
wj = load_from_disk("datasets/wildjailbreak")
```

### Sample Data
See `datasets/wildjailbreak/samples.json`.

---

## Optional Dataset: Multi-Turn Human Jailbreaks (MHJ)

### Overview
- **Source**: ScaleAI MHJ (public release)
- **Access**: Requires downloading from the official release or HuggingFace dataset card (may be gated)

### Download Instructions (if available)
```python
from datasets import load_dataset
mhj = load_dataset("ScaleAI/mhj")
mhj.save_to_disk("datasets/mhj")
```

### Notes
- If access is gated, use the public download link at the official release page.
