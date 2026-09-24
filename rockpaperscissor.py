
import random

option = ("rock","paper","scissor")
running =True
while running:
    user= None

    computer= random.choice(option) 
    while user not in option:
     user = input("Rock paper or scissor!?")


    print(f"Player:{user}")
    print(f"Computer:{computer}")

    


    if user == computer:
     print ("This is a Tie!!")
    elif user == "rock" and computer == "scissor":
     print("You WIN!!")
    elif user == "paper" and computer == "rock":
     print("You WON!!)")
    elif user == "scissor" and computer == "paper":
     print("You WIN!!)")
    else:
     print("You Lose")
if not input("Play again?(y/n):").lower() == "y":
     running=False

print("Thanks for playing :)")







