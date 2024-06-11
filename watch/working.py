import re
import sys

def main():
    print(convert(input("Hours: ")))

def convert(s):
    # Définir les motifs pour les formats d'heure acceptés
    pattern = r'(\d{1,2}(:\d{2})?) (AM|PM) to (\d{1,2}(:\d{2})?) (AM|PM)'

    match = re.fullmatch(pattern, s)
    if not match:
        raise ValueError("Invalid time format")

    # Extraire les heures et les périodes (AM/PM)
    time1, _, period1, time2, _, period2 = match.groups()

    # Convertir les heures
    try:
        time1_24 = convert_to_24_hour_format(time1, period1)
        time2_24 = convert_to_24_hour_format(time2, period2)
    except ValueError as e:
        raise ValueError("Invalid time value") from e

    return f"{time1_24} to {time2_24}"

def convert_to_24_hour_format(time, period):
    if ':' in time:
        hours, minutes = map(int, time.split(':'))
    else:
        hours, minutes = int(time), 0

    if hours > 12 or hours < 1 or minutes >= 60 or minutes < 0:
        raise ValueError("Invalid time value")

    if period == "AM":
        if hours == 12:
            hours = 0
    elif period == "PM":
        if hours != 12:
            hours += 12

    return f"{hours:02}:{minutes:02}"

if __name__ == "__main__":
    main()
