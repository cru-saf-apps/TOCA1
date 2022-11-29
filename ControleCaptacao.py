import streamlit as st
import pandas as pd
import numpy as np
from gspread_pandas import Spread,Client
from google.oauth2 import service_account

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

st.write(base)

