import streamlit as st
import pandas as pd
theme1=pd.read_csv("Meet up without Smartphone.csv")
x=st.number_input("選んだ数字", 0, 10000, 0)
theme1=theme1.sort_values("Random")
x=x % len(theme1)
st.title("スマホなしで待ち合わせ　お題")
st.write(theme1.iloc[x][0])
