
#Formula celcius to farenheit
def celcius_to_farenheit(input_number):
    return round(((input_number * 1.8) + 32),1)


#Formular farenheit to celcius
def farenheit_to_celcius(input_number):
    return round(((input_number - 32) * 5/9), 1)


#handles incorrect input and responsible for releasing the output
def output_number(choice):
    while True:
        input_number = input("Enter a number: ")
 
        if not input_number.replace("-","").isdigit():
            print("Invalid input, please enter a number!")
        else:
            input_number = int(input_number)
            if choice == 'c':
                return print("The farenheit of", input_number,"°C is equivalent to", celcius_to_farenheit(int(input_number)),"°F")

            else:
                return print("The celcius of", input_number,"°F is equivalent to", farenheit_to_celcius(int(input_number)),"°C")



print("\nWelcome To Temperature Corverter\n")

while True:
    print("Which converter you want to use?\n")
    print("c - celcius to farenheit")
    print("f - farenheit to celcius\n")

    choice = input("Enter your input: ").lower()

    if choice != 'f' and choice != 'c':
        print("Invalid input, please try again\n")

    else:
       output_number(choice)
       break

print("\nThank you for using our program\n")
