user = input("enter a sentence: ")
if " " in user:
    response = user.replace(" ", "...")
    print(response)