import streamlit as st
import pandas as pd
import numpy as np

base = pd.read_csv('Planilha Geral - Captação Toca I1.csv',sep=';',decimal=',')

st.write(base)
