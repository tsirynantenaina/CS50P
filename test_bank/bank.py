def value(greeting):
    if greeting.lower().startswith("hello"):
        return 0
    elif greeting.lower().startswith("h"):
        return 20
    else:
        return 100

def main():
    greeting = input("Entrez un salut : ")
    result = value(greeting)
    print(result)

if __name__ == "__main__":
    main()
