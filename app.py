import numpy as np
import pickle
import streamlit as st

# loading the saved model
with open('notebooks/trained_model.pkl', 'rb') as file:
    data = pickle.load(file)

# print(data)

# creating a function for Prediction

def diabetes_prediction(input_data):
    # changing the input_data to numpy array
    input_data_as_numpy_array = np.asarray(input_data)

    # reshape the array as we are predicting for one instance
    input_data_reshaped = input_data_as_numpy_array.reshape(1,-1)

    prediction = data.predict(input_data_reshaped)
    print(prediction)

    if (prediction[0] == 0):
      return 'The person is not diabetic'
    else:
      return 'The person is diabetic'    
  
def main():
    # giving a title
    st.title('Diabetes Prediction Web App')
    
    # Creating two columns
    col1, col2 = st.columns(2)

    # Column 1 inputs
    with col1:
        Pregnancies = st.number_input('Number of Pregnancies', 
                                      min_value=0, 
                                      step=1, 
                                      help="Enter the number of pregnancies the person has had.")
        
        Glucose = st.number_input('Glucose Level', 
                                  min_value=0.0, 
                                  max_value=500.0, 
                                  step=0.1, 
                                  help="Enter the person's glucose level (mg/dL).")
        
        BloodPressure = st.number_input('Blood Pressure value', 
                                        min_value=0.0, 
                                        max_value=500.0, 
                                        help="Enter the person's blood pressure value (mmHg).")
        
        SkinThickness = st.number_input('Skin Thickness value', 
                                        min_value=0.0, 
                                        max_value=500.0, 
                                        help="Enter the person's skinfold thickness (mm).")

    # Column 2 inputs
    with col2:
        Insulin = st.number_input('Insulin Level', 
                                  min_value=0.0, 
                                  max_value=200.0, 
                                  help="Enter the person's insulin level (IU/mL).")
        
        BMI = st.number_input('BMI value', 
                              min_value=0.0, 
                              max_value=100.0, 
                              help="Enter the person's Body Mass Index (BMI).")
        
        DiabetesPedigreeFunction = st.number_input('Diabetes Pedigree Function value', 
                                                  min_value=0.0, 
                                                  max_value=100.0, 
                                                  help="Enter the person's diabetes pedigree function (a measure of family history of diabetes).")
        
        Age = st.number_input('Age of the Person',
                              min_value=0, 
                              max_value=100)
    
    # code for Prediction
    diagnosis = ''
    
    # creating a button for Prediction
    if st.button('Diabetes Test Result'):
      diagnosis = diabetes_prediction([Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age])
      if 'not diabetic' in diagnosis:
        st.success(diagnosis)  # Green message for not diabetic
      else:
        st.error(diagnosis)  # Red message for diabetic  
    
if __name__ == '__main__':
    main()