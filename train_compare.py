import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report
from sklearn.preprocessing import StandardScaler
from ml.advanced_model import train_models

df = pd.read_csv("dataset.csv")

X = df[["error_rate","key_length","mismatch","noise","stability"]].values
y = df["label"].values

scaler = StandardScaler()
X = scaler.fit_transform(X)

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3)

models = train_models(X_train, y_train)

print("\n📊 FINAL MODEL RESULTS\n")

for name, model in models.items():
    pred = model.predict(X_test)
    acc = accuracy_score(y_test, pred)

    print(f"{name} Accuracy: {acc:.3f}")
    print(classification_report(y_test, pred, zero_division=0))
    print("-"*50)