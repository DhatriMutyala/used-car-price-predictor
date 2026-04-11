import pandas as pd
import pickle
from sklearn.ensemble import RandomForestRegressor
from sklearn.preprocessing import LabelEncoder


df = pd.read_csv("cardekho_dataset.csv")


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


pickle.dump(model, open("model.pkl", "wb"))
pickle.dump(brand_encoder, open("brand_encoder.pkl", "wb"))
pickle.dump(model_encoder, open("model_encoder.pkl", "wb"))

print(" Model trained successfully")