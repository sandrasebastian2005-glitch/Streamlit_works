import streamlit as st
from blood_db import BloodAddUpdateRetrieveDelete
st.title("Retrieve Record")

st.write(" ")
id=st.number_input("Enter ID:",min_value=0)
btn=st.button("Retrieve")
if btn:
    b=BloodAddUpdateRetrieveDelete()
    record=b.retrieve(id)
    if record:
        st.write(" ")
        st.write("Name:",record[1])
        st.write("BloodGroup:",record[2])
        st.write("Phone:",record[3])
        st.write("City:",record[4])
        st.write("Last Donation",record[5])
    else:
        st.error("No Record Found")
        
