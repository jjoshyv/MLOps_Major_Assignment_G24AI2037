import os
import io
from PIL import Image, ImageOps
import numpy as np
import joblib
from flask import Flask, request, render_template_string, jsonify

MODEL_PATH = os.path.join("saved_models", "savedmodel.pth")

app = Flask(__name__)

HTML = """
<!doctype html>
<title>Olivetti Faces - Predict</title>
<h1>Upload face image (converted to 64x64 grayscale)</h1>
<form method=post enctype=multipart/form-data>
  <input type=file name=file accept="image/*">
  <input type=submit value=Upload>
</form>
{% if pred is defined %}
  <h2>Predicted class: {{ pred }}</h2>
{% endif %}
"""

def load_model():
    if not os.path.exists(MODEL_PATH):
        raise FileNotFoundError("Model not found. Run train.py and ensure saved_models/savedmodel.pth exists.")
    return joblib.load(MODEL_PATH)

def preprocess_image(stream):
    img = Image.open(io.BytesIO(stream.read())).convert("L")
    img = ImageOps.fit(img, (64, 64))
    arr = np.asarray(img, dtype=np.float32) / 255.0
    return arr.flatten().reshape(1, -1)

@app.route("/", methods=["GET", "POST"])
def index():
    pred = None
    if request.method == "POST":
        if "file" not in request.files:
            return "No file part", 400
        file = request.files["file"]
        if file.filename == "":
            return "No selected file", 400
        try:
            X = preprocess_image(file.stream)
            model = load_model()
            y = model.predict(X)
            pred = int(y[0])
            return render_template_string(HTML, pred=pred)
        except Exception as e:
            return f"Error processing image: {e}", 500
    return render_template_string(HTML)

@app.route("/predict", methods=["POST"])
def predict_api():
    if "file" not in request.files:
        return jsonify({"error": "no file part"}), 400
    file = request.files["file"]
    if file.filename == "":
        return jsonify({"error": "no selected file"}), 400
    try:
        X = preprocess_image(file.stream)
        model = load_model()
        y = model.predict(X)
        return jsonify({"prediction": int(y[0])})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
