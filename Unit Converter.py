class Converter:

    def __init__(self) -> None:
        pass

    def length(self):
        length_units = {
            "km": 1000,
            "dcm": 10,
            "m": 1,
            "cm": 0.01,
            "mm": 0.001,
            "microm": 0.000001,
            "nanom": 0.000000001
        }
        user_input = float(input("enter the number you want to convert :"))
        input_type = input("Enter the type of number you entered ( km / dcm / m / cm / mm / microm / nanom) :")
        output_type = input("Enter the type of number you want to convert to ( km / dcm / m / cm / mm / microm / nanom) :")
        result = user_input * length_units[input_type] / length_units[output_type]
        print(result)

    def mass(self):
        mass_units = {
            "kg": 1000,
            "pound": 453.592,
            "gr": 1,
            "mg": 0.001
        }
        user_input = float(input("enter the number you want to convert :"))
        input_type = input("Enter the type of number you entered ( kg / pound / gr / mg) :")
        output_type = input("Enter the type of number you want to convert to ( kg / pound / gr / mg) :")
        result = user_input * mass_units[input_type] / mass_units[output_type]
        print(result)

    def temperature(self):
        input_type = input("Enter the type of number you entered ( C / F / K) :")
        output_type = input("Enter the type of number you want to convert to ( C / F / K) :")
        user_input = float(input("enter the number you want to convert :"))

        if input_type == "C":
            celsius = user_input
        elif input_type == "F":
            celsius = (user_input - 32) * 5 / 9
        elif input_type == "K":
            celsius = user_input - 273.15
        else:
            print("wrong type entered")
            return

        if output_type == "C":
            result = celsius
        elif output_type == "F":
            result = celsius * 9 / 5 + 32
        elif output_type == "K":
            result = celsius + 273.15
        else:
            print("wrong type entered")
            return

        print(result)

    def area(self):
        area_units = {
            "km2": 1000000,
            "hectare": 10000,
            "m2": 1,
            "cm2": 0.0001,
            "mm2": 0.000001
        }
        user_input = float(input("enter the number you want to convert :"))
        input_type = input("Enter the type of number you entered ( km2 / hectare / m2 / cm2 / mm2) :")
        output_type = input("Enter the type of number you want to convert to ( km2 / hectare / m2 / cm2 / mm2) :")
        result = user_input * area_units[input_type] / area_units[output_type]
        print(result)

    def time(self):
        time_units = {
            "week": 604800,
            "day": 86400,
            "hour": 3600,
            "min": 60,
            "sec": 1
        }
        user_input = float(input("enter the number you want to convert :"))
        input_type = input("Enter the type of number you entered ( week / day / hour / min / sec) :")
        output_type = input("Enter the type of number you want to convert to ( week / day / hour / min / sec) :")
        result = user_input * time_units[input_type] / time_units[output_type]
        print(result)


def main():
    converter = Converter()

    while True:
        print("\nWhat do you want to convert?")
        print("1. Length")
        print("2. Mass")
        print("3. Temperature")
        print("4. Area")
        print("5. Time")
        print("6. Exit")

        choice = input("Enter your choice (1/2/3/4/5/6) :")

        if choice == "1":
            converter.length()
        elif choice == "2":
            converter.mass()
        elif choice == "3":
            converter.temperature()
        elif choice == "4":
            converter.area()
        elif choice == "5":
            converter.time()
        elif choice == "6":
            print("bye!")
            break
        else:
            print("wrong choice, try again")


if __name__ == "__main__":
    main()