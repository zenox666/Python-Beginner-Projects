import random
from hangman_words import word_list
from hangman_art import stages,logo

print(logo)
lives = 6

chosen_word = random.choice(word_list)
print(chosen_word)

placeholder = ""
for i in range(len(chosen_word)):
    placeholder += "_"
print(f"Word to guess: {placeholder}")


game_over = False
correct_letters = []
while not game_over:
    print(f"*****************{lives}/6 LIVES LEFT*******************")
    guess = input("Guess the letter: ").lower()
    display = ""

    if guess in correct_letters:
        print(f"You have already guessed '{guess}'")


    for letter in chosen_word:
        if guess == letter:
            display += letter
            correct_letters.append(letter)
        elif letter in correct_letters:
            display += letter
        else:
            display += "_"

    print(f"word to guess: {display}")

    if "_" not in display:
        game_over = True
        print("***************YOU WON*****************")
        
    if guess not in chosen_word:
        lives -=1
        print(f"You guessed '{guess}', that's not in the word.\nYou lose a life.")
        if lives == 0:
            game_over = True

            print("*****************YOU LOST******************")

    print(stages[lives])