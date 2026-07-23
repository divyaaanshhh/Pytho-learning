### CONDITIONAL EXPRESSION #######
#     Its a one line shorcut for the if-else statement  (ternary operator)
#     Print or assign one of two values based on a condition         
#     X if condition  else y 


# This tool tells if the number is positive /negative and odd or even 

num = float(input("Enter your Number :"))
print ("positive number" if num > 0 else "Negative number")
print("Even" if num % 2 == 0 else "Odd")
