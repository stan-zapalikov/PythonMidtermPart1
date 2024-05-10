# Hoang Khoi Do
# Midterm Part 1 assignment made to completely replace the physical menu

def main():
    isRunning = True
    
    # Dictionary with menu item names as keys and the amounts purchased as values
    burgersDict = {
        "De Anza Burger...$5.25": 0,
        "Bacon Cheese...$5.75": 0,
        "Mushroom Swiss...$5.95": 0,
        "Western Burger...$5.95": 0,
        "Don Cali Burger...$5.95": 0
    }

    show_menu()
    while (isRunning):
        if(get_inputs(burgersDict) == False):
            print("Thank you, have a nice day!!!")
            print("-" * 70)
            break
    total = compute_bill(burgersDict)
    while(isRunning):
        user_type = input("Are you a student or a staff? ").strip().lower()
        if (print_bill(total, burgersDict, user_type) == False):
            continue
        else:
            break
def show_menu():
    '''
    This function prints out the menu and prices
    '''
    print("1. De Anza Burger - $5.25")
    print("2. Bacon Cheese - $5.75")
    print("3. Mushroom Swiss - $5.95")
    print("4. Western Burger - $5.95")
    print("5. Don Cali Burger - $5.95")
    print("6. Exit")
    # help(show_menu)
def get_inputs(burgersDict):
    '''
    This function takes in user input and increments the dictionary values
    
    Parameters:
    burgersDict (dictionary): the dictionary with menu items as the keys and the amounts as values
    
    Returns:
    False when the user enters the sentinel value, stopping the main loop
    '''
    try:
        total = 0
        burger = int(input("Enter the burger you want to get (1-5, 6 to quit): "))
        match burger:
            case 1:
                burgersDict["De Anza Burger...$5.25"] += 1
            case 2:
                burgersDict["Bacon Cheese...$5.75"] += 1
            case 3:
                burgersDict["Mushroom Swiss...$5.95"] += 1
            case 4:
                burgersDict["Western Burger...$5.95"] += 1
            case 5:
                burgersDict["Don Cali Burger...$5.95"] += 1
            case 6:
                return False
            case default:
                raise ValueError
    except ValueError:
        print("Try again, please enter the numeric input from 1-6")
    # help(get_inputs)
        
def compute_bill(burgersDict):
    '''
    Computes the bill based on the values in the dictionary
    
    Parameters:
    burgersDict (dictionary): looks at every value in the dictionary and multiplies
                              it by a given price and assigns it to total
    
    Returns:
    total (float): rounded total of all the prices, if the dict values are 0 then it returns 0
    '''
    total = 0
    total += burgersDict.get("De Anza Burger...$5.25") * 5.25
    total += burgersDict.get("Bacon Cheese...$5.75") * 5.75
    total += burgersDict.get("Mushroom Swiss...$5.95") * 5.95
    total += burgersDict.get("Western Burger...$5.95") * 5.95
    total += burgersDict.get("Don Cali Burger...$5.95") * 5.95
    # help(compute_bill)
    return round(total, 2)
    

def print_bill(total, burgersDict, user_type):
    '''
    Prints the final bill
    
    Parameters:
    total (float): uses the output from the compute_bill() function as an input
    burgersDict (dictionary): dictionary with all the menu items
    '''
    print("-" * 70)
    # 
    TAX = 0.09
    try:
        if (user_type == "student"):
            for key, val in burgersDict.items():
                if (burgersDict.get(key) > 0):
                    print("Quantity of " + str(key) + ": " + str(val))
            print("There will be no tax for student.")
            print("Total: " + str(total))
        elif (user_type == "staff"):
            tax_amount = round(total * TAX, 2)
            for key, val in burgersDict.items():
                if (burgersDict.get(key) > 0):
                    print("Quantity of " + str(key) + ": " + str(val))
            print("There will be tax for staff. ")
            print("Subtotal: " + str(round(total,2)))
            print("Tax amount: " + str(tax_amount))
            print("Total: " + str(round(total + tax_amount, 2)))
        else:
            raise ValueError
            
    except ValueError:
        print("You enter the wrong input, please do it again")
        return False
    # help(print_bill)
                    
main()

'''
Output 1:
    1. De Anza Burger - $5.25
    2. Bacon Cheese - $5.75
    3. Mushroom Swiss - $5.95
    4. Western Burger - $5.95
    5. Don Cali Burger - $5.95
    6. Exit
    Enter the burger you want to get (1-5, 6 to quit): 1
    Enter the burger you want to get (1-5, 6 to quit): 2
    Enter the burger you want to get (1-5, 6 to quit): 3
    Enter the burger you want to get (1-5, 6 to quit): 4
    Enter the burger you want to get (1-5, 6 to quit): 5
    Enter the burger you want to get (1-5, 6 to quit): 6
    Thank you, have a nice day!!!
    ----------------------------------------------------------------------
    Are you a student or a staff? student
    ----------------------------------------------------------------------
    Quantity of De Anza Burger...$5.25: 1
    Quantity of Bacon Cheese...$5.75: 1
    Quantity of Mushroom Swiss...$5.95: 1
    Quantity of Western Burger...$5.95: 1
    Quantity of Don Cali Burger...$5.95: 1
    There will be no tax for student.
    Total: 28.85
Output 2:
    1. De Anza Burger - $5.25
    2. Bacon Cheese - $5.75
    3. Mushroom Swiss - $5.95
    4. Western Burger - $5.95
    5. Don Cali Burger - $5.95
    6. Exit
    Enter the burger you want to get (1-5, 6 to quit): 1
    Enter the burger you want to get (1-5, 6 to quit): 2
    Enter the burger you want to get (1-5, 6 to quit): 3
    Enter the burger you want to get (1-5, 6 to quit): 4
    Enter the burger you want to get (1-5, 6 to quit): 5
    Enter the burger you want to get (1-5, 6 to quit): 6
    Thank you, have a nice day!!!
    ----------------------------------------------------------------------
    Are you a student or a staff? STAFF
    ----------------------------------------------------------------------
    Quantity of De Anza Burger...$5.25: 1
    Quantity of Bacon Cheese...$5.75: 1
    Quantity of Mushroom Swiss...$5.95: 1
    Quantity of Western Burger...$5.95: 1
    Quantity of Don Cali Burger...$5.95: 1
    There will be tax for staff. 
    Subtotal: 28.85
    Tax amount: 2.6
    Total: 31.45
'''


