import streamlit as st
from library1_db import BookListCreateRetrieveUpdateDelete
st.title("Retrieve record")

st.write(" ")
id=st.number_input("Enter id:",min_value=0)
btn=st.button("Retrieve")
if btn:
    b=BookListCreateRetrieveUpdateDelete()
    records=b.retrieve(id)
    if records:
        # st.table(records)
        st.write(" ")
        st.write("Title:",records[1])
        st.write("Author:",records[2])
        st.write("Language:",records[3])
        st.write("Price:",records[4])
        st.write("Page:",records[5])
         # bcs the record id in uple sequence
    else:
        st.write("No record found")