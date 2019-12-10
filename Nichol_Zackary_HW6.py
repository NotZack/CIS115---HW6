while 1:
    pivot_char = ord(input("What is your pivot character?: (char) ").lower())

    cipher_alpha = [chr(((char + pivot_char + 1) % 26) + 97) for char in range(97, 123)]

    input_option = int(input("Encode(0) decode(1) or quit(2)?: (int) "))
    if input_option == 2:
        break

    message = [chr((lambda x: x + cipher_alpha.index(i.lower()))(97 if i.islower() else 65)) if i.isalpha() else i
               for i in input("Type your message: (string) ")]

    print("Your %s message is: " % ("encoded" if input_option == 0 else "decoded") + "".join(message))
