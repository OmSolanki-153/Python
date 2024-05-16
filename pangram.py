print("Om Ajit Solanki")
def pangram(s):
    l = len(set(s))
    if l>=26:
        print("Sentence is a Pangram")
    else:
        print("Sentence is not a Pangram")
sent = input("Enter a sentence:")
pangram(sent.lower())
