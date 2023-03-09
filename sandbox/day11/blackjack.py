import random
import math
import os
import art

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]


def calculate_score(card_list):
    current_score = int(math.fsum(card_list))

    if 11 in card_list and current_score > 21:
        card_list.remove(11)
        card_list.append(1)

    return int(math.fsum(card_list))


def deal_card():
    return int(random.choice(cards))


def compare_results(user_result, computer_result):
    if user_result == computer_result:
        return "It's a draw!"
    if user_result > 21 and computer_result > 21:
        return "It's a draw!"
    if user_result > 21:
        return "You went over it!! You lose!"
    if computer_result > 21:
        return "Computer bust!! You win!!"
    elif user_result > computer_result:
        return "You win!!"
    else:
        return "Computer cards are higher. You lose!"


should_continue = True


def play_blackjack():
    print(art.logo)

    user_cards = [deal_card(), deal_card()]
    computer_cards = [deal_card(), deal_card()]
    print(f"Your cards are {user_cards}. Current score is {calculate_score(user_cards)}.")
    print(f"Computer first cards is {computer_cards[0]}")
    while calculate_score(user_cards) < 21 and input("Type 'y' to get another card, type 'n' to pass: ") == 'y':
        user_cards.append(deal_card())
        print(f"    Your current hand is {user_cards}. Current score is {calculate_score(user_cards)}.")
    while calculate_score(computer_cards) < 17:
        print(f"    Computer's current hand is {computer_cards}. Current score is {calculate_score(computer_cards)}.")
        print("    will draw another card.")
        computer_cards.append(deal_card())
    print(f"\nComputer's final hand is {computer_cards}. Final score is {calculate_score(computer_cards)}.")
    print(f"User final hand is {user_cards}. Final score is {calculate_score(user_cards)}.\n")
    final_user_result = calculate_score(user_cards)
    final_computer_result = calculate_score(computer_cards)

    print(compare_results(final_user_result, final_computer_result))


while input("Do you want to play a game o Blackjack? Type 'y' or 'n': ") == 'y':
    os.system("clear")
    play_blackjack()
