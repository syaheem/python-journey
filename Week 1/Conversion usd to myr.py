RATE=4.15

def to_rm(usd):
    return usd*RATE
usd=float(input("Enter first amount:"))
if usd < 0:
    print("Error:Invalid amount")
elif usd == 0:
    print("Notice:Zero dollars equals RM 0.00")

else :

    print(f"RM {to_rm(usd):.2f}")
