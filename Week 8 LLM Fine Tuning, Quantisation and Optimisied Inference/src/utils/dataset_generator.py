import json
import random
import os
from faker import Faker

fake = Faker()

OUTPUT_PATH = "src/data/raw_dataset.jsonl"
NUM_SAMPLES = 1000


OUTLIER_RATIO = 0.07 

finance_terms = [
    "compound interest", "inflation", "dividend yield",
    "market capitalization", "EBITDA", "P/E ratio",
    "mutual fund", "ETF", "bond yield", "capital gain"
]



def generate_qa_sample():
    term = random.choice(finance_terms)
    return {
        "instruction": "Answer the finance question.",
        "input": f"What is {term}?",
        "output": f"{term} is a financial concept commonly used in investment and economic analysis."
    }


def generate_reasoning_sample():
    principal = random.randint(1000, 10000)
    rate = random.uniform(3, 10)
    years = random.randint(1, 10)

    amount = principal * ((1 + rate/100) ** years)

    return {
        "instruction": "Solve the financial problem step by step.",
        "input": f"If an investment of ${principal} earns {rate:.2f}% annually for {years} years, what is the final amount?",
        "output": f"Using compound interest formula A = P(1+r)^t, the final amount is approximately ${amount:.2f}."
    }


def generate_extraction_sample():
    revenue = random.randint(50000, 500000)
    expense = random.randint(10000, 400000)
    net_income = revenue - expense

    report = f"""
    Company Report:
    Total Revenue: ${revenue}
    Total Expenses: ${expense}
    Net Income: ${net_income}
    """

    return {
        "instruction": "Extract the Net Income from the report.",
        "input": report.strip(),
        "output": f"${net_income}"
    }



def generate_long_reasoning_outlier():
    """Very long explanation"""
    principal = random.randint(1000, 10000)
    rate = random.uniform(3, 10)
    years = random.randint(5, 20)

    long_explanation = (
        "To solve this financial problem, we must carefully analyze the compound interest formula. "
        * 40 
    )

    amount = principal * ((1 + rate/100) ** years)

    return {
        "instruction": "Solve the financial problem step by step.",
        "input": f"If an investment of ${principal} earns {rate:.2f}% annually for {years} years, what is the final amount?",
        "output": long_explanation + f"The final amount is ${amount:.2f}."
    }


def generate_short_outlier():
    """Extremely short useless output"""
    return {
        "instruction": "Answer briefly.",
        "input": "What is inflation?",
        "output": "Yes."
    }


def generate_empty_outlier():
    """Empty output to test cleaning"""
    return {
        "instruction": "Extract value.",
        "input": "Revenue: $50000",
        "output": ""
    }


def generate_noise_outlier():
    """Random noisy long text"""
    noise = " ".join([fake.word() for _ in range(300)])
    return {
        "instruction": "Summarize the report.",
        "input": fake.paragraph(),
        "output": noise
    }




def generate_dataset():
    os.makedirs("src/data", exist_ok=True)

    dataset = []
    num_outliers = int(NUM_SAMPLES * OUTLIER_RATIO)

    for i in range(NUM_SAMPLES):

 
        if i < num_outliers:
            outlier_type = random.choice(
                ["long", "short", "empty", "noise"]
            )

            if outlier_type == "long":
                dataset.append(generate_long_reasoning_outlier())
            elif outlier_type == "short":
                dataset.append(generate_short_outlier())
            elif outlier_type == "empty":
                dataset.append(generate_empty_outlier())
            else:
                dataset.append(generate_noise_outlier())

 
        else:
            sample_type = random.choice(["qa", "reasoning", "extraction"])

            if sample_type == "qa":
                dataset.append(generate_qa_sample())
            elif sample_type == "reasoning":
                dataset.append(generate_reasoning_sample())
            else:
                dataset.append(generate_extraction_sample())

    random.shuffle(dataset)

    with open(OUTPUT_PATH, "w") as f:
        for sample in dataset:
            f.write(json.dumps(sample) + "\n")

    print(f"Generated {len(dataset)} samples at {OUTPUT_PATH}")
    print(f"Included approximately {num_outliers} artificial outliers.")


if __name__ == "__main__":
    generate_dataset()