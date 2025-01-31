def main():
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")


def dollars_to_float(d):
    if "$" in d: 
        response = d.replace("$", "")
        return float(response.lstrip())


def percent_to_float(p):
    if "%" in p:
        response = p.replace("%", "")
        return float(response.lstrip()) / 100


main()