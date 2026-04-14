import pandas as pd
import pickle
import os
from sklearn.ensemble import RandomForestRegressor
from sklearn.preprocessing import LabelEncoder

df = pd.read_csv("data/cardekho_dataset.csv")

required_cols = ["brand", "model", "vehicle_age", "km_driven", "selling_price"]
for col in required_cols:
    if col not in df.columns:
        raise Exception(f"Missing column: {col}")

brand_encoder = LabelEncoder()
model_encoder = LabelEncoder()

df["brand"] = brand_encoder.fit_transform(df["brand"].astype(str))
df["model"] = model_encoder.fit_transform(df["model"].astype(str))

X = df[["brand", "model", "vehicle_age", "km_driven"]]
y = df["selling_price"]

model = RandomForestRegressor(n_estimators=300, random_state=42)
model.fit(X, y)

os.makedirs("models", exist_ok=True)

with open("models/car_price_model.pkl", "wb") as f:
    pickle.dump(model, f)

with open("models/brand_encoder.pkl", "wb") as f:
    pickle.dump(brand_encoder, f)

with open("models/model_encoder.pkl", "wb") as f:
    pickle.dump(model_encoder, f)

print("Model trained successfully")