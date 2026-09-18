#           NESTED LOOP
# A loop within another loop is called a nested loop. 
# The "inner loop" will be executed one time for each iteration of the "outer loop":


rows =int(input("Enter the number of rows: "))
coloums=int(input("Enter the number of coloums: "))
symbol= input("Enter the symbol you want to use: ")


for x in range(3):
    for y in range(3):
        print(symbol, end="")
    print()

    
