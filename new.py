import streamlit as st
# text_input
num1=st.number_input("enter number",min_value = 0)
num2=st.number_input("enter number")# min value in decimal

st.write(num1)
st.write(num2)

name=st.text_input("enter name")
st.write(name)
date=st.date_input("enter date:")
st.write(date)
btn=st.button("click")
st.write(btn)