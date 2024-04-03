print("Om Ajit Solanki")
import os
os.system("cls")
def histogram(n):
    for i in n:
            print("*" * i)
            #print()
r=int(input("Enter no. of rows in histogram:"))
num=[]
for i in range(r):
    num.append(int(input("Enter value for row {}:".format(i+1))))
histogram(num)
