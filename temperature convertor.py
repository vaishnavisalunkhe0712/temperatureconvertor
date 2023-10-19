# python program converts temperature between degree and celsius

#input for the temperature

Temperature= input("Input the  temperature you like to convert? (e.g., 40F, 100C etc.) : ")
degree = int(Temperature[:-1])
i_convention = Temperature[-1]

if i_convention.upper() == "C":
  result = int((9 * degree) / 5 + 32)
  o_convention = "Fahrenheit"
elif i_convention.upper() == "F":
  result = int((degree - 32) * 5 / 9)
  o_convention = "Celsius"
else:
  print("Input proper convention.")
  quit()
print("The temperature in",o_convention, "is", result, "degrees.")

