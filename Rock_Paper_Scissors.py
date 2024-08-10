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

choices = [rock,paper,scissors]

user_input = int(input("What do you choose? Type 0 for rock, 1 for paper or 2 for scissors\n"))

if  user_input < 0 or user_input >2:
    print("Invalid entry!")
    exit()

computer_choice = random.randint(0,2)

print(f"\nYour Choice:\n {choices[user_input]}")
print(f"Computer choice:\n {choices[computer_choice]}")

if user_input == 0 and computer_choice == 2 or \
    user_input == 1 and computer_choice == 0 or \
    user_input == 2 and computer_choice == 1:
    print("You Win!")
else:
    print("You lose!")
    