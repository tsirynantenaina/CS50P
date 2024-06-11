fruits_calories = {
    "apple": 130,
    "banana": 100,
    "grapefruit": 60,
    "grapes": 90,
    "honeydew melon": 50,
    "kiwifruit": 90,
    "lemon": 15,
    "lime": 20,
    "nectarine": 60,
    "orange": 80,
    "peach": 60,
    "pear": 100,
    "pineapple": 50,
    "plums": 30,
    "strawberries": 50,
    "sweet cherries": 100,
    "tangerine": 50,
    "watermelon": 50
}

fruit = input("Entrez un fruit : ").lower().strip()

if fruit in fruits_calories:
    print(f"Item {fruit}, calories: {fruits_calories[fruit]}")
else:
    print("Désolé, ce fruit n'est pas dans la liste.")
