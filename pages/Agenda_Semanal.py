import streamlit as st
import pandas as pd
from fpdf import FPDF
import base64
from gspread_pandas import Spread,Client
from google.oauth2 import service_account
import datetime as dt

def create_download_link(val, filename):
    b64 = base64.b64encode(val)  # val looks like b'...'
    return f'<a href="data:application/octet-stream;base64,{b64.decode()}" download="{filename}.pdf">Download file</a>'

def load_spreadsheet(spreadsheet_name):
    worksheet = sh.worksheet(spreadsheet_name)
    df = pd.DataFrame(worksheet.get_all_records())
    return df
  
scope = ['https://spreadsheets.google.com/feeds',
         'https://www.googleapis.com/auth/drive']


credentials = service_account.Credentials.from_service_account_info(
    st.secrets["gcp_service_account"],
    scopes=scope
)

client = Client(scope = scope, creds = credentials)

spreadsheet_name = "MONITORAMENTO"
spread = Spread(spreadsheet_name, client = client)
sh = client.open(spreadsheet_name)
base = load_spreadsheet(spreadsheet_name)

base['DATA INÍCIO'] = pd.to_datetime(base['DATA INÍCIO'],infer_datetime_format = True)

st.write(base.dtypes)

semana = st.date_input('Selecione a semana para visualizar monitoramentos',dt.date.today()).strftime('%m/%d/%Y')
base_print = base[base['DATA INÍCIO'] == semana]

anos = st.selectbox('Selecione a categoria',pd.unique(base_print.ANO))

base_print = base_print[base_print.ANO.isin(anos)]

pdf = FPDF()
pdf.add_page()

for ano in pd.unique(base_print.ANO):
  try:
    pdf.set_font('Arial','B',16)
    pdf.cell(40,10,base_print.ANO.tolist()[0],ln=1)
    
    pdf.cell(40, 10, ano,ln=1)
    
    base_ano = base_print[base_print.ANO == ano].reset_index(drop=True)
    comp = len(base_ano)
    
    t = 0
    while t <= comp:

      pdf.set_font('Arial','B',12)
      pdf.cell(40, 10, base_ano['NOME COMPLETO'][t],ln=0)
      
      pdf.cell(40, 10, base_ano['POSIÇÃO'][t],ln=0)
      
      pdf.cell(40, 10, base_ano['DATA NASCIMENTO'][t],ln=1)

      t+=1
  except:
    continue

export_as_pdf = st.button("Exportar")

if export_as_pdf:
    html = create_download_link(pdf.output(dest="S").encode("latin-1"), "Histórico de Negociações")
    st.markdown(html, unsafe_allow_html=True)
