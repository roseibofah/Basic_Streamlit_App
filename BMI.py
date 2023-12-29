######Mini Project:
#Let us recollect everything that we learn above and create a BMI Calculator web app.

#The formula of BMI Index when weight is in Kgs and height is in meters is:

##################bmi = weight/height^2        

#Python3
# import the streamlit library
import streamlit as st
 
# give a title to our app
st.title("Know Your Body Mass Index - BMI")
st.subheader("By Dr. Richard O. Bofah -- Economist and Data Scientist")

st.text("All you need: Wight in kg & Height") 
# TAKE WEIGHT INPUT in kgs
weight = st.number_input("Enter your weight (in kgs)")

 
# TAKE HEIGHT INPUT
# radio button to choose height format
status = st.radio('Select your height in the format of your choice: ',
                  ('cms', 'meters', 'feet'))
 
# compare status value
if(status == 'cms'):
    # take height input in centimeters
    height = st.number_input('Centimeters')
 
    try:
        bmi = weight / ((height/100)**2)
    except:
        st.text("Enter some value of height")
 
elif(status == 'meters'):
    # take height input in meters
    height = st.number_input('Meters')
 
    try:
        bmi = weight / (height ** 2)
    except:
        st.text("Enter some value of height")
 
else:
    # take height input in feet
    height = st.number_input('Feet')
 
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
        st.warning("Pre-obesity/Overweight")
    elif(bmi >= 30):
        st.error("Obese")
    st.write("See WHO website for BMI and Health Tips: https://www.who.int/europe/news-room/fact-sheets/item/a-healthy-lifestyle---who-recommendations")

