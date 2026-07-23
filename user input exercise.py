# validate user input exercise
# 1. username is no more than 12 characters
# 2. username must not contain spaces
# 3. username must not contain digits


name =input("what your name? :")

result = len(name)

if result < 12:
   print(f"Welcome {name}")
elif not name.find(" ") == -1:
   print("Your username cant contain spaces")
else:
   print("the username should be less than 12 digits")



