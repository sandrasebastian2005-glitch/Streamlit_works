import streamlit as st
from blood_db import BloodAddUpdateRetrieveDelete

st.write("Read Record")
b=BloodAddUpdateRetrieveDelete()
records=b.list()
if records:
    st.table(records)
else:
    st.error("No records found")