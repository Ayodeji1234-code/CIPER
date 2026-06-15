# Caesar Cipher Encryption and Decryption

## Description

This project is a Python implementation of the Caesar Cipher, one of the oldest and most well-known encryption techniques in cryptography. The program allows users to encrypt and decrypt messages by shifting each letter in the text by a specified number of positions in the alphabet.

The Caesar Cipher is a substitution cipher where each letter is replaced by another letter a fixed number of positions down or up the alphabet. This project demonstrates the basic principles of encryption and decryption while strengthening understanding of Python programming concepts.

## Features

* Encrypt plain text messages
* Decrypt encrypted messages
* User-defined shift key
* Preserves spaces and non-alphabetic characters
* Menu-driven interface
* Input validation and error handling

## Technologies Used

* Python 3

## How It Works

The Caesar Cipher works by shifting each letter in the message by a fixed number of positions.

Example with a shift value of 3:

```text
A → D
B → E
C → F
...
X → A
Y → B
Z → C
```

Encryption converts readable text into coded text, while decryption reverses the process to recover the original message.

## Installation

1. Install Python 3 on your computer.
2. Download or clone the project files.
3. Open a terminal or command prompt in the project folder.

## Usage

Run the program using:

```bash
python caesar_cipher.py
```

Follow the on-screen instructions to:

1. Encrypt a message
2. Decrypt a message
3. Exit the application

## Example

### Encryption

```text
Enter message: HELLO WORLD
Enter shift value: 3

Encrypted Message: KHOOR ZRUOG
```

### Decryption

```text
Enter encrypted message: KHOOR ZRUOG
Enter shift value: 3

Decrypted Message: HELLO WORLD
```

## Project Structure

```text
caesar_cipher.py
README.md
```

## Learning Outcomes

This project helped me develop skills in:

* Python programming
* Functions and modular code design
* String manipulation
* Loops and conditional statements
* User input validation
* Basic cryptography concepts
* Problem-solving and algorithm development

## Future Improvements

* Support for multiple encryption algorithms
* Brute-force attack demonstration
* File encryption and decryption
* Graphical User Interface (GUI)
* Enhanced key management

## Author

Developed as part of my Python Development Internship project.

