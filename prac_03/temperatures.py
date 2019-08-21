def main():
    print("""C - Convert Celsius to Fahrenheit\nF - Convert Fahrenheit to Celsius\nQ - Quit""")
    choice = input("").upper()
    while choice != "Q":
        if choice == "C":
            cel = float(input("Celsius: "))
            fah = convert_celsius_to_fahrenheit(cel)
            print("Result: {:.2f} F".format(fah))
        elif choice == "F":
            fah = float(input("Fahrenheit : "))
            cel = convert_fahrenheit_to_celsius(fah)
            print("Result: {:.2f} C".format(cel))
        else:
            print("Invalid option")
        print("""C - Convert Celsius to Fahrenheit\nF - Convert Fahrenheit to Celsius\nQ - Quit""")
        choice = input("> ").upper()
    print("Thank you.")


def convert_celsius_to_fahrenheit(celsius):
    return celsius * 9.0 / 5 + 32


def convert_fahrenheit_to_celsius(fahrenheit):
    return 5 / 9 * (fahrenheit - 32)


main()

