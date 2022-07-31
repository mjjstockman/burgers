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
            if burger_choice_num == '0':
                burger_choice = "Beef"
            elif burger_choice_num == '1':
                burger_choice = "Chicken"
            elif burger_choice_num == '2':
                burger_choice = "Tofu"
            elif burger_choice_num == '3':
                burger_choice = "Seitan"
        if user_confirm(burger_choice):
            add_quantity(burger_choice)
            choose_fries()
            break
        else:
            choose_burger()

def validate_burger_choice(burger_choice_num):
    try:
        if int(burger_choice_num) not in {0, 1, 2, 3}:
            raise ValueError(
                "Must be a whole num between 1 and 4"
            )
    except ValueError as e:
        print(f"Invalid data: {e}, please try again")
        validate_burger_choice(burger_choice_num)

    return True

def validate_fries_choice(fries_choice_num):
    try:
        if int(fries_choice_num) not in {0, 1, 2}:
            raise ValueError(
                "Must be a whole num between 0 and 2"
            )
    except ValueError as e:
        print(f"Invalid data: {e}, please try again")

    return True

def user_confirm(data):
    print(f"You entered {data}\n")
    print("Is this correct?\n")
    confirm = input("Enter Y for yes, N for No:\n")
    confirm_strip_lcase = confirm.strip().lower()
    if confirm_strip_lcase == "y":
        # print(f"You said {data} is correct!")
        return True
    elif confirm_strip_lcase == "n":
        print("Let's try again")
        return False
    else:
        print("Input must be either a Y or N")
        user_confirm(data)

def add_quantity(data):
    while True:
        quantity = input(f"How many {data} would you like?\n")
        try:
            if int(quantity) not in (1, 2, 3, 4, 5):
                raise ValueError()
            else:
                if user_confirm(quantity):
                    return False
        except ValueError:
            print(f"Invalid data: make sure you enter a full number between 1 and 5")
        

def choose_fries():
    while True:
        print("Please choose which fries you would like\n")
        fries_choice_num = input("Enter your choice below\n")
        if validate_fries_choice(fries_choice_num):
            if fries_choice_num == '0':
                fries_choice = "Straight Fries"
            elif fries_choice_num == '1':
                fries_choice = "Curly Fries"
            elif fries_choice_num == '2':
                fries_choice = "Sweet Potatoe Fries"
        if user_confirm(fries_choice):
            add_quantity(fries_choice)
            add_drink()
            break
        else:
            choose_fries()


def add_drink():
    print("SAAAAAAAFE FROM 137")

welcome()

