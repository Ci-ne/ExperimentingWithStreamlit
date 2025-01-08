import streamlit as st
import torch
import numpy as np


# Title and text
st.title("Experiment 1 With Streamlit")
st.write("A simple streamlit app")

st.slider("Pick a number", 0,100)
