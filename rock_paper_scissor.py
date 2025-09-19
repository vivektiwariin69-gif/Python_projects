# rock , paper , scissor

import random
item_list = ["Rock" , "Paper" , "Scissor"]
user_input = input("Enter your move")
comp_choice = random.choice(item_list)
if user_input == comp_choice:
    print("Both chooses same: = match tie")
elif user_input == "Rock":
    if comp_choice == "Paper":
        print("Paper cover rock = comp win")
    else:
        print("Rock smashes Scissor = you win")
elif user_input == "Paper":
    if comp_choice == "Scissor":
        print("scissors cuts paper , comp win")
    else:
        print("paper cover rock , you win")       
elif user_input == "Scissor":
    if comp_choice == "Paper":
        print("scissor cuts paper  , you win")
    else:
        print( " rock smashes scissor , comp win")

        

   


           

