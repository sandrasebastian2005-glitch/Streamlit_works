import streamlit as st
from blood_db import BloodAddUpdateRetrieveDelete
from datetime import date
st.title("Add new record")

name=st.text_input("Enter the Donor Name:")
bloodgroup=st.text_input("Enter the Blood Group:")
phone=st.text_input("Enter phone:")
city=st.text_input("Enter City:")
last_donation=st.date_input("Enter Last Donation Date:",min_value=date(1990,1,1),max_value=date.today(),value=date(2006,1,1))
btn=st.button("Add")

if btn:
    b=BloodAddUpdateRetrieveDelete()
    b.add(name,bloodgroup,phone,city,last_donation)
    st.success("Added Successfully")
    

