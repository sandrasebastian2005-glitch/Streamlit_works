import streamlit as st
from library1_db import BookListCreateRetrieveUpdateDelete
st.title("Delete record")


id=st.number_input("Enter ID:",min_value=0)
btn=st.button("Delete")
if btn:
    b=BookListCreateRetrieveUpdateDelete()
    record=b.delete(id)

    if record:
        st.write("Record Deleted")
    else:
        st.error("No record found")