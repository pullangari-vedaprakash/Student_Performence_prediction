import streamlit as st
from src.pipeline.predict_pipeline import CustomData, PredictPipeline

st.set_page_config(page_title="Student Performance Predictor")

st.title(" Student Performance Prediction")

st.write("Enter student details below")

gender = st.selectbox(
    "Gender",
    ["male", "female"]
)

race_ethnicity = st.selectbox(
    "Race/Ethnicity",
    ["group A", "group B", "group C", "group D", "group E"]
)

parental_level_of_education = st.selectbox(
    "Parental Level of Education",
    [
        "associate's degree",
        "bachelor's degree",
        "high school",
        "master's degree",
        "some college",
        "some high school"
    ]
)

lunch = st.selectbox(
    "Lunch",
    ["standard", "free/reduced"]
)

test_preparation_course = st.selectbox(
    "Test Preparation Course",
    ["none", "completed"]
)

reading_score = st.slider(
    "Reading Score",
    0,
    100,
    50
)

writing_score = st.slider(
    "Writing Score",
    0,
    100,
    50
)

if st.button("Predict Math Score"):

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

    predict_pipeline = PredictPipeline()

    result = predict_pipeline.predict(pred_df)

    st.success(f"Predicted Math Score: {result[0]:.2f}")