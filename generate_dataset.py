import pandas as pd
from core.bb84_qiskit import run_bb84
from core.error_analysis import calculate_error_rate
from feature_engineering import extract_features

data, labels = [], []

print("Generating dataset...")

for _ in range(600):

    # Secure
    a, b = run_bb84(200, attack=False)
    err = calculate_error_rate(a, b)
    data.append(extract_features(err, len(a)))
    labels.append(0)

    # Attack
    a, b = run_bb84(200, attack=True)
    err = calculate_error_rate(a, b)
    data.append(extract_features(err, len(a)))
    labels.append(1)

df = pd.DataFrame(data, columns=[
    "error_rate","key_length","mismatch","noise","stability"
])

df["label"] = labels
df = df.sample(frac=1).reset_index(drop=True)

df.to_csv("dataset.csv", index=False)

print("✅ Dataset Generated")