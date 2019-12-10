# Name: Zackary Nichol
# Section: 9:30 CIS 115
# Project: ROT13 Cipher (hw6)
# Description: This ROT13 Cipher program encrypts or decrypts a given message by shifting each letter according to the
# letter's index in the alphabet + 13 (wrapped); all input given by the user. Runs until the user quits.

while 1:
    # Stores the given pivot character's ASCII code number
    pivot_char = ord(input("What is your pivot character?: (char) ").lower())

    # Creates a shifted alphabet according to the pivot character. Codes greater than 123 (z) are wrapped to 97 (a)
    cipher_alpha = [chr(((char + pivot_char + 1) % 26) + 97) for char in range(97, 123)]

    # Asks the user if they want to encode, decode, or quit
    input_option = int(input("Encode(0) decode(1) or quit(2)?: (int) "))
    if input_option == 2:
        break

    # En/decodes given user input according to the generated cipher_alpha making sure to keep case and non-alpha chars
    message = [chr((lambda x: x + cipher_alpha.index(i.lower()))(97 if i.islower() else 65)) if i.isalpha() else i
               for i in input("Type your message: (string) ")]

    # Prints the en/decoded message according to what the user selected previously
    print("Your %s message is: " % ("encoded" if input_option == 0 else "decoded") + "".join(message))
