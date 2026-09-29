import streamlit as st
from blood_db import BloodAddUpdateRetrieveDelete

st.title("Delete Record")
id=st.number_input("Enter ID:",min_value=0)
btn=st.button("Delete")
if btn:
    b=BloodAddUpdateRetrieveDelete()
    record=b.delete(id)

    if record:
        st.write("Record Deleted")
    else:
        st.error("No record found")