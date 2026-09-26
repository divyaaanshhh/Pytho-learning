#-----------FUNCTIONS------------------------
# a block of reusable code
# use this () after the function name ot invoke it 

def happy_birthday(name,age):
 print(f"Happy birthday to {name}!")
 print(f"unlocked new level of being and unc :)you are {age}now")
 print("Happy birthday to you!")
 print()

happy_birthday("Ani",20)
happy_birthday("divyansh",26)



def display_invoice(username, due_date, amount):
 print(f"Hello{username}")
 print(f"Your final due date is {due_date}")
 print(f"Your due amount is {amount}")
 print()

display_invoice("Ani","9999999","31/31/31")

#----------------RETURN------------------------
# statement used to end a function and send a result back to the caller 

def add(x,y):
 z=x+y
 return z

def substract (x,y):
 z=x-y
 return z

def multiply(x,y):
 z=x*y
 return z

def divide(x,y):
 z=x/y
 return z

print(add(1,2))
print(multiply(1,2))
print(substract(1,2))
print(divide(1,2))


def create_name(first,last):
 first = first.capitalize()
 last = last.capitalize()
 return first+" "+last


full_name = create_name("Divyansh","Rajput")
full_name2 = create_name("spongebob","sqarepants")


print(full_name2)
print(full_name)




 






 