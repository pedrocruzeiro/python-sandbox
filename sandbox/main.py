# height = float(input("enter your height in m: "))
# weight = float(input("enter your weight in kg: "))

# BMI = int(weight / height ** 2)
# print(BMI)

# print(8 / 3)

# print(round(8 / 3, 2))

# time of life remaining

# current_age = int(input("what is you current age: "))
#
# years_remaining = 90 - current_age
#
# days = years_remaining * 365
# weeks = years_remaining * 52
# months = years_remaining * 12
#
# print(f"you have {days} days, {weeks} weeks and {months} months left.")


# Tip Calculator

# print("Welcome to Tip Calculator")
# bill = float(input("What was the total bill? $"))
# tip = int(input("What percentage tip would you like to give? 10, 12, 15? "))
# split = int(input("How many people would you like to split? "))
#
# bill_with_tip = tip / 100 * bill + bill
#
# bill_per_person = bill_with_tip / split
#
# final_amount = "{:.2f}".format(bill_per_person)
#
# print(f"Each person should pay: ${final_amount}")

dice =["⚀","⚁","⚂","⚃","⚄","⚅"]

# Even or odd

# number = int(input("Which number do you want to check? "))

# if number % 2 == 0:
#    print("The number is even.")
# else:
#    print("The number is odd.")


# BMI calculator 2.0

# height = float(input("enter your height in m: "))
# weight = float(input("enter your weight in kg: "))
#
# BMI = int(weight / height ** 2)
#
# if BMI < 18.5:
#     print(f"Your BMI is {BMI}, you are underweight.")
# elif BMI < 25:
#     print(f"Your BMI is {BMI}, you have normal weight.")
# elif BMI < 30:
#     print(f"Your BMI is {BMI}, you are overweight.")
# elif BMI < 35:
#     print(f"Your BMI is {BMI}, you are obese.")
# else:
#     print(f"Your BMI is {BMI}, you are clinically obese.")


# Leap Year

# year = int(input("Which year do you want to check?"))
#
# if year % 4 == 0:
#     if year % 100 == 0:
#         if year % 400 == 0:
#             print("leap")
#         else:
#             print("no leap")
#     else:
#         print("leap")
# else:
#     print("no leap")

# Pizza delivery
# print("Welcome to Python Pizza Deliveries!")
# size = input("What size do you want the pizza? (S, M or L) ")
# add_pepperoni = input("Do you want pepperoni? (Y or N) ")
# extra_cheese = input("Do you want extra cheese? (Y or N) ")
#
# bill = 0
#
# if size == "S":
#     bill += 15
# elif size == "M":
#     bill += 20
# else:
#     bill += 25
#
# if add_pepperoni == "Y":
#     if size == "S":
#         bill += 2
#     else:
#         bill += 3
#
# if extra_cheese == "Y":
#     bill += 1
#
# print(f"Your final bill is ${bill}.")

# Love calculator
print("Welcome to the Love Calculator!\n")
print('''\n                    .-.  .-.
                   (   \/   )
          .-.  .-.  \      .-.  .-.
         (   \/   )  \    (   \/   )
          \     .-.  .-. / \      /
           \   (   \/  .-.  .-.  /
        .-. \.-.\     (   \/   )/
       (   \/   )\    /\      //
        \      /  \  /  \    /
         \    /    \/    \  /
          \  /            \/
           \/
\n''')
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")

combined_string = name1.lower() + name2.lower()

name1_score = str(combined_string.count("t") +
                  combined_string.count("r") +
                  combined_string.count("u") +
                  combined_string.count("e"))

name2_score = str(combined_string.count("l") +
                  combined_string.count("o") +
                  combined_string.count("v") +
                  combined_string.count("e"))

final_score = int(name1_score + name2_score)

if final_score < 10 or final_score > 90:
    print(f"Your score is {final_score}, you go together like coke and mentos.")
if final_score >= 40 or final_score <= 50:
    print(f"Your score is {final_score}, you are alright together.")
else:
    print(f"your score is {final_score}.")
