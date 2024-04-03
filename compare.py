print("Om Ajit Solanki")
def compare (l1,l2):
    for i in l1:
        if(i in l2):
            return True
            break
        else:
            return False
print("Enter 5 values of list 1")
n1=[]
for i in range(5):
    n1.append(input())
print("Enter 5 values of list 2")
n2=[]
for i in range(5):
    n2.append(input())
if compare (n1,n2):
    print("\n Lists contain common value")
else:
    print("\n No common value in the lists")
