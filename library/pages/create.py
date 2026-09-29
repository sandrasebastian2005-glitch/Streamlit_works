import streamlit as st
from library1_db import BookListCreateRetrieveUpdateDelete
st.title("Add new record")

title=st.text_input("Title:")
author=st.text_input("Author:")
language=st.selectbox("Language:",["Malayalam","English","Hindi"])
price=st.number_input("Price:",min_value=0)
pages=st.number_input("Pages:",min_value=0)
btn=st.button("Add")

if btn:
    b=BookListCreateRetrieveUpdateDelete()
    b.create(title,author,language,price,pages)
    st.success("Create record Successfully")
    # st.write("Title:",title)
    # st.write("Author:",author)
    # st.write("Price:",price)
    # st.write("Language:",language)
    # st.write("Pages:",pages)
    
        
        
        
        
        

