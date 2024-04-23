class TemperatureConverter:
    @staticmethod
    def celsius_to_fahrenheit(celsius):
        return (celsius * 9/5) + 32

    @staticmethod
    def fahrenheit_to_celsius(fahrenheit):
        return (fahrenheit - 32) * 5/9

    @staticmethod
    def celsius_to_kelvin(celsius):
        return celsius + 273.15

    @staticmethod
    def kelvin_to_celsius(kelvin):
        return kelvin - 273.15

    @staticmethod
    def fahrenheit_to_kelvin(fahrenheit):
        return (fahrenheit - 32) * 5/9 + 273.15

    @staticmethod
    def kelvin_to_fahrenheit(kelvin):
        return (kelvin - 273.15) * 9/5 + 32
    

def main():
    while True:
        print("\nTemperature Converter Options:")
        print("1. Convert Celsius to Fahrenheit")
        print("2. Convert Fahrenheit to Celsius")
        print("3. Convert Celsius to Kelvin")
        print("4. Convert Kelvin to Celsius")
        print("5. Convert Fahrenheit to Kelvin")
        print("6. Convert Kelvin to Fahrenheit")
        print("7. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            celsius = float(input("Enter temperature in Celsius: "))
            print(f"{celsius} Celsius = {TemperatureConverter.celsius_to_fahrenheit(celsius)} Fahrenheit")
        elif choice == '2':
            fahrenheit = float(input("Enter temperature in Fahrenheit: "))
            print(f"{fahrenheit} Fahrenheit = {TemperatureConverter.fahrenheit_to_celsius(fahrenheit)} Celsius")
        elif choice == '3':
            celsius = float(input("Enter temperature in Celsius: "))
            print(f"{celsius} Celsius = {TemperatureConverter.celsius_to_kelvin(celsius)} Kelvin")
        elif choice == '4':
            kelvin = float(input("Enter temperature in Kelvin: "))
            print(f"{kelvin} Kelvin = {TemperatureConverter.kelvin_to_celsius(kelvin)} Celsius")
        elif choice == '5':
            fahrenheit = float(input("Enter temperature in Fahrenheit: "))
            print(f"{fahrenheit} Fahrenheit = {TemperatureConverter.fahrenheit_to_kelvin(fahrenheit)} Kelvin")
        elif choice == '6':
            kelvin = float(input("Enter temperature in Kelvin: "))
            print(f"{kelvin} Kelvin = {TemperatureConverter.kelvin_to_fahrenheit(kelvin)} Fahrenheit")
        elif choice == '7':
            print("Exiting...")
            break
        else:
            print("Invalid choice! Please try again.")

if __name__ == "__main__":
    main()

