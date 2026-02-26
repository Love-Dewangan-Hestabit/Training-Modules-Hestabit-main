import json
import os
import numpy as np
import matplotlib.pyplot as plt
from transformers import AutoTokenizer
from sklearn.model_selection import train_test_split

RAW_PATH = "src/data/raw_dataset.jsonl"
TRAIN_PATH = "src/data/train.jsonl"
VAL_PATH = "src/data/val.jsonl"

tokenizer = AutoTokenizer.from_pretrained("gpt2")


def load_dataset():
    with open(RAW_PATH, "r") as f:
        return [json.loads(line) for line in f]


def token_length(sample):
    text = sample["instruction"] + sample["input"] + sample["output"]
    return len(tokenizer.encode(text))


def clean_dataset(dataset):
    cleaned = []
    lengths = []

    for sample in dataset:
        if not sample["output"].strip():
            continue

        length = token_length(sample)
        sample["token_length"] = length
        cleaned.append(sample)
        lengths.append(length)

    return cleaned, lengths


def remove_outliers(dataset, lengths):
    mean = np.mean(lengths)
    std = np.std(lengths)

    filtered = []
    for sample in dataset:
        if abs(sample["token_length"] - mean) <= 2 * std:
            filtered.append(sample)

    return filtered


def plot_distribution(lengths):
    plt.figure(figsize=(8, 5))
    plt.hist(lengths, bins=40)
    plt.title("Token Length Distribution (After Outlier Removal)")
    plt.xlabel("Token Count")
    plt.ylabel("Frequency")
    plt.tight_layout()
    plt.savefig("src/data/token_distribution_after.png")
    plt.close()


def save_split(dataset):
    train, val = train_test_split(dataset, test_size=0.2, random_state=42)

    for path, data in [(TRAIN_PATH, train), (VAL_PATH, val)]:
        with open(path, "w") as f:
            for sample in data:
                sample.pop("token_length", None)
                f.write(json.dumps(sample) + "\n")

    print("Train/Val split saved.")


def main():
    dataset = load_dataset()

    cleaned, lengths = clean_dataset(dataset)

    print("\nToken Length Analysis Before Removing the Outliers:")
    print(f"Total samples: {len(lengths)}")
    print(f"Mean: {np.mean(lengths):.2f}")
    print(f"Std: {np.std(lengths):.2f}")
    print(f"Min: {np.min(lengths)}")
    print(f"Max: {np.max(lengths)}")

    filtered = remove_outliers(cleaned, lengths)
    filtered_lengths = [sample["token_length"] for sample in filtered]

    print("\nAfter Outlier Removal:")
    print(f"Remaining samples: {len(filtered)}")
    print(f"Removed samples: {len(cleaned) - len(filtered)}")

    plot_distribution(filtered_lengths)


    save_split(filtered)

    print("\nFinal dataset size:", len(filtered))


if __name__ == "__main__":
    main()