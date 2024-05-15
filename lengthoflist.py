print("Om Ajit Solanki")
def count(s):
    len = 0
    for c in s:
        len+=1
    return len
str = input("Enter a string:")
print("\n Length of the string =",count(str))
print("Length =", count(list(str)))
l1=[10,20,30]
print("\n Length of the list=",count(l1))
