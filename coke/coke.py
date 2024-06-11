# coke.py

def main():
    amount_due = 50

    while amount_due > 0:
        coin = int(input("Insert Coin: "))

        if coin == 25 or coin == 10 or coin == 5:
            amount_due -= coin
            if amount_due <= 0:
                change_owed = abs(amount_due)
                print("Change Owed:", change_owed)
                break
            else:
                print("Amount Due:", amount_due)
        else:
            print("Invalid coin! Please insert a valid coin.")

if __name__ == "__main__":
    main()
