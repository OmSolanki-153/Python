print("Om Ajit Solanki")
s=input("Enter a String:")
i= c = 0
while(i<len(s)):
    if(s[i]=='a'):
        print(i+1)
        c+=1
    i+=1
if(c==0):
    print(s, "does not contain the letter a")
else:
    print(s, "contain the letter a",c,"times")
