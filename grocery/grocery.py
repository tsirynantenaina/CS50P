
def main():
    grocery_list = {}

    # Collecting items from user until EOFError (control-d)
    while True:
        try:
            item = input().strip().lower()
            if item in grocery_list:
                grocery_list[item] += 1
            else:
                grocery_list[item] = 1
        except EOFError:
            break

    # Sorting items alphabetically and printing in uppercase
    for item in sorted(grocery_list):
        print(f"{grocery_list[item]} {item.upper()}")

if __name__ == "__main__":
    main()
