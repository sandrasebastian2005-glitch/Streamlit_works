import streamlit as st
from datetime import date
from blood_db import BloodAddUpdateRetrieveDelete

st.title("Update Record")

id=st.number_input("Enter ID:",min_value=0)
name=st.text_input("Enter the Donor Name:")
bloodgroup=st.text_input("Enter the Blood Group:")
phone=st.text_input("Enter phone:")
city=st.text_input("Enter City:")
last_donation=st.date_input("Enter Last Donation Date:",min_value=date(1990,1,1),max_value=date.today(),value=date(2006,1,1))

btn=st.button("Update")
if btn:
    b=BloodAddUpdateRetrieveDelete()
    record=b.update(id,name,bloodgroup,phone,city,last_donation)
    if record:
        st.success("updated successfully")
    else:
        st.error("No record found")        
        