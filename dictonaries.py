# ------------DICTIONARY-------------
#collection of {key values} pairs 
#ordered and changable but no duplicate 


capitals= {"USA": "Washington D.C",
           "India": "Delhi",
           "China":"bejing",
           "Russia":"Moscow"}


#print(dir(capitals))
print(capitals.get("USA"))
if capitals.get("japan"):
    print("that capital exists")
else :
    print("That capital doesnt exits")


capitals.update({"India":"Bejing"})      # USED TO UPDATE AN ITEM IN THE lIST
print(capitals)

capitals.pop("India")           #USED TO REMOVE ANY ITEM FROM THE LIST
print(capitals)

capitals.popitem()      #YOU DONT NEED ANY INSERT ANY KEY IT WILL REMOVE THE LAST ITEM THAT WAS ADDED
print(capitals)

    #capitals.clear()                            #IT CLEANS THE WHOLE DICTIONARY



#----------------KEYS---------------------
# It is used to store,locate and access specific values

keys=capitals.keys
for keys in capitals:
   print(keys)

values= capitals.values()
for value in capitals.values():
    print(value)
        










