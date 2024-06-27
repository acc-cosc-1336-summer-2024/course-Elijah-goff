def get_factorial(num):

    factorial = 1

    for i in range(1, num + 1):
        factorial *= i

    return factorial

def sum_odd_numbers(num):

    sum_odd = 0

    current_number = 1

    while current_number <= num:

        if current_number %2 != 0:

            sum_odd += current_number

        current_number += 1
        
    return sum_odd

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

def option_3():
    print("Exiting...")            

