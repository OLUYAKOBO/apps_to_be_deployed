import streamlit as st
import pandas as pd
import numpy as np
import pickle
#from sklearn.ensemble import RandomForestClassifier
#import os
st.title("Diabetes Prediction Application")
st.write("""

#### This application predicts whether an individual is suffering from diabetes or not """)

st.header("User Input Parameters")

def user_input():
    c1,c2,c3 = st.columns(3)
    
    with c1:
        age = st.number_input('Age', 0, 100, 40)
        gender = st.selectbox('Gender', ('Male','Female'))
        polyuria = st.selectbox('Polyuria', ('Yes','No'))
        polydipsia = st.selectbox('Polydipsia', ('Yes','No'))
        sudden_weight_loss = st.selectbox('Sudden weight loss', ('Yes','No'))
        
    with c2:
        
        weakness = st.selectbox('Weakness', ('Yes','No'))
        polyphagia = st.selectbox('Polyphagia', ('Yes','No'))
        genital_thrush = st.selectbox('Genital thrush', ('Yes','No'))
        visual_blurring = st.selectbox('Visual blurring', ('Yes','No'))
        Itching = st.selectbox('Itching', ('Yes','No'))
        
    with c3:
        
        Irritability = st.selectbox('Irritability', ('Yes','No'))
        delayed_healing = st.selectbox('Delayed healing', ('Yes','No'))
        partial_paresis = st.selectbox('Partial paresis', ('Yes','No'))
        muscle_stiffness = st.selectbox('Muscle stiffness', ('Yes','No'))
        Alopecia = st.selectbox('Alopecia', ('Yes','No'))
        Obesity = st.selectbox('Obesity', ('Yes','No'))
    
    data = {'Age' : age,
            'Gender'  : gender,
            'Polyuria' : polyuria,
            'Polydipsia' : polydipsia,
            'sudden weight loss' : sudden_weight_loss,
            'weakness'  : weakness,
            'Polyphagia' : polyphagia,
            'Genital thrush' : genital_thrush,
            'visual blurring' : visual_blurring,
            'Itching'  : Itching,
            'Irritability' : Irritability,
            'delayed healing' : delayed_healing,
            'partial paresis' : partial_paresis,
            'muscle stiffness'  : muscle_stiffness,
            'Alopecia' : Alopecia,
            'Obesity' : Obesity
           }
    features  = pd.DataFrame(data, index= [0])
    return features

df1 = user_input()
#st.subheader('User Input Parameters')
#st.write(df1)


df1.Gender = df1.Gender.map({'Female':0,
                          'Male':1})
df1.Polyuria = df1.Polyuria.map({'No': 0,
                                'Yes': 1})
df1.Polydipsia = df1.Polydipsia.map({'No': 0,
                                'Yes': 1})
df1['sudden weight loss'] = df1['sudden weight loss'].map({'No': 0,
                                'Yes': 1})
df1.weakness = df1.weakness.map({'No': 0,
                                'Yes': 1})
df1.Polyphagia = df1.Polyphagia.map({'No': 0,
                                'Yes': 1})
df1['Genital thrush'] = df1['Genital thrush'].map({'No': 0,
                                'Yes': 1})
df1['visual blurring'] = df1['visual blurring'].map({'No': 0,
                                'Yes': 1})
df1.Itching = df1.Itching.map({'No': 0,
                                'Yes': 1})
df1.Irritability = df1.Irritability.map({'No': 0,
                                'Yes': 1})
df1['delayed healing'] = df1['delayed healing'].map({'No': 0,
                                'Yes': 1})
df1['partial paresis'] = df1['partial paresis'].map({'No': 0,
                                'Yes': 1})
df1['muscle stiffness'] = df1['muscle stiffness'].map({'No': 0,
                                'Yes': 1})
df1.Alopecia = df1.Alopecia.map({'No': 0,
                                'Yes': 1})
df1.Obesity = df1.Obesity.map({'No': 0,
                                'Yes': 1})


#st.write(df1)

load_clf = pickle.load(open('diabetes_clf.pkl', 'rb'))

prediction = load_clf.predict(df1)
prediction_proba = load_clf.predict_proba(df1)


st.subheader('Prediction')
if st.button('Click here to get your diagnosis'):
    if predictions == '0':
        st.write("Your diabetes condition is Negative")
    st.write("Your diabetes condition is Positive")
    

#st.subheader('Prediction Probability')
#st.write(prediction_proba)
    
    
    
    

                
    
