def main():
    print("This program converts Fahrenheit temps to Celsius")

    fahrenheit = eval(input("What is the Fahrenheit temperature?"))
    celsius = (fahrenheit - 32) / 1.8
    print("The temperature is", celsius, "degrees Celsius")


main()