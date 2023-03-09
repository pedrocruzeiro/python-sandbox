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

user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper, 2 for Scissors. "))

plays_list = [rock,paper,scissors]

pc_choice = random.randint(0, 2)

if user_choice < 0 or user_choice > 2:
    print("You selected an invalid number, you lose!")
else:
    print("You choose:")
    print(plays_list[user_choice])
    print("Computer choose:")
    print(plays_list[pc_choice])

    if user_choice == 0 and pc_choice == 2:
        print("You win!")
    elif user_choice == 1 and pc_choice == 0:
        print("You win!")
    elif user_choice == 2 and pc_choice == 1:
        print("You win!")
    elif pc_choice == user_choice:
        print("It's a draw!")
    else:
        print("You loose!")