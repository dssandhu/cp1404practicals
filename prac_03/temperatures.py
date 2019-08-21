menu = """C - Convert Celsius to Fahrenheit
    F - Convert Fahrenheit to Celsius
    Q - Quit"""

def main():
    print(menu)
    choice = input("").upper()
    while choice != "Q":
        if choice == "C":
            cel = float(input("Celsius: "))
            fah = conv_cel_to_fah(cel)
            print("Result: {:.2f} F".format(fah))
        elif choice == "F":
            fah = float(input("Fahrenheit : "))
            cel = conv_fah_to_cel(fah)
            print("Result: {:.2f} C".format(cel))
        else:
            print("Invalid option")
        print(menu)
        choice = input("> ").upper()
    print("Thank you.")


def conv_cel_to_fah(celsius):
    return celsius * 9.0 / 5 + 32


def conv_fah_to_cel(fahrenheit):
    return 5 / 9 * (fahrenheit - 32)


main()

