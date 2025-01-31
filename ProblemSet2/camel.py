
def convert(userInput):
#converting to snakecase
  snakeCase = ""
  for letters in userInput:
    if letters.isupper(): #checks if the letter is upper or not
        snakeCase = snakeCase + "_" + letters.lower() #if yes a underscore will be added infront of it
    else:
        snakeCase = snakeCase + letters
  return snakeCase



def main():
   userInput = input("enter in camelCase: ")
   result = convert(userInput)
   print (result)

main()
