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
    while True:
        print("Please choose which burger you would like\n")
        burger_choice_num = input("Enter your choice below\n")
        if validate_burger_choice(burger_choice_num):
            if user_confirm(burger_choice_num):
                print(f"You chose {burger_choice_num}, from 33")
                break
        else:
            choose_burger()

def validate_burger_choice(burger_choice_num):
    try:
        if int(burger_choice_num) not in {1, 2, 3, 4}:
            raise ValueError(
                "Must be a whole num between 1 and 4"
            )
    except ValueError as e:
        print(f"Invalid data: {e}, please try again")
        return False

    return True

def user_confirm(data):
    print(f"You entered {data}\n")
    print("Is this correct?\n")
    confirm = input("Enter Y for yes, N for No:\n")
    confirm_strip_lcase = confirm.strip().lower()
    if confirm_strip_lcase == "y":
        print(f"You said {data} is correct!")
        return True
    elif confirm_strip_lcase == "n":
        print("Let's try again")
        return False
    else:
        print("Input must be either a Y or N")
        user_confirm(data)

    # if burger_choice_num == 1:
    #     burger = "Beef"
    # elif burger_choice_num == 2:
    #     burger = "Chicken"
    #     print(f"You entered {burger}")
    # elif burger_choice_num == 3:
    #     burger = "Vegan"
    # elif burger_choice_num == 4:
    #     burger = "Tofu"
    #     print(f"You chose {burger}")

    

welcome()