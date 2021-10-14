import streamlit as st
import joblib
import pickle
import base64

st.title('Welcome to stroke predication Page!')

#col1, mid, col2 = st.beta_columns([10,100,90])
#with col1:
st.image('shutterstock_735909310.jpg', width=500)



model_rf = joblib.load('heart_stoke_lib.pkl')


activites =['Random forest']
option=st.sidebar.selectbox('Select the model for prediction',activites)
unsafe_allow_html=True

gender =st.selectbox('Select the gender',('Male','Female'))

if gender =='Male':
	gender=0
else:
	gender=1

ever_married = st.selectbox('Are you married',('Yes','No'))
if ever_married == 'Yes':
	ever_married=1
else:
	ever_married=0

work_type = st.radio('select the work type',('Private','Self-employed','Govt job','children','Never worked'))
if work_type=='Never worked':
	work_type=0
elif work_type=='children':
	work_type=1
elif work_type=='Self-employed':
	work_type=2
elif work_type=='Private':
	work_type=3
else:
	work_type=4

Residence_type=st.selectbox('where do you live',('Urban','Rural'))

if	Residence_type=='Urban':
	Residence_type=0
else:
	Residence_type=1

smoking_status = st.radio("How frequent you smoke ?",('FormerlySmoked','NeverSmoked','Smokes','Unknown'))

if smoking_status == 'Unknown':
	smoking_status=0
elif smoking_status == 'NeverSmoked':
	smoking_status=1
elif smoking_status == 'FormerlySmoked':
	smoking_status=2
else:	
	smoking_status=3

age = st.slider('Enter your age',0,100)

hypertension=st.radio('Do you hacv hypertension?',('Yes','No'))
if hypertension== 'Yes':
	hypertension=1
else:
	hypertension=0

heart_disease =st.radio('Do you have Heart Disease?',('Yes','No'))
if heart_disease== 'Yes':
	heart_disease=1
else:
	heart_disease=0

#avg_glucose_level =st.slider('Enter your Average Glucose Level',0,100)
avg_glucose_level=st.number_input('Glucose Level:',key="name") 

#if not avg_glucose_level:
#  st.warning("Please Enter Glucose Level")


#bmi =st.slider('Enter the bmi',0,500)
bmi =st.number_input('BMI Level:',key="value")##

#if not bmi:
#  st.warning("Please Enter BMI Level")

inputs =[[gender,ever_married,work_type,Residence_type,
smoking_status,age,
hypertension,
heart_disease,
avg_glucose_level,bmi]]

print(inputs)
if option== 'Random forest':
	model_rf.predict(inputs)

if st.button('Predict'):
	if model_rf.predict(inputs)[0]==0:
		st.success('There is possibility that you may get stroke .Kindly visit nearest hospital for checkup :(')
	else:
		st.success('Your health is fit and fine!!')