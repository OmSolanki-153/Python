print("Om Ajit Solanki")
n= int(input("Enter a number:"))
div=0
for x in range(1,n+1):
    if n%x==0:
        div+=1
print("\n No. of Divisors =", div)
