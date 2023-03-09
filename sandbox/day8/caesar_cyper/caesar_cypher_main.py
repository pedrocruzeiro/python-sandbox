import caesar_cyper_logo
import caesar_cypher_functions

print(caesar_cyper_logo.logo)

should_exit = False

while should_exit is False:
    command = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()

    if command in ('encode', 'decode'):
        message = input("Type your message:\n").lower()
        shift_number = int(input("Type the shift number:\n"))
        caesar_cypher_functions.cypher(message, shift_number, command)
    else:
        print("Unknown command.")
    exit_command = ""
    while exit_command not in ('yes', 'no'):
        exit_command = input("Type 'yes' if you want to go again, type 'no' if you want to exit:\n").lower()
        if exit_command == 'no':
            should_exit = True
            print(caesar_cyper_logo.goodbye)
