should_continue = True


def caeser(text, shift, alphabet, direction):

    encrypted = []
    shift %= 26

    if direction == "decode":
        shift *= -1

    for char in text:
        if char in alphabet:

            new_index = (alphabet.index(char)+shift) % 26
            encrypted.append(alphabet[new_index])
        else:
            encrypted.append(char)

    print(f'The Text is :{"".join(encrypted)} ')


while should_continue:
    alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m",
                "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]

    direction = input(
        "Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()

    shift = int(input("Enter the shift number:\n"))
    text = input("Type your message:\n").lower()
    caeser(text, shift, alphabet, direction)
    # print(f'The Text isss :{result}')

    repeat = input("want to go agin? say No to terminate:").lower()
    if repeat == "no":
        should_continue = False
        print("bye bye")
