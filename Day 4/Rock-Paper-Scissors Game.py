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
user_choice = int(input("Rock, Paper, Scissors. Please choose - 0 for Rock, 1 for Paper, 2 for Scissors : "))
game_image = [rock, paper, scissors]
computer_choice = random.randint(0, 2)

if user_choice == 0:
    print(f"You chooses:\n{rock}")
    print(f"Computer chooses:\n{game_image[computer_choice]}")
    if computer_choice == 0:
        print("Draw!")
    elif computer_choice == 1:
        print("Computer Win!")
    elif computer_choice == 2:
        print("You win!")
elif user_choice == 1:
    print(f"You chooses:\n{paper}")
    print(f"Computer chooses:\n{game_image[computer_choice]}")
    if computer_choice == 1:
        print("Draw!")
    elif computer_choice == 0:
        print("You Win!")
    elif computer_choice == 2:
        print("Computer Win!")
elif user_choice == 2:
    print(f"You chooses:\n{scissors}")
    print(f"Computer chooses:\n{game_image[computer_choice]}")
    if computer_choice == 2:
        print("Draw!")
    elif computer_choice == 1:
        print("You Win!")
    elif computer_choice == 0:
        print("Computer Win!")
