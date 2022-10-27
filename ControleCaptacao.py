import streamlit as st
import pandas as pd
import numpy as np

base = pd.read_csv('Planilha Geral - Captação TOCA I1.csv',sep=';',decimal=',').reset_index(drop=True)
base = base.rename(columns={'Posição (GOL, ZG, LD, LE, VOL, MEI, ATA, EXT)':'Posição','Nome Completo':'Nome'})
st.write(base)

st.subheader("O que deseja fazer?")

acao = st.radio("Selecione o que deseja fazer:",options = ['Adicionar atleta','Editar atleta','Ver atleta'])

if acao == 'Adicionar atleta':
  col1, col2, col3 = st.columns(3)
  
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
  
  with col3:
    st.subheader("Histórico no clube")

    monit = st.radio("Monitorado?",options=['Não','Sim'])

    if monit == 'Sim':
      data1_monit = st.date_input('Início do monitoramento')
      data2_monit = ""
      st.write("A data de fim do monitoramento será preenchida no momento do resultado")
    else:
      data1_monit = ""
      data2_monit = ""

    aval = st.radio("Avaliação?",options=['Não','Sim'])

    if aval == 'Sim':
      data1_aval = st.date_input('Início da avaliação')
      data2_aval = ""
      st.write("A data de fim da avaliação será preenchida no momento do resultado")

      

    else:
      data1_aval = ""
      data2_aval = ""

    contrat = st.radio("Contratado?",options=['Não','Sim'])

    if contrat == 'Sim':
      data_contrat = st.date_input('Data da contratação')

      situ_text = st.text("Situação: ATIVO")

        
elif acao == 'Editar atleta':
  
  st.subheader('Busca Rápida')
  pesq_rap = st.text_input('Digite o nome desejado:')
  
  lista_results = []
  nomes = pd.unique(base.Nome).tolist()
  t = 0
  while t<len(nomes):
    if pesq_rap in nomes[t]:
      lista_results.append(nomes[t])
    t += 1
    
  st.write(base[base.Nome.isin(lista_results)][['Nome','Data Nascimento','Posição']])
