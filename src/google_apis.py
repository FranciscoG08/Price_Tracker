import gspread
from google.oauth2.service_account import Credentials

def connect(sheet_name):
    scope= [
        "https://www.googleapis.com/auth/spreadsheets",
        "https://www.googleapis.com/auth/drive"
    ]
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

def add_new_product_row(sheet,row,store,name,first_price,last_price):
    sheet.update(f"B{row}", [[store]])
    sheet.update(f"C{row}", [[name]])
    sheet.update(f"D{row}", [[first_price]])
    sheet.update(f"E{row}", [[last_price]])

def update_product_price(sheet, row, first_price, last_price):
    sheet.update(
        f"D{row}",
        [[first_price]],
        value_input_option="USER_ENTERED"
    )
    sheet.update(
        f"E{row}",
        [[last_price]],
        value_input_option="USER_ENTERED"
    )