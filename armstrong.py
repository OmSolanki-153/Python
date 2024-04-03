print("Om Ajit Solanki")
def armstrong(n):
    s=0
    temp=n
    p=len(str(n))
    while(temp!=0):
        digit=temp%10
        s+=digit**p
        temp//=10
    if(s==n):
        print(n," is an Armstrong Number")
    else:
        print(n, "is not an Armstrong Number")
num=int(input("Enter a Number:"))
armstrong(num)
