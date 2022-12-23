import streamlit as st
import pandas as pd
from PIL import Image
st.title("スマホなしで待ち合わせ　お題")
st.write(365870_0.jpg)
theme1=pd.read_csv("Meet up without Smartphone.csv")
x=st.number_input("選んだ数字", -10000, 10000, 0)
theme1=theme1.sort_values("Random")
if x!=0:
  x=x % len(theme1)
  st.snow()
  st.write(theme1.iloc[x][0])
