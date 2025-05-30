"""
WORK FLOW OF THE PROGRAM:
1 - Input from user (Rock , paper, scissor)
2  - computer choice Randomly(we use random module)
3 - Compare the choices and decide the winner
4 - Display the winner

cases:
A - Rock 
Rock = Rock = tie
Rock > scissor = Rock wins
Rock < paper = paper wins

B - paper
paper = paper = tie
paper > rock = paper wins
paper < scissor = scissor win 

C - scissor
scissor = scissor = tie
scissor > paper = scissor win
scissor < rock = rock win

"""
import random

item_list = ["rock", "paper", "scissor"]

user_choice = input("Enter your move  = rock , paper, scissor: ")
computer_choice = random.choice(item_list)
print(f"User choice  = {user_choice} , computer choice = {computer_choice}")

if user_choice == computer_choice:
  print("Both chosse same, it's a tie")

elif user_choice == "rock":
  if computer_choice == "paper":
    print("Paper cover rock = computer wins")
  else:
    print("Rock smashes scissor = You win")

elif user_choice == "paper":
  if computer_choice == "scissor":
    print("Scissor cuts paper = computer wins")
  else:
    print("Paper covers rock = You win")

elif user_choice == "scissor":
  if computer_choice == "rock":
    print("Rock smashes scissor = computer wins")

  else:
    print("Scissor cuts paper = You win")

#end of the program
