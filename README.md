# 🚀 LLM Benchmarking & Evaluation (End-to-End Framework)

This repository presents a **complete, end-to-end implementation of benchmarking and evaluating Large Language Models (LLMs)** using standardized datasets and structured evaluation pipelines.

The project is built as part of an **Agentic AI / LLM Benchmarking internship** and is intended for:
- Learning how real-world LLM evaluation works
- Conducting reproducible AI experiments
- Comparing multiple LLMs using standard benchmarks
- Preparing research-ready and internship-grade outputs

---

## 📌 Why This Project?

Large Language Models are powerful, but **measuring their performance objectively** is critical.  
This project focuses on **how to evaluate LLMs correctly**, not just how to use them.

Key focus areas:
- Standard benchmark datasets
- Proper evaluation metrics
- Structured result storage
- Reproducibility
- Clean research workflow

---

## 🎯 Project Objectives

- Understand LLM benchmarking fundamentals
- Run standardized evaluation using GSM8K
- Build a reusable benchmarking pipeline
- Generate structured CSV outputs
- Compare models using accuracy
- Follow best practices in Git and experiment tracking

---

## 📊 Benchmarks Covered

### ✅ Implemented
- **GSM8K** – Grade School Math 8K  
  *(Evaluates mathematical reasoning and logical problem solving)*

### 🔜 Planned / Extendable
- **MMLU** – Multi-domain knowledge evaluation
- **HumanEval** – Code generation benchmark
- **AgentBench** – Agent-based task evaluation

---

## 🧠 What You Learn From This Project

- How benchmark datasets are structured
- How LLM outputs are parsed and evaluated
- How accuracy is computed programmatically
- How to design reproducible AI experiments
- How to manage API-based experimentation
- How to maintain clean ML repositories on GitHub

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
⚙️ System Requirements
Python 3.9 or above

Git

macOS / Linux / Windows

Internet connection

OpenAI API key (billing enabled)

🛠️ Environment Setup (Step-by-Step)
1️⃣ Clone the Repository
bash
Copy code
git clone https://github.com/<your-username>/LLM-Benchmarking.git
cd LLM-Benchmarking
2️⃣ Create & Activate Virtual Environment
bash
Copy code
python3 -m venv venv
source venv/bin/activate
Virtual environments are used to isolate dependencies and avoid conflicts.

3️⃣ Install Dependencies
bash
Copy code
pip install -r requirements.txt
If requirements.txt is missing:

bash
Copy code
pip install transformers datasets openai pandas numpy
4️⃣ Set OpenAI API Key
bash
Copy code
export OPENAI_API_KEY="your_api_key_here"
💡 For permanent setup, add the export line to ~/.zshrc or ~/.bashrc.

▶️ Running the GSM8K Benchmark
Execute the Benchmark Script
bash
Copy code
python3 scripts/run_gsm8k.py
⚙️ What Happens Internally
The benchmark script performs the following steps:

Loads the GSM8K dataset using Hugging Face datasets

Selects a subset of test questions

Sends each question to the LLM via OpenAI API

Restricts output to the final numeric answer

Extracts the predicted answer

Compares prediction with ground truth

Computes accuracy

Saves structured results to CSV

📊 Output: Structured CSV Results
File Location
text
Copy code
results/gsm8k_structured_results.csv
CSV Schema
Column Name	Description
id	Question index
benchmark	Benchmark name (GSM8K)
model	LLM used
question	Problem statement
prediction	Model’s final answer
ground_truth	Correct answer
correct	True / False

This structure allows:

Easy comparison

Statistical analysis

Visualization

Research reporting

📈 Model Comparison
After running benchmarks with multiple models:

bash
Copy code
python3 scripts/compare_results.py
Output
text
Copy code
results/model_comparison.csv
This file summarizes:

Model name

Accuracy score

