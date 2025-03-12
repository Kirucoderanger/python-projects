#Author Kirubel Mekonen Lemu 
#windchill calculator

def windchill_calculator(temprature):
        wind_chill = 35.74 + (0.6215 * temprature) - (35.75 * (i**0.16)) + (0.4275 * temprature) * (i**0.16)
        return wind_chill
def celsius_converter(temprature):
    fahrenheit = (temprature * (9/5)) + 32
    return fahrenheit
temprature = float(input ("Enter the temprature you need to calculate the WINDCHILL: "))
choise = input("Fahrenheit or Celsius (F/C)? ")
if choise.lower() == "f":
    for i in range(5,61,5):
        print (f"At temperature {temprature:.1f}F, and wind speed {i} mph, the windchill is: {windchill_calculator(temprature):.2f}F")
elif choise.lower() == "c":
    converted = celsius_converter(temprature)
    for i in range(5,61,5):
        print (f"At temperature {converted:.1f}F, and wind speed {i} mph, the windchill is: {windchill_calculator(converted):.2f}F")
else:
    print ("you enterd a wrong value")
    

    


