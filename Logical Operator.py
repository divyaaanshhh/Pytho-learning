#Logical Operator = (or/and/not)
#                  or= at least one condition must be true
#                  and= both must be true
#                  not = inverts the condition (not FALSE , not TRUE)


######    OR     ###########
temp= float(input("Whats the temp for OR :"))
is_raining= False

if temp > 35 or temp < 0 or is_raining:
   print("Stay the Fuck inside your house!!")
else :
   print("Enjoy :)")

######## AND  ##########
temp= float(input("Whats the temp :"))
is_raining= False

if temp > 35 or temp < 0 or is_raining:
   print("Stay the Fuck inside your house!!")
else :
   print("Enjoy :)")


######### NOT ##########
temp = float (input("whats the temp :"))
its_sunny = True


