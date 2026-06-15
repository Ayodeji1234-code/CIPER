def caesar_encrypt(text, shift):
    encrypted_text = ""

    for character in text:
        encrypted_text += chr(ord(character) + shift)

    return encrypted_text


def caesar_decrypt(text, shift):
    decrypted_text = ""

    for character in text:
        decrypted_text += chr(ord(character) - shift)

    return decrypted_text


def encrypt_file(input_file, output_file, shift):
    try:
        with open(input_file, "r", encoding="utf-8") as file:
            content = file.read()

        encrypted_content = caesar_encrypt(content, shift)

        with open(output_file, "w", encoding="utf-8") as file:
            file.write(encrypted_content)

        print(f"File encrypted successfully and saved as: {output_file}")

    except FileNotFoundError:
        print("Error: The input file was not found.")
    except Exception as error:
        print(f"An error occurred: {error}")


def decrypt_file(input_file, output_file, shift):
    try:
        with open(input_file, "r", encoding="utf-8") as file:
            content = file.read()

        decrypted_content = caesar_decrypt(content, shift)

        with open(output_file, "w", encoding="utf-8") as file:
            file.write(decrypted_content)

        print(f"File decrypted successfully and saved as: {output_file}")

    except FileNotFoundError:
        print("Error: The input file was not found.")
    except Exception as error:
        print(f"An error occurred: {error}")


def main():
    shift = 3

    while True:
        print("\nBasic File Encryption/Decryption")
        print("1. Encrypt a file")
        print("2. Decrypt a file")
        print("3. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            input_file = input("Enter the file name to encrypt: ")
            output_file = input("Enter the new encrypted file name: ")
            encrypt_file(input_file, output_file, shift)

        elif choice == "2":
            input_file = input("Enter the file name to decrypt: ")
            output_file = input("Enter the new decrypted file name: ")
            decrypt_file(input_file, output_file, shift)

        elif choice == "3":
            print("Program closed.")
            break

        else:
            print("Invalid choice. Please select 1, 2, or 3.")


if __name__ == "__main__":
    main()