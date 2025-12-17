import pandas as pd

df1 = pd.read_csv("results/gsm8k_structured_results.csv")
df2 = pd.read_csv("results/gsm8k_gpt41mini_structured_results.csv")

summary = pd.DataFrame({
    "model": ["gpt-4o-mini", "gpt-4.1-mini"],
    "accuracy": [df1["correct"].mean(), df2["correct"].mean()]
})

summary.to_csv("results/model_comparison.csv", index=False)
print(summary)
