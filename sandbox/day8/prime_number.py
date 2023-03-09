def prime_number_checker(number):
    is_prime = True
    for n in range(2, number):
        if number % n == 0:
            is_prime = False
    if number == 1:
        print("Number 1 is not a prime number. Prime numbers are greater than 1.")
    elif is_prime is True:
        print(f"Number {number} is a prime number.")
    else:
        print(f"Number {number} is not a prime number. It's a composite number.")


# check_number = int(input("Provide the number to check: "))

# prime_number_checker(number=check_number)

for i in range(1, 25):
    prime_number_checker(number=i)
