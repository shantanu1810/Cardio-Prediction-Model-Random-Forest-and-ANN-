import streamlit as st
from PIL import Image

Page_title="Cardio Prediction Model"
icon=Image.open("neuralnetworklogo.jpg")
st.set_page_config(page_title=Page_title,page_icon=icon,layout="wide",initial_sidebar_state="collapsed")

st.markdown(
    """
    <style>
        .st-emotion-cache-pkm19r{
            display:none;
        }
        div.stColumn{
            width:25%;
        }
        div[data-testid="stToolbar"] {
        visibility: hidden;
        height: 0%;
        position: fixed;
        }
        div[data-testid="stDecoration"] {
        visibility: hidden;
        height: 0%;
        position: fixed;
        }
        div[data-testid="stStatusWidget"] {
        visibility: hidden;
        height: 0%;
        position: fixed;
        }
        #MainMenu {
        visibility: hidden;
        height: 0%;
        }
        header {
        visibility: hidden;
        height: 0%;
        }
        footer {
        visibility: hidden;
        height: 0%;
        }
    </style>
    """,
    unsafe_allow_html=True
)
st.title("Cardio Prediction Model")
st.write("A predictive model was built using *Random Forest (RF)* and *Artificial Neural Network (ANN)* techniques to estimate *cardio requirement prediction* based on some common parameters such as weight, Sugar, Cholesterol, Blood Pressure, etc. The dataset was first preprocessed through data cleaning, and data transformation and scale the data to improve model accuracy and reliability. It is binary classification model that predicts only 2 values yes and no.")

st.write("There are total 11 features on which the models are trained.\n\n **Features - Age, Gender, Height, Weight, Glucose(Sugar), Cholesterol, BP Systolic Pressure, BP Diastolic Pressure, Smoking, Alcohol Consume, and Activity**")
st.write("##### The Models trained on the on the dataset. The below 2 models you can try :-")
c0,c1=st.columns(2)
with c0:
    c2,c3=st.columns(2)
    with c2:
        st.write("ANN Model ----")
    with c3:
        st.page_link('pages/prediction_in_NN.py',label=':green-background[Artificial Neural Network Model]')
    st.write("Architecture: The network is composed of layers: an input layer, 3 hidden layers, and an output layer.")
    st.write("Activation Functions: These functions introduce non-linearity into the model, allowing it to learn complex patterns. Common functions include 'relu' (Rectified Linear Unit) and 'sigmoid' which is used in these model.")
    st.write("Epochs and Batch Size: Parameters that control the training process. An epoch is one full pass through the entire training dataset. Batch size is the number of samples processed before the model is updated.**In these model Epoches = 40 and batch size = 32**.")
with c1:
    c2,c3=st.columns(2)
    with c2:
        st.write("Random Forest Model ----")
    with c3:
        #st.page_link('pages/prediction_in_RF.py',label=':green-background[Random Forest Model]')
        pass
    st.write("Ensemble Learning: The core idea is that a large number of relatively uncorrelated models (decision trees) operating as a committee will outperform any of the individual constituent models. In these model they use for classification.")
    st.write("Decision Trees: The foundational element of the random forest is the decision tree, which recursively splits the data based on features to make predictions. **Here 100 decision tree are used**.")
