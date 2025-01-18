import streamlit as st
import numpy as np
import pickle

# Load the trained model and scaler
try:
    classifier = pickle.load(open('diabetes_model.pkl', 'rb'))
    scaler = pickle.load(open('scaler.pkl', 'rb'))
except Exception as e:
    st.error(f"Error loading model or scaler: {e}")

# Streamlit app
def main():
    st.title("Diabetes Prediction App")
    st.write("Provide the following details to predict the likelihood of diabetes.")

    # Input fields
    pregnancies = st.number_input("Number of Pregnancies", min_value=0, max_value=20, value=0, step=1)
    glucose = st.number_input("Glucose Level", min_value=0, max_value=300, value=100)
    blood_pressure = st.number_input("Blood Pressure (mm Hg)", min_value=0, max_value=200, value=80)
    skin_thickness = st.number_input("Skin Thickness (mm)", min_value=0, max_value=100, value=20)
    insulin = st.number_input("Insulin Level", min_value=0, max_value=1000, value=50)
    bmi = st.number_input("BMI", min_value=0.0, max_value=100.0, value=25.0, step=0.1)
    diabetes_pedigree = st.number_input("Diabetes Pedigree Function", min_value=0.0, max_value=2.5, value=0.5, step=0.01)
    age = st.number_input("Age", min_value=0, max_value=120, value=30)

    # Predict button
    if st.button("Predict"):
        # Prepare the input data
        input_data = np.array([[pregnancies, glucose, blood_pressure, skin_thickness, insulin, bmi, diabetes_pedigree, age]])
        input_data_scaled = scaler.transform(input_data)

        # Make a prediction
        prediction = classifier.predict(input_data_scaled)

        # Display the result
        if prediction[0] == 1:
            st.success("The model predicts that- the person  have diabetes.")
        else:
            st.success("The model predicts that- the person  have Not diabetes.")

if __name__ == "__main__":
    main()
