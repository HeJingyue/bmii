import streamlit as st
st.title("Welcome to Kat's BMI APP!")

weight = st.number_input("Enter your weight in kgs:")
status = st.radio("Select your height format:",("cms","meters","feet"))

if(status == "cms"):
    height = st.number_input("Cemtimeters")
    try:
        bmi = weight/((height/100)**2)
    except:
        st.text("something went wrong")
elif(status == "meters"):
    height = st.number_input("meters")
    try:
        bmi = weight/((height/100)**2)
    except:
        print("Enter some value of height")
    try:
        bmi = weight/((height/100)**2)
    except:
        st.text("something went wrong")

else:
    height = st.number_input("feet")
    try:
        bmi = weight/((height/100)**2)
    except:
        st.text("Enter some value of height")
if(st.button("Calculate BMI")):
    st.text("Your BMI is {} :".format(bmi))
    if(bmi<16):
         st.error("You are extremely underweight. You better live your grandma")
    elif(bmi>=16):
         st.error ("You are extremely underweight.")
    elif(bmi>=16):
         st.error("You are extremely underweight.")
    elif(bmi>=18.5):
         st.error("You are healthy.")
    elif(bmi>=25):
         st.error("You are extremely underweight.")
    elif(bmi>=30):
         st.error("You are extremely underweight.")
 