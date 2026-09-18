#Compound intrest rate CALC

prin=0
amt=0
time=0

while prin <= 0:
   prin = float(input("Enter the principal amount: "))
   if prin < 0:
       print("Principal amount cannot be negative. Please enter a valid amount.")

while amt <= 0:
   amt = float(input("Enter the interest rate: "))
   if amt < 0:
       print("Amount cannot be negative. Please enter a valid amount.")

while time <= 0:
   time = float(input("Enter the time in years: "))
   if time < 0:
       print("Time cannot be negative. Please enter a valid amount.")
 
total = prin * (1 + (amt / 100)) ** time
print(f"The total amount after interest is: {total:.2f}")


            