import streamlit as st

@st.cache(allow_output_mutation=True)
def cache():
    dict = {'is_done': {'Home'}}
    return dict