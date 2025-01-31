def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(plate):
    if not (2 <= len(plate) <= 6):
        return False

    if not (plate[0].isalpha() and plate[1].isalpha()):
        return False

    if not plate.isalnum():
        return False

    has_seen_digit = False
    for char in plate:
        if char.isdigit():
            has_seen_digit = True
        elif has_seen_digit and char.isalpha():
            return False  # Letter after a number is invalid

    for char in plate:
        if char.isdigit():
            if char == '0':
                return False
            break  

    return True


main()
