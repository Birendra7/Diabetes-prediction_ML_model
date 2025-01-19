# Diabetes Prediction App

This is a web-based application that predicts the likelihood of diabetes in an individual based on various health parameters. The app is built using Streamlit and a pre-trained machine learning model.

## Features

- **User Input**: The app allows users to input several health metrics including:

  - Number of Pregnancies
  - Glucose Level
  - Blood Pressure
  - Skin Thickness
  - Insulin Level
  - BMI (Body Mass Index)
  - Diabetes Pedigree Function
  - Age

- **Prediction**: After providing the necessary details, the app predicts whether the individual is likely to have diabetes.

## Requirements

- Python 3.7 or higher
- Streamlit
- NumPy
- Scikit-learn
- Pickle files for the trained model (`diabetes_model.pkl`) and scaler (`scaler.pkl`)

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/Birendra7/Diabetes-prediction_ML_model
   cd Diabetes-prediction_ML_model
   ```

2. Install the required packages:

   ```bash
   pip install -r requirements.txt
   ```

3. Ensure the pre-trained model and scaler files (`diabetes_model.pkl` and `scaler.pkl`) are placed in the same directory as `app.py`.

## Running the App

To run the Streamlit app, execute the following command:

```bash
streamlit run app.py
```

This will start a local web server and provide a URL to access the app in your browser.

## Usage

1. Open the provided URL in your browser.
2. Input the requested health parameters in the provided fields.
3. Click the "Predict" button to see the prediction result.

## Note

- The app is for informational purposes only and should not be used as a substitute for professional medical advice, diagnosis, or treatment.

## License

This project is licensed under the MIT License. See the LICENSE file for more details.

## Acknowledgments

- The model used in this app is trained on publicly available datasets.
- Special thanks to the contributors and the Streamlit community for their support.



