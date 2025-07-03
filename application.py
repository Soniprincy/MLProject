# from flask import Flask, request, render_template
# import numpy as np
# import pandas as pd

# from sklearn.preprocessing import StandardScaler
# import sys
# import os
# sys.path.append(os.path.abspath(os.path.dirname(__file__)))
# from src.pipeline.predict_pipeline import PredictPipeline, CustomData

# application = Flask(__name__)

# app = application

# ## route for a home page

# @app.route('/')
# def index():
#     return render_template('index.html')

# @app.route('/predictdata',methods=['GET','POST'])
# def predict_datapoint():
#     if request.method=='GET':
#         return render_template('home.html')
#     else:
#         data=CustomData(
#             gender=request.form.get('gender'),
#             race_ethnicity=request.form.get('ethnicity'),
#             parental_level_of_education=request.form.get('parental_level_of_education'),
#             lunch=request.form.get('lunch'),
#             test_preparation_course=request.form.get('test_preparation_course'),
#             reading_score=float(request.form.get('writing_score')),
#             writing_score=float(request.form.get('reading_score'))

#         )
#         pred_df=data.get_data_as_data_frame()
#         print(pred_df)
#         print("Before Prediction")

#         predict_pipeline=PredictPipeline()
#         print("Mid Prediction")
#         results=predict_pipeline.predict(pred_df)
#         print("after Prediction")
#         return render_template('home.html',results=results[0])
    

# if __name__=="__main__":
#     app.run(host="0.0.0.0")     

import streamlit as st
import pandas as pd
from src.pipeline.predict_pipeline import PredictPipeline, CustomData

st.set_page_config(page_title="Exam Score Predictor", layout="centered")

st.title("🎓 Student Exam Performance Prediction")

# Sidebar or Input Fields
st.header("Enter Student Information")

gender = st.selectbox("Gender", ["male", "female"])
race_ethnicity = st.selectbox("Race/Ethnicity", ["group A", "group B", "group C", "group D", "group E"])
parental_level_of_education = st.selectbox("Parental Level of Education", [
    "some high school", "high school", "some college", 
    "associate's degree", "bachelor's degree", "master's degree"
])
lunch = st.selectbox("Lunch Type", ["standard", "free/reduced"])
test_preparation_course = st.selectbox("Test Preparation Course", ["none", "completed"])

reading_score = st.number_input("Reading Score (0–100)", min_value=0.0, max_value=100.0, value=70.0)
writing_score = st.number_input("Writing Score (0–100)", min_value=0.0, max_value=100.0, value=70.0)

# Predict Button
if st.button("Predict Math Score"):
    try:
        data = CustomData(
            gender=gender,
            race_ethnicity=race_ethnicity,
            parental_level_of_education=parental_level_of_education,
            lunch=lunch,
            test_preparation_course=test_preparation_course,
            reading_score=reading_score,
            writing_score=writing_score
        )
        pred_df = data.get_data_as_data_frame()
        pipeline = PredictPipeline()
        result = pipeline.predict(pred_df)
        
        st.success(f"✅ Predicted Math Score: {result[0]:.2f}")
    
    except Exception as e:
        st.error(f"❌ Error: {str(e)}")

