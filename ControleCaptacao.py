import streamlit as st
import pandas as pd
import numpy as np

base = pd.read_csv('Planilha Geral - Captação TOCA I1.csv',sep=';',decimal=',')
st.write(base)

st.subheader("O que deseja fazer?")

acao = st.radio("Selecione o que deseja fazer:",options = ['Adicionar atleta','Ver histórico de atleta','Editar atleta'])

if acao == 'Adicionar atleta':
  col1, col2 = st.columns(2)
  
  with col1:
    st.subheader("Informações pessoais")
    
    nome = st.text_input("Nome")
    datanasc = st.date_input("Data de nascimento")
    tel = st.text_input("Contato de telefone")
    cat = st.radio("Categoria de chegada (Sub-...)",options=[6,7,8,9,10,11,12,13,14,15,17,20])
    pos = st.radio("Posição",options=['GOL','LD','ZAG','LE','VOL','MEI','EXT','ATA'])
    
  with col2:
    st.subheader("Origem do jogador")
    
    indicador = st.text_input("Indicador (Pessoa de dentro do clube)")
    visu = st.radio("In loco / Contato externo",options=["In loco","Contato externo"])
    if visu == "Contato externo":
      contato = st.text_input("Contato externo")
    else:
      contato = "-"
    origem = st.text_input("Origem do jogador (Último clube / escolinha / projeto)")
   
