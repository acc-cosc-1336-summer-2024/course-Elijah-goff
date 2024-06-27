import repetition

def display_menu():
    print("1-Factorials")
    print("2-Sum Odd Numbers")
    print("3-Exit")

def user_controlled_loop():

    option = "1"
    
    while(option != "3"):
        display_menu()
        option = input(int("Enter Menu Option"))
        handle_menu_option(option)

def handle_menu_options(option):

    if (option == "1"):
         
         option_1()
    elif (option == "2"):
         option_2()
    elif (option =="3"):
         print("Exiting...")
    else:
        print("Invalid Input")


def option_1():
    print("User selected Option 1")

def option_2():
    print("User selected Option 2")

