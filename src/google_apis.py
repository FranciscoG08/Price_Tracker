import gspread
import os
import json
from google.oauth2.service_account import Credentials

def connect(sheet_name):
    scope= [
        "https://www.googleapis.com/auth/spreadsheets",
        "https://www.googleapis.com/auth/drive"
    ]

    # Tenta ler do Secret do GitHub (Variável de Ambiente)
    creds_json = os.getenv("GOOGLE_CREDENTIALS")
    
    # Se estiver no GitHub, usa a info do Secret ## Caso seja o GitHub a correr o código
    if creds_json:
        # Se estiver no GitHub, usa a info do Secret
        info = json.loads(creds_json)
        creds = Credentials.from_service_account_info(info, scopes=scope)
    # Se estiver local, usa o teu ficheiro na pasta config
    else:
        creds = Credentials.from_service_account_file(
            "config/credentials.json",
            scopes=scope
        )

    client = gspread.authorize(creds)

    sheet = client.open(sheet_name).sheet1
    return sheet

def get_sheet_data(sheet_name):
    sheet = connect(sheet_name)
    data = sheet.get_all_records(numericise_ignore=['all'])
    return data,sheet

def add_new_product_row(sheet, row, store, name, first_price, last_price):
    # Otimizado: Envia B, C, D e E numa única chamada à API
    values = [[store, name, first_price, last_price]]
    sheet.update(range_name=f"B{row}:E{row}", values=values, value_input_option="USER_ENTERED")

def update_product_price(sheet, row, first_price, last_price):
    # Otimizado: Envia D e E numa única chamada à API
    values = [[first_price, last_price]]
    sheet.update(
        range_name=f"D{row}:E{row}",
        values=values,
        value_input_option="USER_ENTERED"
    )