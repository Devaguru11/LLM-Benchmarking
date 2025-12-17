from datasets import load_dataset

dataset = load_dataset("gsm8k", "main")
print(dataset["test"][0])
