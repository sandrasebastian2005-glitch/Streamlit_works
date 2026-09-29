import streamlit as st
from library1_db import BookListCreateRetrieveUpdateDelete

st.title("Welcome to Library App")

b=BookListCreateRetrieveUpdateDelete()
tab1,tab2,tab3,tab4,tab5=st.tabs(['ADD','read','retrieve','update','delete'])
with tab1:
    st.write("ADD")

with tab2:
    st.write('read')
with tab3:
    st.write('retrieve')
with tab4:
    st.write('update')
with tab5:
    st.write('delete')

# other way to do making interfaces for the pages
