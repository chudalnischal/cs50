def main():
    user_input = input("What time is it? ").strip()
    hours = convert(user_input)

    if 7 <= hours <= 8:
        print("Breakfast Time")
    elif 12 <= hours <= 13:
        print("Lunch Time")
    elif 18 <= hours <= 19:
        print("Dinner Time")
    else:
        pass

def convert(user_input):
    time = user_input.split(":")
    hours = int(time[0])
    minutes = int(time[1])
    total_hours = hours + (minutes / 60)
    return total_hours

if __name__ == "__main__":
    main()
