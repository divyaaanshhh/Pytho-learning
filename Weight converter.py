weight= float(input("Enter your weight?"))
unit = input("Is this in Kilogram or pound? (K/P)")
if   unit =="K":
    weight = weight*2.205
    unit = "pounds"
elif unit =="P":
   weight = weight/2.205   
   unit= "kgs"

print(f" your weight in {unit} is {round(weight ,2)}")


