import streamlit as st
# text_input
num1=st.number_input("enter number 1",min_value = 0)
num2=st.number_input("enter number 2",min_value = 0)
btn=st.button("multiply")
if btn:
    st.write("multiply is ",num1*num2)
