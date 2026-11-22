
while True:
    try:
        age = int(input("Your age:"))
        if age>=50:
                print("You're old")
        elif age>= 18:
            print("You're a chad")
        elif age<=10:
            print("You're a kid")
        
        break
    except ValueError:
        print("That is not a number")
        print("Enter a whole number")


