def caesar_cipher(text, shift, mode):
    result = ""

    if mode == "decrypt":
        shift = -shift

    for character in text:
        if character.isalpha():
            start = ord('A') if character.isupper() else ord('a')

            new_position = (ord(character) - start + shift) % 26
            result += chr(start + new_position)
        else:
            result += character

    return result


print("================================")
print("     CAESAR CIPHER PROGRAM")
print("================================")

while True:
    print("\n1. Encrypt Text")
    print("2. Decrypt Text")
    print("3. Exit")

    choice = input("\nChoose an option (1-3): ")

    if choice == "1" or choice == "2":
        message = input("Enter your text: ")

        try:
            shift = int(input("Enter shift value: "))

            if choice == "1":
                result = caesar_cipher(message, shift, "encrypt")
                print("\nEncrypted Text:", result)

            else:
                result = caesar_cipher(message, shift, "decrypt")
                print("\nDecrypted Text:", result)

        except ValueError:
            print("Please enter a valid number for the shift.")

    elif choice == "3":
        print("Thank you for using Caesar Cipher!")
        break

    else:
        print("Invalid choice. Please select 1, 2 or 3.")
