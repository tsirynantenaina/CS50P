# outdated.py

def main():
    while True:
        date_input = input("Date: ")
        try:
            formatted_date = convert_date(date_input)
            if formatted_date:
                print(formatted_date)
                break
        except ValueError:
            continue

def convert_date(date_input):
    months = [
        "January", "February", "March", "April", "May", "June",
        "July", "August", "September", "October", "November", "December"
    ]

    # Check for MM/DD/YYYY format
    if "/" in date_input:
        parts = date_input.split("/")
        if len(parts) == 3:
            month, day, year = parts
            if is_valid_date(month, day, year):
                return f"{int(year):04}-{int(month):02}-{int(day):02}"

    # Check for Month D, YYYY format
    elif "," in date_input:
        try:
            month_day, year = date_input.split(", ")
            month_name, day = month_day.split(" ")
            month = months.index(month_name) + 1
            if is_valid_date(month, day, year):
                return f"{int(year):04}-{int(month):02}-{int(day):02}"
        except (ValueError, IndexError):
            pass

    raise ValueError("Invalid date format")

def is_valid_date(month, day, year):
    try:
        month = int(month)
        day = int(day)
        year = int(year)

        if month < 1 or month > 12:
            return False
        if day < 1 or day > 31:
            return False
        if year < 1:
            return False
        return True
    except ValueError:
        return False

if __name__ == "__main__":
    main()
