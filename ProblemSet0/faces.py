def converting(text):
    if ":)" in text:
        response = text.replace(":)", "🙂")
        print(response)
    elif ":(" in text:        
        response = text.replace(":(", "🙁")
        print(response)

def main():
    userInput = input("enter: ")
    converting(userInput)
    

main()