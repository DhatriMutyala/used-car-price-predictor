# Used Car Price Predictor

A Machine Learning web application that predicts the selling price of a used car based on different features such as brand, fuel type, transmission, mileage, engine capacity, and more.

This project uses **Python, Flask, and Scikit-Learn** to train a regression model and provide predictions through a simple web interface.


# Features

• Predicts used car prices using a trained machine learning model
• Web interface built with Flask
• Automatic model training if the trained model is missing
• Dataset included inside the repository
• Easy to run after cloning the repository



# Technologies Used

Python
Flask
Pandas
NumPy
Scikit-Learn
HTML
CSS
JavaScript



# Project Structure

used-car-price-predictor
│
├── data
│   └── cardekho_dataset.csv
│
├── static
│   ├── style.css
│   └── script.js
│
├── templates
│   └── index.html
│
├── utils
│   ├── preprocess.py
│   └── download_dataset.py
│
├── app.py
├── train_model.py
├── requirements.txt
├── README.md
└── .gitignore


# Dataset

The project uses the **CarDekho Used Car Dataset**, which contains information such as:

* Car brand
* Model
* Vehicle age
* Kilometers driven
* Fuel type
* Transmission type
* Engine capacity
* Mileage
* Maximum power
* Seats
* Selling price

The dataset is stored inside:

data/cardekho_dataset.csv

# How the System Works

1. User enters car details in the web interface
2. Flask application processes the input
3. If the trained model is not found, the system automatically runs `train_model.py`
4. The trained model predicts the selling price
5. The predicted price is displayed on the webpage


# Installation and Setup

### 1. Clone the Repository

git clone https://github.com/DhatriMutyala/used-car-price-predictor.git


### 2. Navigate to Project Folder

cd used-car-price-predictor

### 3. Install Dependencies

pip install -r requirements.txt

### 4. Run the Application

python app.py

### 5. Open in Browser

http://127.0.0.1:5000


# Model Training

If the trained model file does not exist, the system automatically runs:

train_model.py

This script:

• Loads the dataset
• Preprocesses the data
• Trains the machine learning model
• Saves the trained model for prediction

