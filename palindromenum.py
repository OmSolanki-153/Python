print("Om Ajit Solanki")
def palin(n):
    s=0
    temp=n
    while(temp!=0):
        rem=temp%10
        s=rem+(s*10)
        temp//=10
    if(s==n):
        print(n,"is a Palindrome")
    else:
        print(n,"is not a Palindrome")
num= int(input("Enter a Number:"))
palin(num)
