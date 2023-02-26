import streamlit as st
from PIL import Image
import pandas as pd
from matplotlib import image
import plotly.express as px


image = Image.open("./resources/images/car.jpg")
df = pd.read_csv('./resources/dataset/USA_cars_datasets.csv')


st.title("Dashboar- US Cars Data ")
st.image(image, caption='CAR')
st.dataframe(df)
CARS = st.selectbox("Select the Brand:", df['brand'].unique(),index=1)

col1, col2 = st.columns(2)
fig_1 = px.histogram(df[df['brand'] == CARS], x="price")
col1.plotly_chart(fig_1, use_container_width=True)

fig_2 = px.box(df[df['brand'] == CARS], y="price")
col2.plotly_chart(fig_2, use_container_width=True)

fig_3 = px.bar(df[df['brand'] == CARS], x="year" ,y="price")
col1.plotly_chart(fig_3, use_container_width=True)

fig_4 = px.line(df[df['brand'] == CARS],y="price")
col2.plotly_chart(fig_4, use_container_width=True)
