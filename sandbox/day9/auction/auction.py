import art
import os

print(art.logo)
print("Welcome to the secret auction program!")

should_exit = False

bid_dict = {}

while should_exit is False:
    name = input("What is your name?: ")
    bid = int(input("What is your bid?: $"))
    bid_dict[name] = bid
    exit_command = ""
    while exit_command not in ('yes', 'no'):
        exit_command = input("Are there other bidders? Type 'yes' or 'no'\n").lower()
        if exit_command == 'no':
            should_exit = True
    os.system('clear')

higher_bid_value = 0
higher_bid_name = ""
for key in bid_dict:
    if bid_dict[key] > higher_bid_value:
        higher_bid_name = key
        higher_bid_value = bid_dict[key]

print(f"The winner is {higher_bid_name} with a bid of ${higher_bid_value}.")