# convert.py
#     A program to convert Celsius temps to Fahrenheit
# by: Susan Computewell

def main():
    #introduction
    print('this program converts kilometers to miles')
    #kilometers to miles converter
    kilometer = eval(input("What is the distance in kilometers? "))
    mile = 0.62 * kilometer
    print("The temperature is", mile, "degrees Fahrenheit.")

main()
