###finally we are going to create a calculator using python

operator = input("Enter your operator? (+ - * /): ")
num1 = float(input("Your first number?: "))
num2 = float(input("Your second number?: "))
if operator == "+":
    print(round (num1 + num2, 2))
elif operator == "-":
    print(round(num1 - num2, 2))
elif operator == "*":
    print(round(num1 * num2, 2))
elif operator == "/":
    print(round(num1 / num2, 2))


