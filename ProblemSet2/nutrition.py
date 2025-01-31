def main():
    user = input("Item: ").lower()
    fruit_calories = {
    "Apple": 130,
    "Avocado": 50,
    "Banana": 110,
    "Cantaloupe": 50,
    "Grapefruit": 60,
    "Grapes": 90,
    "Honeydew": 50,
    "Kiwifruit": 90,
    "Lemon": 15,
    "Lime": 20,
    "Nectarine": 60,
    "Orange": 80,
    "Peach": 60,
    "Pear": 100,
    "Pineapple": 50,
    "Plums": 70,
    "Strawberries": 50,
    "Sweet Cherries": 100,
    "Tangerine": 50,
    "Watermelon": 80  }
    calories(user,fruit_calories)

def calories(user, fruit_calories):
    for keys in fruit_calories:
        if keys.lower() == user:
            print("Calories:",fruit_calories[keys])
main()
