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
    st.date_input("Data de Nascimento")
    tel = st.text_input("Contato de telefone")
    cat = st.selectbox("Categoria de chegada (Sub-...)",options=[6,7,8,9,10,11,12,13,14,15,17,20])
    pos = st.selectbox("Posição",options=['GOL','LD','ZAG','LE','VOL','MEI','EXT','ATA'])
    
  with col2:
    st.subheader("Origem do jogador")
    
    indicador = st.text_input("Indicador (Pessoa de dentro do clube)")
    visu = st.radio("In loco / Contato externo",options=["In loco","Contato externo"])
    if visu == "Contato externo":
      contato = st.text_input("Contato externo")
    else:
      contato = "-"
    origem = st.text_input("Origem do jogador (Último clube / escolinha / projeto)")
    
  st.subheader("Histórico no clube")
  
  monit = st.radio("Monitorado?",options=['Sim','Não'])
  
  if monit == 'Sim':
    data1_monit = st.date_input('Início do monitoramento')
    data2_monit = st.date_input('Fim do monitoramento')
  else:
    data1_monit = ""
    data2_monit = ""
    
  aval = st.radio("Avaliação?",options=['Sim','Não'])
  
  if aval == 'Sim':
    data1_aval = st.date_input('Início da avaliação')
    data2_aval = st.date_input('Fim da avaliação')
    
    aprov = st.radio("Aprovado?",options=['Sim','Não'])
    if aprov == 'Sim':
      data_aprov = st.date_input('Data da aprovação')
     
      situ_text = st.text("Situação: ATIVO")
      
      deslig = st.select("Desligado?",options=['Sim','Não'])
      
      if deslig == 'Sim':
        situ_text.text('Situação: DESLIGADO')
      
    
    
  else:
    data1_aval = ""
    data2_aval = ""
    
  
    
    
    
  
    
    
   
