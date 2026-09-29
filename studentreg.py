import streamlit as st
from datetime import date
st.title("Student Registration Form")

name=st.text_input("Name:")
age=st.number_input("Age:",min_value = 0)
dob=st.date_input("DOB",min_value=date(1990,1,1),max_value=date.today(),value=date(2006,1,1))
email=st.text_input("Email")
gender=st.radio("Gender",["Male","Female"])
course=st.selectbox("Courses",["Python","dotnet","testing"])
btn=st.button("Submit")
if btn:
    st.write("Name:",name)
    st.write("Age:",age)
    st.write("DOB:",dob)
    st.write("Email",email)
    st.write("Gender",gender)
    st.write("Course",course)
