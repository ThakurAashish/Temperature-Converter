def celcius_to_farenheit(celcius):
    fahrenheit = (celcius * 9/5) + 32
    return fahrenheit

def farhrenheit_to_Celsius(farhrenheit):
    Celsius = (farhrenheit - 32)*5/9
    return Celsius

celsius_temperature = float(input("Enter temperature in Celsius: "))
farhrenheit_temp = float(input(" Enter the temp in farhrenheit  :"))

converted_temperature = celcius_to_farenheit(celsius_temperature)
converted__temperature = farhrenheit_to_Celsius(farhrenheit_temp)

print("Converted temperature in Fahrenheit:", converted_temperature)
print("Converted temperature in celsius:", converted__temperature)