#### Importing the streamlit module
import streamlit as st
# 1. Defining a title
st.title("My Basic Streamlit App Deployed!!!")
#2. Header and subheader
st.header("Header is: A streamlit app")
st.subheader("Sub-Header is: App deployed")
#3. Text
st.text("Writing a text: Building a basic app using the streamlit model deployment framework")
#4. Markdown
st.markdown("For a markdown")
#5. 5.  Success, Info, Warning, Error, Exception:
st.success("Success")
st.info("Information")
st.warning("Warning")
st.error("Error")
exp=ZeroDivisionError("Wrongly dividing a nmber by zero")
st.exception(exp)
#6.Write
st.write("Using the write to write text. can also display code")
st.write(range(30))
#7. Display Images
# import Image from pillow to open images
from PIL import Image
img=Image.open("OIP.jpg")
st.image(img, width=200)

#8. checkbox
# check if the checkbox is checked
# title of the checkbox is 'Show/Hide'
if st.checkbox("Show/Hide"):

    # display the text if the checkbox returns True value
    st.text("the value of the check box when checked")

#9. Radio

# radio button
# first argument is the title of the radio button
# second argument is the options for the radio button
status = st.radio("Select Gender: ", ('Male', 'Female'))
 
# conditional statement to print 
# Male if male is selected else print female
# show the result using the success function
if (status == 'Male'):
    st.success("Male")
else:
    st.success("Female")
st.write("Your Gender is:", status)

#10. Selection Box
# first argument takes the titleof the selectionbox
# second argument takes options
hob=st.selectbox("Hobby:", ["Footbal", "Reading", "Pet", "Singing"])
# print the selected hobby
st.write("Your Hobby is: ", hob)

#11. Multi-Selectbox:
# first argument takes the box title
# second argument takes the options to show
Hobbies=st.multiselect("Hobbies", ["Footbal", "Reading", "Pet", "Singing"])
#st.write("Your hobbies:", len(Hobbies), Hobbies)
st.write("Selected Number:", len(Hobbies), "Hobbies")

#12. Button
# Create a simple button that does nothing
st.button("Click me for no reason")
 
# Create a button, that when clicked, shows a text
if(st.button("About")):
    st.text("Welcome To GeeksForGeeks!!!")

#13. Text input
# save the input text in the variable 'name'
# first argument shows the title of the text input box
# second argument displays a default text inside the text input area
name = st.text_input("Enter Your name", "Type Here ...")
 
# display the name when the submit button is clicked
# .title() is used to get the input text string
if(st.button('Submit')):
    result = name.title()
    st.success(result)
#Alternatively, yoy may add:
    st.write("Your first name is:", result)

#14. Slider
# first argument takes the title of the slider
# second argument takes the starting of the slider
# last argument takes the end number
level=st.slider("Select level:", 1, 20)


# print the level
# format() is used to print value 
# of a variable at a specific position
st.text("Selected level: {}".format(level))
#Alternatively,
st.write("Selected level is:- ", format(level) )

