def  main():
    user = input("Greetings: ").lower().strip()
    response(user)



def response(user):
    if user[:5] == "hello":
        print("$0")
    elif userstartswith("h"):
            print("$20")
    else:
        print("$100")

if __name__ == "__main__":
    main()