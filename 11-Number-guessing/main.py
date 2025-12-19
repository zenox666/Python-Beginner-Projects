import random
import art


def difficulty(choice):

    if choice =="easy":
        attempts = 10
    elif choice =="hard":
        attempts = 5
    else:
        return 0
    return attempts



def compare(g_choice,c_choice):

    if g_choice == c_choice:
        return f"you got it! The answer was {g_choice}"
    elif g_choice > c_choice:
        return f"Too High "
    else:  #g_choice < c_choice
        return f"Too Low "


def guess_game():

    print(art.logo)
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    comp_choice = random.randint(1, 100)


    chosen_diff = input("Choose a difficulty.Type 'easy' or 'hard': ").lower()
    lives = difficulty(chosen_diff)

    while lives != 0:
        print(f"You have {lives} attempts remaining. ")

        guess = int(input("Guess a number: "))
        situation=compare(guess, comp_choice)

        if guess != comp_choice:
            lives -=1
            if lives == 0:
                print("You ran out of lives.")
                return

            print(situation)
            print("Guess again.")

        else:
            print(situation)
            return

while input("YOU WANT TO PLAY THE GUESS GAME.TYPE 'YES' OR 'NO': ").upper()=='YES':
    print("\n"*10)
    guess_game()





# import random
#
#
# number = random.randint(0, 100)
#
#
# def attempts():
#     level = input("select a level of difficulty: (easy) or (hard)")
#     if level == "easy":
#         return 10
#     else:
#         return 5
#
#
# def game():
#     for n in range(0, attempts()):
#         user_num = int(input("guess"))
#         if user_num > number:
#             print("high")
#         elif user_num < number:
#             print("low")
#         elif user_num == number:
#             print("jack")
#             attempts()
#
#
# game()
