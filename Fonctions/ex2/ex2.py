import convTemp

celcius = float(input("Veuillez entrer la temperature en celsius: "))
farenheit = convTemp.convCelToFar(celcius)
kelvin = convTemp.convCelToKelv(celcius)
print(f"{celcius:.2f}° en Celsius correspond à {farenheit:.2f}° en Farenheit et {kelvin:.2f}° en Kelvin")
