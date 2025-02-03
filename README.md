# Diabetic-Patients-Identification-System

<h2>Overview</h2>
<p>The <strong>Diabetic Patients Identification System</strong> is a machine learning-based project designed to predict the likelihood of an individual having diabetes. This system utilizes diagnostic features such as glucose levels, age, blood pressure, and other relevant health indicators to make accurate predictions. The model has been trained using the <strong>Support Vector Classifier (SVC)</strong> algorithm and is deployed as a web application using <strong>Streamlit</strong>.</p>

<h2>Web Application Preview</h2>
<img src="Diabetics prediction system.png" alt="Diabetic Patients Identification System Web App" width="800">

<h2>Dataset</h2>
<p>The dataset used in this project originates from the <strong>National Institute of Diabetes and Digestive and Kidney Diseases</strong>. The objective is to predict diabetes based on diagnostic measurements. The dataset includes only female patients of <strong>Pima Indian heritage</strong>, aged at least 21 years.</p>

<h3>Features</h3>
<ul>
    <li><strong>Pregnancies</strong>: Number of times pregnant</li>
    <li><strong>Glucose</strong>: Plasma glucose concentration after 2 hours in an oral glucose tolerance test</li>
    <li><strong>BloodPressure</strong>: Diastolic blood pressure (mm Hg)</li>
    <li><strong>SkinThickness</strong>: Triceps skin fold thickness (mm)</li>
    <li><strong>Insulin</strong>: 2-Hour serum insulin (mu U/ml)</li>
    <li><strong>BMI</strong>: Body mass index (weight in kg/(height in m)^2)</li>
    <li><strong>DiabetesPedigreeFunction</strong>: A measure of diabetes history in family members</li>
    <li><strong>Age</strong>: Age of the patient (years)</li>
    <li><strong>Outcome</strong>: Class variable (0 = No diabetes, 1 = Diabetes)</li>
</ul>

<h2>Model Training</h2>
<ul>
    <li>The <strong>Support Vector Classifier (SVC)</strong> architecture was used to train the model.</li>
    <li>The dataset was split into <strong>training</strong> and <strong>testing</strong> sets.</li>
    <li>The model was evaluated based on <strong>accuracy</strong> for both training and testing sets.</li>
</ul>

<h2>Web Application</h2>
<p>A <strong>Streamlit</strong> web application was developed to allow users to input their health data and receive a diabetes prediction.</p>

<h3>Technologies Used</h3>
<ul>
    <li><strong>Python</strong> (for model training and development)</li>
    <li><strong>Scikit-Learn</strong> (for implementing the SVC model)</li>
    <li><strong>Pandas & NumPy</strong> (for data preprocessing)</li>
    <li><strong>Streamlit</strong> (for creating the web application)</li>
    <li><strong>Pickle</strong> (for saving and loading the trained model)</li>
</ul>
<h2>Model Deployment</h2>
<p>The trained <strong>SVC model</strong> was saved using the <strong>pickle</strong> library and loaded in the web application to provide real-time predictions.</p>

<h2>Model Evaluation</h2>
<p>The performance of the model was assessed using <strong>accuracy metrics</strong> for both the training and testing datasets.</p>

<h2>Conclusion</h2>
<p>The <strong>Diabetic Patients Identification System</strong> is an efficient and reliable tool for predicting diabetes using machine learning. By leveraging a robust dataset and the power of the Support Vector Classifier (SVC), this project provides an easy-to-use web application for medical professionals and individuals alike. Future enhancements will focus on improving model accuracy and expanding the dataset for more comprehensive predictions.</p>
