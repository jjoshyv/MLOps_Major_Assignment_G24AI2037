import os
from sklearn.datasets import fetch_olivetti_faces
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score
import joblib

def main():
    os.makedirs("saved_models", exist_ok=True)
    data = fetch_olivetti_faces(shuffle=True, random_state=42)
    X = data.data
    y = data.target
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.30, random_state=42, stratify=y
    )
    clf = DecisionTreeClassifier(random_state=42)
    clf.fit(X_train, y_train)
    y_pred = clf.predict(X_test)
    acc = accuracy_score(y_test, y_pred)
    print(f"Test accuracy (train.py): {acc:.4f}")
    save_path = os.path.join("saved_models", "savedmodel.pth")
    joblib.dump(clf, save_path)
    print(f"Saved model to {save_path}")

if __name__ == "__main__":
    main()
