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

items = []


def welcome():
    """welcomes the user with a simple greeting
    """
    print("Welcome to Burgers!\n")
    show_burgers()


def show_burgers():
    """Uses tabulate to pretty print the burgers
    Calls the choose_burger function
    """
    print("Here are our burgers...\n")
    print(tabulate(burger_data, headers="firstrow", showindex="always",
          tablefmt="fancy_grid"))
    choose_burger()


def choose_burger():
    """a loop to continue asking the user to choose a burger until their choice 
    is validated
    The user is then asked to confirm their choice
    If validated and confirmed the choice is added to the items list and 
    show_fries is called.
    If the user does not confirm their choice or enter an invalid choice the
    function calls itself again
    """
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
        if user_confirm(burger_choice_num):
            items.append(burger_choice_num)
            show_fries()
            break
        else:
            choose_burger()

def choose_drink():
    """a loop to continue asking the user to choose a drink until their choice 
    is validated
    The user is then asked to confirm their choice
    If validated and confirmed the choice is added to the items list and 
    add_shot is called.
    If the user does not confirm their choice or enter an invalid choice the
    function calls itself again
    """
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
        if user_confirm(drink_choice_num):
            items.append(drink_choice_num)
            add_shot(drink_choice_num)
            break
        else:
            choose_drink()
            

def validate_burger_choice(burger_choice_num):
    """If the entered number is not an int between 0 and 3
    an exception is raised

    Args:
        burger_choice_num (str): the users choice of burger

    Raises:
        ValueError: when an invalid choice is made

    Returns:
        True if there are no errors
    """
    try:
        if int(burger_choice_num) not in {0, 1, 2, 3}:
            raise ValueError(
                "Must be a whole num between 0 and 3"
            )
    except ValueError as e:
        print(f"Invalid data: {e}, please try again")

    return True


def validate_fries_choice(fries_choice_num):
    """If the entered number is not an int between 0 and 2
    an exception is raised

    Args:
        fries_choice_num (str): the users choice of fries

    Raises:
        ValueError: when an invalid choice is made

    Returns:
        True if there are no errors
    """
    try:
        if int(fries_choice_num) not in {0, 1, 2}:
            raise ValueError(
                "Must be a whole num between 0 and 2"
            )
    except ValueError as e:
        print(f"Invalid data: {e}, please try again")

    return True


def user_confirm(data):
    """asks the user to confirm a choice by entering Y, y, N or n
    THe answer is stripped of whitespace and if the user does not enter a 
    valid answer they are asked again


    Args:
        data (str): the data the user is confirming

    Returns:
        boolean: True if user eenters Y or y
        boolean: False if user eenters N or n
    """
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
        print("\nInput must be either a Y or N")
        print("Let's try that again\n")
        user_confirm(data)


def show_fries():
    """Uses tabulate to pretty print the fries
    Calls the choose_fries function
    """
    print("\nHere are our fries...\n")
    print(tabulate(fries_data, headers="firstrow", showindex="always",
          tablefmt="fancy_grid"))
    choose_fries()


def choose_fries():
    """a loop to continue asking the user to choose their fries until their
    choice is validated
    The user is then asked to confirm their choice
    If validated and confirmed the choice is added to the items list and 
    show_drinks is called.
    If the user does not confirm their choice or enter an invalid choice the
    function calls itself again
    """
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
        if user_confirm(fries_choice_num):
            items.append(fries_choice_num)
            show_drinks()
            break
        else:
            choose_fries()


def show_drinks():
    """Uses tabulate to pretty print the drinks
    Calls the choose_drink function
    """
    print("Here are our drinks...\n")
    print(tabulate(drinks_data, headers="firstrow", showindex="always",
          tablefmt="fancy_grid"))
    choose_drink()


def choose_drink():
    """a loop to continue asking the user to choose their drink until their
    choice is validated
    The user is then asked to confirm their choice
    If validated and confirmed the choice is added to the items list and 
    add_whisky is called.
    If the user does not confirm their choice or enter an invalid choice the
    function calls itself again
    """
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
        if user_confirm(drink_choice_num):
            items.append(drink_choice_num)
            add_whisky(drink_choice_num)
            break
        else:
            choose_drink()


def validate_drink_choice(drink_choice_num):
     """If the entered number is not an int between 0 and 2
    an exception is raised

    Args:
        drinks_choice_num (str): the users choice of drink

    Raises:
        ValueError: when an invalid choice is made

    Returns:
        True if there are no errors
    """
    try:
        if int(drink_choice_num) not in {0, 1, 2}:
            raise ValueError(
                "Must be a whole num between 0 and 2"
            )
    except ValueError as e:
        print(f"Invalid data: {e}, please try again")

    return True


def add_whisky(drink_choice_num):
    """Asks the user if they want a shot of whisky in their drink

    Args:
        drink_choice_num (str): _description_

    Returns:
        True if there are no errors
    """
    while True:
        add_shot = input(f"\nAdd a shot of whisky to your drink?\n")
        add_shot_strip_lcase = add_shot.strip().lower()
        if add_shot_strip_lcase == "y":
            get_dob()
            return False
        elif add_shot_strip_lcase == "n":
            show_order()
            return False
        else:
            print("Input must be either a Y or N")
            add_whisky(drink_choice_num)


def get_dob():
    """asks the user for their date of birth if ordering whisky
    Adss whisky to the item list if so
    """
    print("\nPlease enter your date of birth\n")
    print("This should be in the dd/mm/yy format")
    dob = input("For example: 15/12/90\n")
    if validate_dob_format(dob):
        if check_age(dob):
            items.append("with whisky")
            show_order()
        else:
            print("Sorry you're not old enough.")
            print("We check ID on collection anyway!")
            show_order()
    else:
        get_dob()


def check_age(dob):
    """Checks if the user is 18 or above

    Args:
        dob (datetime): users date of birth

    Returns:
        boolean: True if over 18, False if not
    """
    today = datetime.datetime.today()
    dob_date = datetime.datetime.strptime(dob, "%d/%m/%y")
    age = today.year - dob_date.year - ((today.month, today.day) <
                                        (dob_date.month, dob_date.day))
    if age >= 18:
        return True
    else:
        return False


def validate_dob_format(dob):
    """validates date of birth format to be d/m/y

    Args:
        dob (datetime): users date of birth

    Returns:
        boolean: True if date of birth is validated
    """
    try:
        datetime.datetime.strptime(dob, '%d/%m/%y')
        return True
    except ValueError:
        print("let's try again!")


def show_order():
    """Shows the order back to the customer
    """
    print("You have ordered the following:\n")
    print(f"Burger number {items[0]}, number {items[1]} fries and number {items[2]} drink")
    send_to_order()


def send_to_order():
    """Adds the order to the orders worksheet
    """
    order_worksheet = SHEET.worksheet("orders")
    order_worksheet.append_row(items)


welcome()

