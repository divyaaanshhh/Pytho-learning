fruits=["apple" ,"watermelon" ,"orange", "kiwi"]
vegetables =["potato", "onion", "tomato", "carrot"]
meats =["chicken", "fish", "mutton","prawns"]

groceries= [fruits,vegetables,meats]

print(groceries[0][2])  # prints the third item in the first list (fruits)
print(groceries[1][0])  # prints the third item in the second list (vegetables)
print(groceries[2])  # prints the third item in the third list (meats)


numpad=((1,2,3),
        (4,5,6),
        (7,8,9),
        ('*',0,'#'))

for row in numpad:
    for num in row:
        print(num, end=" ")
    print()



