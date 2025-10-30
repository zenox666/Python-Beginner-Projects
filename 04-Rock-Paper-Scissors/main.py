import  random
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
choice = [rock, paper, scissors]
user = int(input("What do chose?Type 0 for rock, 1 for paper, 2 for scissors: \n"))
print(choice[user])
computer_choice = random.randint(0,2)
print("Computer chose:")
print(choice[computer_choice])

if user > 2:
    print("That's dumb")
elif user == computer_choice:
    print("It's a draw")
elif user == computer_choice + 1:
    print("You won!!")
elif user + 2 == computer_choice:
    print("You won!!")
else:
    print("You lost")
