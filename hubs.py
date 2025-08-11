import streamlit as st
import pandas as pd
import gspread
from google.oauth2.service_account import Credentials
from datetime import datetime

# === CONFIGURAÇÃO DO APP ===
st.set_page_config(layout="wide")
st.title("📊 Dashboard - Relatório de Hubs")

# === CONEXÃO COM GOOGLE SHEETS via SECRETS ===
SCOPES = ["https://www.googleapis.com/auth/spreadsheets"]
service_account_info = st.secrets["google_service_account"]
creds = Credentials.from_service_account_info(service_account_info, scopes=SCOPES)
client = gspread.authorize(creds)

# ID e Nome da Planilha
SHEET_ID = "1L9X2Xt0C-g87w97qbWQIqJKyDcnchmUU0UIZbixmCac"
SHEET_NAME = "Página1"
sheet = client.open_by_key(SHEET_ID).worksheet(SHEET_NAME)

# === LEITURA DOS DADOS ===
data = sheet.get_all_records()
df = pd.DataFrame(data)

# ===hu
