# Stanislav Zapalikov 05-07-24
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
            print("Thank you")
            isRunning = False
    total = compute_bill(burgersDict)
    print_bill(total, burgersDict)
            
            
def show_menu():
    '''
    This function prints out the menu and prices
    '''
    print("1. De Anza Burger - $5.25")
    print("2. Bacon Cheese - $5.75")
    print("3. Mushroom Swiss - $5.95")
    print("4. Western Burger - $5.95")
    print("5. Don Cali Burger - $5.95")

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
        if (burger == 1):
            burgersDict["De Anza Burger...$5.25"] += 1
        if (burger == 2):
            burgersDict["Bacon Cheese...$5.75"] += 1
        if (burger == 3):
            burgersDict["Mushroom Swiss...$5.95"] += 1
        if (burger == 4):
            burgersDict["Western Burger...$5.95"] += 1
        if (burger == 5):
            burgersDict["Don Cali Burger...$5.95"] += 1
        if (burger == 6):
            return False
        else:
            print("Try again")
    except:
        print("Try again")
        
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
    
    return round(total, 2)

def print_bill(total, burgersDict):
    '''
    Prints the final bill
    
    Parameters:
    total (float): uses the output from the compute_bill() function as an input
    burgersDict (dictionary): dictionary with all the menu items
    '''
    if (total > 0):
        print("Your order is:")
        
        # Loops through every key and value in the dictionary and prints them
        for key, val in burgersDict.items():
            if (burgersDict.get(key) > 0):
                print(str(key) + ": " + str(val))
        
        tax = round(total * 0.09125, 2)
        print("Subtotal: " + str(round(total,2)))
        print("Tax: " + str(tax))
        print("Total: " + str(round(total + tax, 2)))
            

main()