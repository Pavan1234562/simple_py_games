
import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
game_moves = [rock, paper, scissors]
player_choice = int(input("Choose 0 for Rock,1 for Paper,2 for scissors\n"))
if(player_choice>=3):
    print("Enter a valid no.\n 0 for rock\n 1 for paper\n 2 for scissor")
else:
    print(game_moves[player_choice])
    print("\n Computer Choose:")
    computer_choice = random.randint(0,2)
    print(f"\n {game_moves[computer_choice]}")
    if(player_choice == computer_choice):
        print("Draw")
    elif(player_choice == 0 and computer_choice ==1 or 
        player_choice == 1 and computer_choice == 2 or 
        player_choice == 2 and computer_choice == 0):
        print("Lose!! Try again")
    else:
        print("You Win!!")
