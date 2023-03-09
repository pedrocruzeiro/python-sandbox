import random

# random_integer = random.randint(1,10)
#
# random_float = random.random()
#
# final_random_number = random_integer + random_float
#
# print("{:.2f}".format(final_random_number))
#
# print("{:.2f}".format(random.random() * 10))

#names = input("Give me everybody's names, separated by a comma.").split(",")

# names = ["Angela", "Ben", "Jenny", "Michael", "Chloe"]
#
# len_names = len(names) - 1
#
# person_to_pay = names[random.randint(0, len_names)]
#
# person_to_pay_with_choice_function = random.choice(names)
#
# print(f"{person_to_pay} is going to pay the bill.")
#
# print(f"{person_to_pay_with_choice_function} is going to pay the bill. (Chosen by choice function)")

# Treasure challange

row1 = [" ", " ", " "]
row2 = [" ", " ", " "]
row3 = [" ", " ", " "]
treasure_map = [row1, row2, row3]

print(f"{row1}\n{row2}\n{row3}")
treasure_position = input("Where do you want to put the treasure? ")

# row = int(treasure_position) % 10
# column = int(int(treasure_position) / 10)

column = int(treasure_position[0])
row = int(treasure_position[1])

treasure_map[row-1][column-1] = 'X'
print(f"{row1}\n{row2}\n{row3}")