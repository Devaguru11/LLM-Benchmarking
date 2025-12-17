from datasets import load_dataset
from openai import OpenAI
import re, time
import pandas as pd

client = OpenAI()

dataset = load_dataset("gsm8k", "main")
test_data = dataset["test"].select(range(20))

def extract_answer(text):
    nums = re.findall(r"\d+", text)
    return nums[-1] if nums else None

rows = []

for idx, item in enumerate(test_data):
    prompt = f"""
Solve the problem.
Return ONLY the final numeric answer.

Question: {item['question']}
"""

    response = client.chat.completions.create(
        model="gpt-4.1-mini",
        messages=[{"role": "user", "content": prompt}],
        max_tokens=20
    )

    output = response.choices[0].message.content
    prediction = extract_answer(output)
    truth = extract_answer(item["answer"])

    rows.append({
        "id": idx,
        "benchmark": "GSM8K",
        "model": "gpt-4o-mini",
        "question": item["question"],
        "prediction": prediction,
        "ground_truth": truth,
        "correct": prediction == truth
    })

    time.sleep(0.3)

df = pd.DataFrame(rows)

df.to_csv("results/gsm8k_gpt41mini_structured_results.csv", index=False)

print("Accuracy:", df["correct"].mean())
