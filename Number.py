
total_num = 0
while True:
    text=input("enter a number or ('done'):")
    if text.lower()=="done":
        break
    total_num += float(text)
print(f"Total number is: {total_num:.2f}")