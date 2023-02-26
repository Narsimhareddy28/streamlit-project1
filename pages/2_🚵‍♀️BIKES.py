import streamlit as st
from PIL import Image
import pandas as pd
from matplotlib import image
import plotly.express as px


image = Image.open("./resources/images/bikr.jpg")
df = pd.read_csv('./resources/dataset/BIKE DETAILS.csv')


st.title("Dashboar-  Bike Data ")
st.image(image, caption='BIKE')
st.dataframe(df)
BIKES = st.selectbox("Select the Brand:", df['name'].unique(),index=1)

col1, col2 = st.columns(2)
fig_1 = px.histogram(df[df['name'] == BIKES], x="selling_price")
col1.plotly_chart(fig_1, use_container_width=True)

fig_2 = px.box(df[df['name'] == BIKES], y="selling_price")
col2.plotly_chart(fig_2, use_container_width=True)

fig_3 = px.bar(df[df['name'] == BIKES], x="year" ,y="selling_price")
col1.plotly_chart(fig_3, use_container_width=True)

fig_4 = px.line(df[df['name'] == BIKES],y="selling_price")
col2.plotly_chart(fig_4, use_container_width=True)
