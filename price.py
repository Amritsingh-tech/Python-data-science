amt=int(input("enter amount:"))
pm=input("payment method (credit ,cash,upi):")
if amt>1000:
    amt-=amt*.03 #discount 3%
if pm=="credit":
    amt-=100
amt+=amt*.18 #tax 18%
print("ur final amt is :",amt)