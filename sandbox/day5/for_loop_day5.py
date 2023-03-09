# Student average height - input: 156 178 165 171 187
# student_heights = input("Input a list of student heights ").split()
#
# for n in range(0, len(student_heights)):
#     student_heights[n] = int(student_heights[n])
# print(student_heights)
#
# total_count = sum(student_heights)
#
# average_height = round(total_count / len(student_heights))
#
# print(f"Average height is {average_height}.")

# Students highest score
# student_scores = input("Input a list of student scores ").split()
# #
# for n in range(0, len(student_scores)):
#     student_scores[n] = int(student_scores[n])
# print(student_scores)
#
# student_higher_score = 0
#
# for score in student_scores:
#     if score > student_higher_score:
#         student_higher_score = score
# print(max(student_scores))
# print(f"Students high score is: {student_higher_score}.")


# for range

# total = 0
# for number in range(0, 101, 2):
#     total += number
# print(total)

# fizz buzz challenge

for number in range(1, 101):
    if number % 3 == 0 and number % 5 == 0:
        print("FizzBuzz")
    elif number % 3 == 0:
        print("Fizz")
    elif number % 5 == 0:
        print("Buzz")
    else:
        print(number)