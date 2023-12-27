import streamlit as st

st.title("Area of a circle calculation App")
#Area of circle
from PIL import Image
img=Image.open("formula.jpg")
st.image(img, width=300)

#The Pi (π) is constant at 3.14
Pi=3.14
st.write("Value of Pi is constant at 3.14")

# Note, the area has input radius. But sometimes, we are given the diameter
#Hence, use the radio button to define the two category or format
Input_format=st.radio("Choose input for either radius or diameter", ("radius", "diameter"))


if (Input_format=="radius"):
    radius=st.slider("Select input value in radius", 0, 200)
    st.text("Your selected radius is: {}".format(radius))

    try:
        Areas_Circle=Pi*(radius**2)
    except:
        st.text("Enter some value for the input")
else:
    diameter=st.slider("Select input value in diameter", 0, 400)
    st.text("Your selected diameter is: {}".format(diameter))

    try:
        Areas_Circle=Pi*((diameter/2)**2)
    except:
        st.text("Enter some value for the input")

# check if the button is pressed or not
if(st.button('Calculate Area of circle')):
 
    # print the BMI INDEX
    st.text("Hnece, Area of the Circle is {}.".format(Areas_Circle))
    


