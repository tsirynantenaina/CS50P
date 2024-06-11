def get_fuel_level():
    while True:
        try:
            fraction = input("Entrez une fraction (X/Y) : ").split('/')
            x, y = int(fraction[0]), int(fraction[1])
            if x > y or y == 0:
                print("Erreur : la fraction doit être au format X/Y avec X <= Y et Y > 0.")
                continue
            percentage = round((x / y) * 100)
            if percentage <= 1:
                print("E : essentiellement vide")
            elif percentage >= 99:
                print("F : essentiellement plein")
            else:
                print(f"{percentage}%")
            break
        except ValueError:
            print("Erreur : la fraction doit être au format X/Y avec X et Y des nombres entiers.")

if __name__ == "__main__":
    get_fuel_level()
