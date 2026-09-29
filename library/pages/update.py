import streamlit as st
from library1_db import BookListCreateRetrieveUpdateDelete
st.title("Update record")

id=st.number_input("Enter Id:",min_value=0)
title=st.text_input("Title:")
author=st.text_input("Author:")
language=st.selectbox("Language:",["Malayalam","English","Hindi"])
price=st.number_input("Price:",min_value=0)
pages=st.number_input("Pages:",min_value=0)


btn=st.button("Update")
if btn:
    b=BookListCreateRetrieveUpdateDelete()
    records=b.update(id,title,author,language,price,pages)
    if records:
        st.success("updated successfully")
    else:
        st.error("No record found")

