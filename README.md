![background1](https://github.com/sameerk126/Hepatitis-B-Prediction/assets/81867462/1f622ec0-fcc5-4306-8cce-e2d03d8b0efe)

# Hepatitis B Prediction

This repository contains a machine learning model to predict if a patient has Hepatitis B, based on their lab test reports, with 94% accuracy.

## Usage

The model is served through a Flask web application. To run:
```
python app.py
```
The app will be available at http://localhost:5000. Enter patient lab values like bilirubin, ALT levels etc. to get a prediction.

## Model
The machine learning model is logistic regression, trained on liver patient datasets. The pickled model file is under `/models`. 
Exploratory data analysis and model training notebooks are under `/notebooks`.

## Web App
The Flask app code is in `app.py`. 
HTML templates are under `/templates` and static files like css under `/static`.

## Installation
Requirements:
- Python 3.6+
- Libraries: Numpy, Pandas, Scikit-Learn, Flask (see `requirements.txt`)  

To setup:
1. Clone this repo 
2. Create & activate a **virtualenv**
3. Run `pip install -r requirements.txt`

## Accuracy
The model achieves 94% accuracy in detecting Hepatitis B based on lab tests and liver patient data.

## Contributing
Contributions to improve model accuracy are welcome!
![background1](https://github.com/sameerk126/Hepatitis-B-Prediction/assets/81867462/d590ef47-61b1-41a0-a643-5a800939687f)
