print("Om AJit Solanki")
def palin(v):
    l=len(v)-1
    rev=""
    while l>=0:
        rev = rev+v[l]
        l-=1
    if(rev==v):
        print(v,"is a Palindrome")
    else:
        print(v,"is not a Palindrome")
s=input("Enter a String:")
palin(s)
