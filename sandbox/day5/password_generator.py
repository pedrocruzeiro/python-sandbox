import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
           'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
           'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

# Hard Level - Order of characters randomised:
# e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P

# list_of_chars = [letters, numbers, symbols]
#
# total_chars = nr_letters + nr_symbols + nr_numbers
#
# generated_password = ""
# for char in range(1, total_chars + 1):
#     random_char_list = random.choice(list_of_chars)
#     generated_password += random.choice(random_char_list)
#
# print(generated_password)

# Hard Level - Other possible solution

generated_password_list = []

for char in range(1, nr_letters + 1):
    generated_password_list.append(random.choice(letters))

for char in range(1, nr_symbols + 1):
    generated_password_list.append(random.choice(symbols))

for char in range(1, nr_numbers + 1):
    generated_password_list.append(random.choice(str(nr_numbers)))

random.shuffle(generated_password_list)

generated_password = ""
for char in generated_password_list:
    generated_password += char

print(f"Random password is {generated_password}.")
