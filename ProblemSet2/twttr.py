def main():
    userInput = input("Input: ")
    vowels = [ "a","e","i","o","u","A","E","I","O","U"]
    result = check(userInput, vowels)
    print(result)



def check(userInput, vowels):
   result = ""
   for letters in userInput:
     if letters not in vowels:
        result = result + letters
   return result


main()

