#---------------PYTHON QUIZ GAME------------------
questions=("what the best song of weekend? ",
           "which is the most abundent gas on earth?" ,
           "How much protien does an average egg has?", 
           "which is the longest bone in human body?", 
           "which is the strongest muscle in human body?")

options= (("A.House of ballon","B. One of the Girls","C.The Abyss","D.The Hills",), 
         ("A.O","B. N","C.S","D.He"),
         ("A.5","B.6","C.7","D.8"),
         ("A.spine","B.finger","C.femer","D.fibula"),
         ("A.cardiac","B.buttock","C.calf","D.jaw"))

answers=("C","B","B","C","D")

guesses=[]

score =0

question_num =0

for question in questions:
      print("-----------------------------------")
      print(question)
      for option in options[question_num]:
            print(option)


      guess =input("Enter (A, B, C, D)").upper()
      guesses.append(guess)
      if guess == answers[question_num]:
           score +=1
           print("CORRECT!")
      else:
           print("Incorrect")
           print:(f"The correct answer is {answers[question_num]}")

          
       

      question_num += 1



         


