import pandas as pd
import pickle
import os
from sklearn.ensemble import RandomForestRegressor
from sklearn.preprocessing import LabelEncoder

# load dataset
df = pd.read_csv("data/cardekho_dataset.csv")

# required columns check
required_cols = ["brand", "model", "vehicle_age", "km_driven", "selling_price"]
for col in required_cols:
    if col not in df.columns:
        raise Exception(f"Missing column: {col}")

# encoders
brand_encoder = LabelEncoder()
model_encoder = LabelEncoder()

df["brand"] = brand_encoder.fit_transform(df["brand"].astype(str))
df["model"] = model_encoder.fit_transform(df["model"].astype(str))

# features and target
X = df[["brand", "model", "vehicle_age", "km_driven"]]
y = df["selling_price"]

# train model
model = RandomForestRegressor(n_estimators=300, random_state=42)
model.fit(X, y)

# create models folder if not exists
os.makedirs("models", exist_ok=True)

# save model and encoders
pickle.dump(model, open("models/car_price_model.pkl", "wb"))
pickle.dump(brand_encoder, open("models/brand_encoder.pkl", "wb"))
pickle.dump(model_encoder, open("models/model_encoder.pkl", "wb"))

print("Model trained successfully")