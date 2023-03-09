alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z']


def cypher(message, shift_number, command):

    output_message = ""
    shift_number = shift_number % 26

    for letter in message:
        if letter in alphabet:
            position = alphabet.index(letter)
            if command == 'encode':
                if position + shift_number > 25:
                    new_position = position + shift_number - 26
                else:
                    new_position = position + shift_number
                output_message += alphabet[new_position]
            else:
                new_position = position - shift_number
                output_message += alphabet[new_position]
        else:
            output_message += letter
    print(f"Here's the {command}d result: {output_message}")
