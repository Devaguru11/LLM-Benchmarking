# LLM Benchmarking and Evaluation

This repository contains an implementation of a benchmarking pipeline for evaluating Large Language Models (LLMs) using standard datasets.  
The project demonstrates environment setup, benchmark execution, structured result generation, and model comparison.

---

## What This Project Does

- Runs LLM benchmarking using the **GSM8K** dataset
- Evaluates model performance using **accuracy**
- Stores results in a **structured CSV format**
- Allows easy comparison between multiple models
- Follows clean Git and reproducibility practices

---

## Requirements

- Python 3.9 or above
- Git
- OpenAI API key (with billing enabled)

---

## Setup Instructions

### 1. Clone the repository
```bash
git clone https://github.com/<your-username>/LLM-Benchmarking.git
cd LLM-Benchmarking
```

### 2. Create and activate virtual environment
```bash
python3 -m venv venv
source venv/bin/activate
```
### 3. Install dependencies
```bash
pip install -r requirements.txt
```
### If requirements.txt is not present:
```bash
pip install transformers datasets openai pandas numpy
```
### 4. Set OpenAI API key
```bash
export OPENAI_API_KEY="your_api_key_here"
```
---

## Running the Benchmark
### GSM8K Evaluation
```bash
python3 scripts/run_gsm8k.py
```

### This script:

- Loads the GSM8K dataset

- Sends questions to the LLM

- Extracts final numeric answers

- Computes accuracy

- Saves structured results to CSV

---

## Output
### Structured Results File
```bash
results/gsm8k_structured_results.csv
```

### CSV Columns

- id

- benchmark

- model

- question

- prediction

- ground_truth

- correct


### Model Comparison

After running benchmarks for multiple models:
```bash
python3 scripts/compare_results.py
```

This generates:
```bash
results/model_comparison.csv
```

## Notes

- Virtual environment (venv/) is excluded from Git

- API keys should never be committed

- Sample size can be adjusted in run_gsm8k.py

- Start with small samples before scaling

---

## 📂 Project Structure

```text
LLM-Benchmarking/
│
├── scripts/
│   ├── load_data.py              # Dataset loading & inspection
│   ├── run_gsm8k.py              # GSM8K benchmark execution
│   └── compare_results.py        # Model comparison script
│
├── results/
│   ├── gsm8k_structured_results.csv
│   └── model_comparison.csv
│
├── .gitignore                    # Prevents pushing venv, keys, binaries
├── README.md                     # Project documentation
└── requirements.txt              # Dependencies
```

