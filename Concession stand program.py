#-------------------CONCESSION STAND PROGRAM------------------------

menu={"pizza":10.99,
      "burger":4.99,
      "popcorn":6.99,
      "fries":3.99,
      "soda":2.99,
      "lemonade":2.99}

cart=[]
total=0
print("---------------MENU----------------------")
for key, value in menu.items():
    print(f"{key:10}: ${value:.2f}")

print("-----------------------------------------")


while True:
    food=input("Type the item you want to order! (use Q to quit)").lower()
    if food=="q":
        break
    elif menu.get(food) is not None:
        cart.append(food)



print("--YOUR CART ITEMS ARE -")
print(cart)

for food in cart:
    total += menu.get(food)
    print(food,end=" ")
print()
print(f"Total is: ${total:.2f}")





















    
