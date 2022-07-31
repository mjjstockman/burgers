import gspread
from google.oauth2.service_account import Credentials
from tabulate import tabulate

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('burger_shop')

burgers = SHEET.worksheet('burgers')

data = burgers.get_all_values()
def welcome():
    print("Welcome to Burgers!\n")
    show_burgers()

def show_burgers():
    print("Here are our burgers...\n")
    print(tabulate(data, headers="firstrow", showindex="always", tablefmt="fancy_grid")) 
    choose_burger()

def choose_burger():
    print("Please choose which burger you would like\n")
    burger_choice = input("Enter your choice below\n")
    print(f"You entered {burger_choice}")

welcome()