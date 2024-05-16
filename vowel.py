print("Om Ajit Solanki")
def vowel(c):
    return(c.lower() in ['a','e','i','o','u'])
c = input("Enter a Character:")
if vowel(c):
    print("Vowel")
else:
    print("Consonant")
