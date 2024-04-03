print("Om Ajit Solanki")
a = input ("Enter area Code:")
s = int(input("Enter sales:"))
if (a == "C"):
    if (s>=100000):
        c=s*0.10
    elif(s>=50000):
        c=s*0.05
    else:
        c=1000
    print("\nCommission=",c)
elif(a=="v"):
    if(s>=100000):
        c= s*0.15
    elif(s>= 50000):
        c=s*0.08
    else:
        c=1500
    print("\n Commission = ",c)
else:
    print("\n\n Invalid Area Code")
