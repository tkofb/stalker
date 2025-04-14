import streamlit as st
import pandas as pd

st.title("Portfolio Analyzer")

uploaded_file = st.file_uploader("Upload files", type='csv', label_visibility="collapsed")

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    st.write(df)




