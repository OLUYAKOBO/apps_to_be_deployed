import pandas as pd
import pickle 
import streamlit as st
import numpy as np

st.title(" Loan Eligibility Status Application")

st.write("This App predicts the **Loan Eligibility** status of a customer")

st.header("User Information")

def user_info():
    
    c1,c2 = st.columns(2)
    
    with c1:
        gender = st.selectbox('Please select your gender', (['Male','Female']))
        mar = st.selectbox('Are you married?',(['Yes','No']))
        dep = st.selectbox('How many dependents do you have?', (['0','1','2','3+']))
        edu = st.selectbox('Are you a college graduate', (['Yes','No']))
        self_emp = st.selectbox('Are you self employed?', (['Yes','No']))
        
    with c2:
        app_inc = st.number_input('Please enter your annual income')
        coapp_inc = st.number_input('Please enter your coapplicant annual income')
        loan_amt = st.number_input('Please enter the amount of loan you want to obtain')
        term = st.selectbox('Please enter your term',(['12','36','60','84','120','180','240','300','360','480']))
        cred_hist = st.selectbox('Do you have a credit history', (['Yes','No']))
        
    area = st.selectbox('Which type of area do you live in',(['Urban','Semiurban','Rural']))
    
    
    data = {'Gender' : gender,
            'Married' : mar,
            'Dependents': dep,
            'Education': edu,
            'Self_Employed': self_emp,
            'Applicant_Income': app_inc,
            'Coapplicant_Income' : coapp_inc,
            'Loan_Amount' : loan_amt,
            'Term': term,
            'Credit_History': cred_hist,
            'Area': area
           }
    
    features = pd.DataFrame(data, index = [0])
    return features

df = user_info()

#st.write(df)

yes_no_map = {'No':0,
              'Yes':1}

gender_map = {'Female':0,
              'Male':1}

dep_map = {'0':0,
           '1':1,
           '2':2,
           '3+':3}

area_map = {'Rural':0,
            'Semiurban':1,
            'Urban':2}

term_map = {'12':12,
            '36':36,
            '60':60,
            '84':84,
            '120':120,
            '180':180,
            '240':240,
            '300':300,
            '360':360,
            '480':480}

def encoding():
    df1 = df.copy()
    df1.Gender = df1.Gender.map(gender_map)
    df1.Area = df1.Area.map(area_map)
    df1.Term = df1.Term.map(term_map)
    df1.Dependents = df1.Dependents.map(dep_map)
    y_n = ['Married', 'Education', 'Self_Employed', 'Credit_History']

    for cols in y_n:
        df1[cols] = df1[cols].map(yes_no_map)
    return df1
df1 = encoding()

model = pickle.load(open('loan_eli.pkl','rb'))

if st.button("Click here to know your Loan Eligibility Status"):
    predictions = model.predict(df1)
    #st.write(predictions)
    if predictions == 'N':
        st.write("You are not eligible for a loan")
    else:
        st.write("You are eligible for a loan")
          
            

            
            
            
            
            
            
            
            
            
            
            