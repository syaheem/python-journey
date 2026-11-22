RATE=4.15

def to_rm(usd):
    return usd*RATE
x=float(input("Enter first amount:"))
y= float(input("Enter second amount:"))
z= float(input("Enter third amount:"))
print("1st",f"{to_rm(x):.2f}","2nd",f"{to_rm(y):.2f}","3rd",f"{to_rm(z):.2f}")