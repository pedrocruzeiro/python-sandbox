import random

import art

print(art.logo)

print("Welcome to the Number Guessing Game!")

levels = {
    "easy": 10,
    "hard": 5,
}

print("I'm thinking of a number between 1 and 100.")

random_number = random.randint(0, 100)

level_of_difficulty = input("Choose a difficulty level. Type 'easy' or 'hard': ").lower()


def game():
    if level_of_difficulty not in levels:
        return f"{level_of_difficulty} difficulty doesn't exist."
    else:
        turns = levels[level_of_difficulty]
        for i in range(1, turns + 1):
            guess_number = int(input("Make a guess: "))
            if guess_number == random_number:
                return f"You win. Number was {random_number}."
            elif guess_number > random_number:
                print("Too high")
            else:
                print("Too low")
            print(f"You have {turns - i} attempts to guess the number.")

        return f"You lose. Number was {random_number}."


print(game())
