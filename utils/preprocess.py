import pandas as pd

def load_and_preprocess():

    df = pd.read_csv("data/cardekho_dataset.csv")

    
    if "car_name" in df.columns:
        df = df.drop("car_name", axis=1)

    
    df = pd.get_dummies(df, columns=[
        "brand",
        "model",
        "seller_type",
        "fuel_type",
        "transmission_type"
    ], drop_first=True)

    return df