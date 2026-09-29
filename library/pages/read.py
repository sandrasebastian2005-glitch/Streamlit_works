import streamlit as st
from library1_db import BookListCreateRetrieveUpdateDelete
st.title("Read record")

b=BookListCreateRetrieveUpdateDelete()
records=b.list()
print("hai")

# st.write(records)
st.write(" ")
if records:
    st.table(records)
else:
    st.error("No records found")

