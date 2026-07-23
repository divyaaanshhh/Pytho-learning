#Addition
friends = 0
#friends = friends + 2
#This is a long way now short one
friends +=2
print(friends)


#Substraction
Dushman= 2
Dushman -= 3
print(Dushman)
#its same as addition


#Multiplication
finalchaos= Dushman*friends
print(finalchaos)


#just use the operation before the final equal sign


#Division
division = 40
division /= 10
print(division)

#Power
division **=2
print(division)

# Modulo Opertaion
remainder = division % 50
print(remainder )
#this function can be used to find if the number is odd or even like if i divide it by 2 modulo,if i get 0 its even
#and if i get 1 its odd

#NOW
x=3.4
y=-5
z=9

#ROUND function
finalx =round(x)
print(finalx)


#ABSOLUTE VALUE
#it is the distance from 0 in the axis
finaly =abs(y)
print(finaly)



 #Power function
power = pow(4, 3)
print(power)

#MAX And MIN function
#it is used to find the max and min value

finaly = max(x,y,z)
finalx = min(x,y,z)

print(finaly)
print(finalx)


#MATHS
import math
print(math.pi)
print(math.e)
print(math.sqrt(z))
print(math.ceil(x)) #rounds off to the bigger number
print(math.floor(x))#rounds off to the smaller number

##NOW LETS USE SOME FORMULAS
#LETS CALCULATE THE CIRCUMFERENCE OF THE CIRCLE
radius = float(input("Enter the radius: "))
finalradius = (2*math.pi*radius)
print(f"The circumference of the circle is {finalradius}")
print(f"Rounded off to Aprrox{round(radius, 2)}")
area = math.pi * pow(radius,  2)
print(f"The area of the circle is {area}")
print(f"Rounded off to approx{round(area, 2)}")


#Calculate Hypotenuse of Triangle

a= float(input("Enter Side A : "))
b= float(input("Enter Side B : "))
c= math.sqrt(pow(a,  2) + pow(b, 2))

print(f"The Hypotenuse is {c}")






