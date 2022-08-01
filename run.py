import datetime
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
burger_data = burgers.get_all_values()
fries = SHEET.worksheet('fries')
fries_data = fries.get_all_values()
drinks = SHEET.worksheet('drinks')
drinks_data = drinks.get_all_values()


def welcome():
    print("Welcome to Burgers!\n")
    show_burgers()


def show_burgers():
    print("Here are our burgers...\n")
    print(tabulate(burger_data, headers="firstrow", showindex="always", tablefmt="fancy_grid")) 
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
            show_fries()
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


def show_fries():
    print("Here are our fries...\n")
    print(tabulate(fries_data, headers="firstrow", showindex="always", tablefmt="fancy_grid")) 
    choose_fries()


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
            show_drinks()
            break
        else:
            choose_fries()


def show_drinks():
    print("Here are our drinks...\n")
    print(tabulate(drinks_data, headers="firstrow", showindex="always", tablefmt="fancy_grid")) 
    choose_drink()

def choose_drink():
    while True:
        print("Please choose which drink you would like\n")
        drink_choice_num = input("Enter your choice below\n")
        if validate_drink_choice(drink_choice_num):
            if drink_choice_num == '0':
                drink_choice = "Cola"
            elif drink_choice_num == '1':
                drink_choice = "Lemonade"
            elif drink_choice_num == '2':
                drink_choice = "Orange Juice"
        if user_confirm(drink_choice):
            add_quantity(drink_choice)
            add_shot(drink_choice)
            break
        else:
            choose_drink()


def validate_drink_choice(drink_choice_num):
    try:
        if int(drink_choice_num) not in {0, 1, 2}:
            raise ValueError(
                "Must be a whole num between 0 and 2"
            )
    except ValueError as e:
        print(f"Invalid data: {e}, please try again")

    return True

def add_shot(drink_choice):
    while True:
        add_shot = input(f"Would you like to add a shot of whiskey to your {drink_choice}?\n")
        add_shot_strip_lcase = add_shot.strip().lower()
        if add_shot_strip_lcase == "y":
            dob()
            break
        elif add_shot_strip_lcase == "n":
            review_order()
            break
        else:
            print("Input must be either a Y or N")
            add_shot(drink_choice)


def get_dob():
    print("Plerase enter your date of birth")
    print("This should be in the dd/mm/yy format")
    dob = input("For example: 15/12/90\n")
    if validate_dob_format(dob):
        print("DOB ALL GOOD")
        if check_age(dob):
            print("Over 18")
    else:
        get_dob()

def check_age(dob):
    print("Checking age")

def validate_dob_format(dob):
    try:
        datetime.datetime.strptime(dob, '%d/%m/%y')
        return True
    except ValueError:
        print("let's try again!")


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


# def validate_drink_choice(drink_choice_num):
#     try:
#         if int(drink_choice_num) not in {0, 1, 2}:
#             raise ValueError(
#                 "Must be a whole num between 0 and 2"
#             )
#     except ValueError as e:
#         print(f"Invalid data: {e}, please try again")

    # return True
def review_order():
    print("You have ordered....")


def calulate_age(dob):
    print("Calculating dob on 216")


# welcome()
# show_drinks()
get_dob()