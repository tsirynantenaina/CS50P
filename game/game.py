import random

def main():
    level = get_level()
    target_number = random.randint(1, level)

    while True:
        guess = get_guess()
        if guess < target_number:
            print("Too small!")
        elif guess > target_number:
            print("Too large!")
        else:
            print("Just right!")
            break

def get_level():
    while True:
        try:
            level = int(input("Level: "))
            if level > 0:
                return level
        except ValueError:
            pass

def get_guess():
    while True:
        try:
            guess = int(input("Guess: "))
            if guess > 0:
                return guess
        except ValueError:
            pass

if __name__ == "__main__":
    main()
