print("Om Ajit Solanki")
n= int(input("Enter a number: "))
for d in range(2,n):
    if n%d==0:
        print("Not a Prime Number")
        break
else:
    print("Prime Number")
