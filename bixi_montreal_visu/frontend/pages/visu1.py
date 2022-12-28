import streamlit as st
import pandas as pd


df = pd.read_csv('data/dropoff_station.csv')

st.map(df)