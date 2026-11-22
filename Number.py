
total_num = 0
while True:
    text=input("enter a number or ('done'):")
    if text.lower()=="done":
        break
    try:
        total_num += float(text)
    except ValueError:
        print("That is not a number")


print(f"Total number is: {total_num:.2f}")