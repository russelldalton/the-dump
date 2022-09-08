# convert.py
#     A program to convert Celsius temps to Fahrenheit
# by: Susan Computewell

def main():
    #introduction
    print('this program converts celsius to farenheit')
    #celsius to farenheit converter
    celsius = eval(input("What is the temperature in celsius? "))
    fahrenheit = 9/5 * celsius + 32
    print("The temperature is", fahrenheit, "degrees Fahrenheit.")

main()
