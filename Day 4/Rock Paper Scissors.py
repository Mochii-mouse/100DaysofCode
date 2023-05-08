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

symbols = [rock, paper, scissors]

action = int(
    input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors?\n"))
if action < 0 or action > 2:
    print("Invalid number, you lose!")
else:
    print(symbols[action])
    pcmove = random.randint(0, 2)
    print("Computer chose:\n" + symbols[pcmove])

    if action == 0 and pcmove == 2:
        print("You won!")
    elif pcmove == 0 and action == 2:
        print("You lose!")
    elif pcmove > action:
        print("You lose!")
    elif action > pcmove and action <= 2:
        print("You won!")
    elif pcmove == action:
        print("You drew!")
    else:
        print("You typed an invalid number, you lose!")
