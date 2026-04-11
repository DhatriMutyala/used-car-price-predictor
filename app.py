from flask import Flask, render_template, request
import pandas as pd
import pickle
import numpy as np

app = Flask(__name__)


model = pickle.load(open("model.pkl","rb"))
brand_encoder = pickle.load(open("brand_encoder.pkl","rb"))
model_encoder = pickle.load(open("model_encoder.pkl","rb"))


df = pd.read_csv("data/cardekho_dataset.csv")


brand_model_map = df.groupby("brand")["model"].unique().apply(list).to_dict()
brands = sorted(brand_model_map.keys())


@app.route("/")
def home():
    return render_template(
        "index.html",
        brands=brands,
        brand_model_map=brand_model_map
    )


@app.route("/predict", methods=["POST"])
def predict():

    brand = request.form["brand"]
    model_name = request.form["model"]
    age = int(request.form["age"])
    km = int(request.form["km"])

    
    brand_encoded = brand_encoder.transform([brand])[0]
    model_encoded = model_encoder.transform([model_name])[0]

    input_data = np.array([[brand_encoded, model_encoded, age, km]])

    
    prediction = model.predict(input_data)
    price = int(prediction[0])

    
    low_price = price - 50000
    high_price = price + 50000

    return render_template(
        "index.html",
        brands=brands,
        brand_model_map=brand_model_map,
        prediction_text=f"Estimated Price: ₹ {price}",
        price_range=f"₹ {low_price} - ₹ {high_price}"
    )


if __name__ == "__main__":
    app.run(debug=True)