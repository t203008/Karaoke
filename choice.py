import streamlit as st
import pandas as pd
theme1=pd.read_csv("Meet up without Smartphone.csv")
st.number_input("選んだ数字", 0, 10000, 0)
st.write(theme1)
