
def main():
    time = input("Enter the time (in 24-hour format, ex 7:00 or 13:45): ").strip()
    time_in_hours = convert(time)

    if time_in_hours is not None:
        if 7.0 <= time_in_hours <= 8.0:
            print("breakfast time")
        elif 12.0 <= time_in_hours <= 13.0:
            print("lunch time")
        elif 18.0 <= time_in_hours <= 19.0:
            print("dinner time")

def convert(time):
    try:
        hours, minutes = time.split(":")
        hours = int(hours)
        minutes = int(minutes)

        # Convertir en heures flottantes
        time_in_hours = hours + minutes / 60.0

        return time_in_hours
    except ValueError:
        return None

if __name__ == "__main__":
    main()

