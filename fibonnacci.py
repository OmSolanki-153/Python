print("Om Ajit Solanki")
n=int(input("Enter a Number:"))
a,b,s = 0,1,0
print(a,b,end=" ")
for x in range(n-2):
    s=a+b
    a,b = b,s
    print(s,end=" ")
