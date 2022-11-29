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
monit = load_spreadsheet(spreadsheet_name)


spreadsheet_name = "AVALIAÇÃO"
spread = Spread(spreadsheet_name, client = client)
sh = client.open(spreadsheet_name)
aval = load_spreadsheet(spreadsheet_name)


monit['DATA INÍCIO'] = pd.to_datetime(monit['DATA INÍCIO'],infer_datetime_format = True)
monit['DATA FIM'] = pd.to_datetime(monit['DATA FIM'],infer_datetime_format = True)
monit['DATA NASCIMENTO'] = pd.to_datetime(monit['DATA NASCIMENTO'],infer_datetime_format = True)

aval['DATA INÍCIO'] = pd.to_datetime(aval['DATA INÍCIO'],infer_datetime_format = True)
aval['DATA FIM'] = pd.to_datetime(aval['DATA FIM'],infer_datetime_format = True)
aval['DATA NASCIMENTO'] = pd.to_datetime(aval['DATA NASCIMENTO'],infer_datetime_format = True)


opcao = st.radio('Deseja visualizar Avaliações ou Monitoramentos?',options=['Avaliações','Monitoramentos'])

if opcao == 'Monitoramentos':

    semana = st.date_input('Selecione a semana para visualizar monitoramentos',dt.date.today()).strftime('%m/%d/%Y')

    monit_print = monit[monit['DATA INÍCIO'] == semana]

    if monit_print.empty:
        st.write('Não há monitoramentos agendados para iniciar na data selecionada.')

    else:
        anos = st.multiselect('Selecione a categoria',pd.unique(monit_print.ANO))
        lista_anos = []
        for ano in anos:
            lista_anos.append(ano)

        monit_print = monit_print[monit_print.ANO.isin(lista_anos)]

        pdf = FPDF()
        pdf.add_page()
        pdf.set_font('Arial','B',16)
        try:
            pdf.cell(100,10,"Agenda de Monitorados em "+str(monit_print['DATA INÍCIO'].tolist()[0].strftime('%d/%m/%Y')),ln=1,border='B')
            pdf.cell(40,10," ",ln=1)
        except:
            st.write('Favor selecionar uma semana válida e anos válidos')


        for ano in pd.unique(monit_print.ANO):

            monit_ano = monit_print[monit_print.ANO == ano].reset_index(drop=True)

            pdf.set_font('Arial','B',14)
            pdf.cell(15,10,str(ano),ln=1,border='B')    

            comp = len(monit_ano)

            t = 0
            while t < comp:

              pdf.set_font('Arial','',12)
              pdf.cell(40, 10, monit_ano['NOME COMPLETO'][t],ln=0,border='B')

              pdf.cell(40, 10, monit_ano['POSIÇÃO'][t],ln=0,border='B')

              pdf.cell(40, 10, str(monit_ano['DATA NASCIMENTO'][t].strftime('%d/%m/%Y')),ln=1,border='B')
              pdf.cell(40, 10, " ",ln=1)

              t+=1

        export_as_pdf = st.button("Exportar")

        if export_as_pdf:
            html = create_download_link(pdf.output(dest="S").encode("latin-1"), "Agenda de Monitoramentos em "+str(monit_print['DATA INÍCIO'].tolist()[0].strftime('%d/%m/%Y')))
            st.markdown(html, unsafe_allow_html=True)

elif opcao == 'Avaliações':
    
    semana = st.date_input('Selecione a semana para visualizar avaliações',dt.date.today()).strftime('%m/%d/%Y')

    aval_print = aval[aval['DATA INÍCIO'] == semana]

    if aval_print.empty:
        st.write('Não há avaliações agendadas para iniciar na data selecionada.')

    else:
        anos = st.multiselect('Selecione a categoria',pd.unique(aval_print.ANO))
        lista_anos = []
        for ano in anos:
            lista_anos.append(ano)

        aval_print = aval_print[aval_print.ANO.isin(lista_anos)]

        pdf = FPDF()
        pdf.add_page()
        pdf.set_font('Arial','B',16)
        try:
            pdf.cell(100,10,"Agenda de Monitorados em "+str(aval_print['DATA INÍCIO'].tolist()[0].strftime('%d/%m/%Y')),ln=1,border='B')
            pdf.cell(40,10," ",ln=1)
        except:
            st.write('Favor selecionar uma semana válida e anos válidos')


        for ano in pd.unique(aval_print.ANO):

            aval_ano = aval_print[aval_print.ANO == ano].reset_index(drop=True)

            pdf.set_font('Arial','B',14)
            pdf.cell(15,10,str(ano),ln=1,border='B')    

            comp = len(aval_ano)

            t = 0
            while t < comp:

              pdf.set_font('Arial','',12)
              pdf.cell(40, 10, aval_ano['NOME COMPLETO'][t],ln=0,border='B')

              pdf.cell(40, 10, aval_ano['POSIÇÃO'][t],ln=0,border='B')

              pdf.cell(40, 10, str(aval_ano['DATA NASCIMENTO'][t].strftime('%d/%m/%Y')),ln=1,border='B')
              pdf.cell(40, 10, " ",ln=1)

              t+=1

        export_as_pdf = st.button("Exportar")

        if export_as_pdf:
            html = create_download_link(pdf.output(dest="S").encode("latin-1"), "Agenda de Monitoramentos em "+str(monit_print['DATA INÍCIO'].tolist()[0].strftime('%d/%m/%Y')))
            st.markdown(html, unsafe_allow_html=True)
