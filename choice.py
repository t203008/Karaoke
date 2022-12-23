import streamlit as st
import pandas as pd
from PIL import Image
st.title("スマホなしで待ち合わせ　お題")
image1=Image.open("365870_0.jpg")
image2=Image.open("366082_0.jpg")
theme1=pd.read_excel("Meet up without Smartphone.xlsx")
x=st.number_input("選んだ数字", -10000, 10000, 0)
theme1=theme1.sort_values("Random")
if x!=0:
  x=x % len(theme1)
  st.snow()
  st.header(theme1.iloc[x][0])
  
st.image(image1,caption="路線図",use_column_width=True)
st.image(image2,caption="待ち合わせ禁止エリア",use_column_width=True)

