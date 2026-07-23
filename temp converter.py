temp = float(input("whats the temprature :"))

unit = input("is this temperature in celsius or Fahrenheit:(C/F)")
if unit == "C":
 temp = round((9*temp  /5+32),1)
 print(f"The temp in farenhite is {temp}")
elif unit == "F":
 temp = ((temp -32) * 5/9 )
 print(f"The temp in celsuis is {temp} ")