import random
import os
import hangman_art
import hangman_words

end_of_game = False
lives = 6
chosen_word = random.choice(hangman_words.word_list)

guess_word = []
check_letter_list = []

for letter in chosen_word:
    guess_word.append("_")

print(hangman_art.logo)
print(f"You have {lives} lives!!")

while not end_of_game:
    check_letter = input("Please provide letter to check ").lower()
    os.system('clear')
    if check_letter in check_letter_list:
        print(f"Letter {check_letter} already guessed.")
        print(guess_word)
        print(hangman_art.stages[lives])
    else:
        check_letter_list.append(check_letter)
        letter_miss = True
        for position in range(len(chosen_word)):
            letter = chosen_word[position]
            if letter == check_letter:
                guess_word[position] = letter
                letter_miss = False
        print(guess_word)
        if letter_miss:
            lives -= 1
            print(f"You guessed {check_letter}. That letter is not in the word. You have {lives} lives.")

        else:
            print(f"You guessed {check_letter}. That letter is in the word. Please continue.")
        print(hangman_art.stages[lives])
        if lives == 0:
            print("You lose!!")
            print(f"The word was {chosen_word}.")
            end_of_game = True
        if "_" not in guess_word:
            print("You win!!")
            end_of_game = True




