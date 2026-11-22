def get_value(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("That is not a whole number, please try again!")
grade = get_value("Enter a grade: ")
print(get_value(f"Your grade is: {grade:.2f}"))