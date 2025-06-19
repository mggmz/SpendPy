import streamlit as st
import pandas as pd 
import plotly.express as px
import json 
import os


st.set_page_config(page_title="Personal Finance App", page_icon=":money_with_wings:" , layout="wide")

def load_transactions(file):

    try: 
        df = pd.read_csv(file)
def main():
    st.title("Personal Finance App")

    upload_file = st.file_uploader("Upload your transactions file (CSV)", type=["csv"])

    if upload_file is not None:
        df = load_transactions(upload_file)


main()