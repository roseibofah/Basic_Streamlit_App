######Mini Project:
#Let us recollect everything that we learn above and create a BMI Calculator web app.

#The formula of BMI Index when weight is in Kgs and height is in meters is:

##################bmi = weight/height^2        

#Python3
# import the streamlit library
import streamlit as st
 
# give a title to our app
st.title("Welcome to BMI Calculator - 'By Richard O. Bofah'")
 
# TAKE WEIGHT INPUT in kgs
#weight = st.number_input("Enter your weight (in kgs)")
#Alternatively, 
weight=st.slider("Select Your weight (in kgs)", 0, 1000)
st.text("Your selected weight is: {}".format(weight))

 
# TAKE HEIGHT INPUT
# radio button to choose height format
status = st.radio('Select your preferred height format: ',
                  ('cms', 'meters', 'feet'))
 
# compare status value
if(status == 'cms'):
    # take height input in centimeters
    #height = st.number_input('Centimeters')
    height=st.slider("Select height in cms", 0, 500)
    st.text("Your selected height is: {}".format(height))

    try:
        bmi = weight / ((height/100)**2)
    except:
        st.text("Enter some value of height")
 
elif(status == 'meters'):
    # take height input in meters
    #height = st.number_input('Meters')
    height=st.slider("Select height in meters", 0, 5)
    st.text("Your selected height is: {}".format(height))
 
    try:
        bmi = weight / (height ** 2)
    except:
        st.text("Enter some value of height")
 
else:
    # take height input in feet
    #height = st.number_input('Feet')
    height=st.slider("Select height in feet", 0, 15)
    st.text("Your selected height is: {}".format(height))
 
    # 1 meter = 3.28
    try:
        bmi = weight / (((height/3.28))**2)
    except:
        st.text("Enter some value of height")
 
# check if the button is pressed or not
if(st.button('Calculate BMI')):
 
    # print the BMI INDEX
    st.text("Your BMI Index is {}.".format(bmi))
 
    # give the interpretation of BMI index
    if(bmi < 16):
        st.error("You are Extremely Underweight")
    elif(bmi >= 16 and bmi < 18.5):
        st.warning("You are Underweight")
    elif(bmi >= 18.5 and bmi < 25):
        st.success("Healthy")
    elif(bmi >= 25 and bmi < 30):
        st.warning("Overweight")
    elif(bmi >= 30):
        st.error("Extremely Overweight/Obese")

