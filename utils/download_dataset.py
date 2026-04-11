import os

dataset = "athirags/car-data"

print("Downloading dataset...")

os.system(f"kaggle datasets download -d {dataset} -p data --unzip")

print("Dataset downloaded successfully")