
#Out of boundary error function
def choice_(prompt, min_val, max_val, choice):
    while True:
        try:
            if min_val <= choice <= max_val:
                return choice
            print(f"Please enter a number between {min_val} and {max_val}." )
            choice = int(input(">"))
        except ValueError:
            print("Please enter a whole number")
    return choice            


    
#Add expeneses function
def add_expense():
    while True:
        try:
            print("=== Type of Expenses ===")
            print("1. Debt")
            print("2. Grocery")
            print("3. Subscription")
            print("4. Other")
            print("5. Exit")
            choice = int(input(">"))
        except ValueError:
            print("That is not a valid number")
            continue
        choice = choice_(">", 1, 5, choice)
        if choice == 1:
            expenses_detail("Debt")
        elif choice == 2:
            expenses_detail("Grocery")
        elif choice == 3:
            expenses_detail("Subscription")
        elif choice == 4:
            expenses_detail("Other")
        elif choice == 5:
            break
expenses = []

#Storing all expenses data 
def expenses_detail(type):
    
    expense = {}
    print("=== ", type, " ===")
    expense["type"] = type
    while True:
        try:
            expense["value"] = float(input("How much spent: "))
            break
        except ValueError:
            print("Please enter a whole number")
    expense["miscellanous"] = input("Other information: ")
    expenses.append(expense)

    with open("expenses.txt", "a") as file:
        file.write(f"{expense['type']},{expense['value']:.2f},{expense['miscellanous']}\n")
    print("Expense successfully added and saved")
    
#View all expenses function
def view_():
    print("\n=== All Expenses ===")
    try:
        with open("expenses.txt", "r") as file:
            for line in file:
                category,value,information = line.strip().split(",")
                print(f"Category: {category} | Value(RM): {value} | Information: {information}")
    except FileNotFoundError:
                print("File does not exist")



#View summary function
def view_summary():
    print("\n=== All Expenses Summary ===")
    values = []
    category_totals = {}
   
    try:
        with open("expenses.txt", "r") as file:
            for line in file:
                category,value,information = line.strip().split(",")
                num = float(value)
                values.append(num)

                if category in category_totals:
                    category_totals[category] += num
                else:
                     category_totals[category] = num
        
        if values:
            total = sum(values)
            average = total/len(values)
            highest = max(values)
            lowest = min(values)

            print(f"Total spent: {total:.2f}")
            print(f"Average spent per item: {average:.2f}")
            print(f"Maxmimum spent: {highest:.2f}")
            print(f"Minimum spent: {lowest:.2f}")

            print("\n--- Spending by Category ---")
            for cat,amount in category_totals.items():
                print(f"- {cat}: RM {amount:.2f}")
        else:
            print("No expenses found in the file")
        
    except FileNotFoundError:
        print("File did not exist")




while True:
    try:    

        print("=== Expense Tracker ===")
        print("1. Add Expense")
        print("2. View All Expenses")
        print("3. View Summary (Total, Highest, Average)")
        print("4. Exit")
        choice = int(input(">"))
    except ValueError:
        print("That is not a valid number")
        continue
    choice = choice_(">", 1, 4, choice)
    if choice == 1:
        add_expense()
    elif choice == 2:
        view_()
    elif choice == 3:
        view_summary()
    elif choice == 4:
        break



