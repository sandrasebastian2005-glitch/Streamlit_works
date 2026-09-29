import streamlit as st
st.title("BMI Calculator")

weight=st.number_input("enter weight in kg")
height=st.number_input("enter height in cm")

btn=st.button("BMI")
if btn:
    bmi=weight/((height/100)**2)
    if bmi<18.5:
        st.info("underweight")
    elif 18.5<=bmi<25:
        st.success("normal")
    elif 25<=bmi<30:
        st.warning("overweight")
    else:
        st.error("obesity")
