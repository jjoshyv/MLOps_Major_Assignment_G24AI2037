import os
from sklearn.datasets import fetch_olivetti_faces
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import joblib

def main():
    model_path = os.path.join("saved_models", "savedmodel.pth")
    if not os.path.exists(model_path):
        raise FileNotFoundError(f"Model not found at {model_path}. Run train.py first.")
    clf = joblib.load(model_path)
    data = fetch_olivetti_faces(shuffle=True, random_state=42)
    X = data.data
    y = data.target
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.30, random_state=42, stratify=y
    )
    y_pred = clf.predict(X_test)
    acc = accuracy_score(y_test, y_pred)
    print(f"Test accuracy (test.py): {acc:.4f}")

if __name__ == "__main__":
    main()
