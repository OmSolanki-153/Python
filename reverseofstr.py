print("Om Ajit Solanki")
def reverse(v):
    l = len(v)-1
    rev = " "
    while l>=0:
        rev = rev + v[l]
        l-=1
    return rev
val=input("Enter a value:")
print("Reverse = ",reverse(val))
