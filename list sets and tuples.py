# colection  = single "variable " used to store mutiple vaules 
# sets = {}unordered or inmutable, but Add/ remove OK. NO Duplicates 
#List =  []ordered and mutable . Duplicates works 
#tuples = ()

fruit= ["apples", "oranges" , "banana", "kiwi", "mango", "grapes"]

print(fruit)
print (fruit[0])
print (fruit[1])
print (fruit[2])
print (fruit[3])
print (fruit[4])
print (fruit[5])

#print(dir(fruit))
print(len(fruit))  # THIS TELLS THE TOATAL NUMBER OF ELEMENTS IN THE TUPLE


print("apples" in fruit)  # THIS TELLS IF THE ELEMENT IS PRESENT IN THE TUPLE OR NOT

fruit.append("papaya")  # THIS ADDS THE ELEMENT TO THE List

fruit.remove("kiwi")  # THIS REMOVES THE ELEMENT FROM THE List

fruit.insert(2, "kiwi")  # THIS ADDS THE ELEMENT TO THE List AT THE SPECIFIED INDEX 
#                           AND REPLACES IT WITH THE ELEMENT PRESENT AT THAT INDEX

fruit.sort()  # THIS SORTS THE ELEMENTS IN THE List IN ALPHABETICAL ORDER   

fruit.reverse()  # THIS REVERSES THE ELEMENTS IN THE List

fruit.pop()  # THIS REMOVES THE LAST ELEMENT FROM THE List

print(fruit.count  ("kiwi"))  # THIS TELLS THE NUMBER OF TIMES THE ELEMENT IS PRESENT 
#                                IN THE List






