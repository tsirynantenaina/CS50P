def main():
    # Exemple d'utilisation des fonctions pour les tester manuellement
    try:
        fraction = input("Enter fraction (X/Y): ")
        percentage = convert(fraction)
        print(f"Percentage: {percentage}%")
        print(f"Gauge: {gauge(percentage)}")
    except ValueError as e:
        print(e)
    except ZeroDivisionError as e:
        print(e)

def convert(fraction):
    try:
        x, y = fraction.split("/")
        x = int(x)
        y = int(y)
        if y == 0:
            raise ZeroDivisionError("Y cannot be zero")
        if x > y:
            raise ValueError("X cannot be greater than Y")
        percentage = round((x / y) * 100)
        return percentage
    except ValueError:
        raise ValueError("Invalid input: X and Y must be integers and X/Y must be a valid fraction")


def gauge(percentage):
    if percentage <= 1:
        return "E"
    elif percentage >= 99:
        return "F"
    else:
        return f"{percentage}%"

if __name__ == "__main__":
    main()
