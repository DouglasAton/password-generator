"""
Password Generator Project

This Python script generates a random password based on user-specified criteria, including the number of letters, symbols,
and numbers to include. The generated password is a combination of random characters from the lists of letters, numbers,
and symbols.

Usage:
- Run the script.
- Follow the prompts to specify the number of letters, symbols, and numbers for the password.
- The script will generate a random password based on the provided criteria and display it to the user.
"""

import random

# List of letters, numbers, and symbols to generate password
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
           'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
           'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

# Get user input for password criteria
print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

# List to store generated password characters
password_list = []

# Generate letters for the password
for char in range(1, nr_letters + 1):
    password_list.append(random.choice(letters))

# Generate symbols for the password
for char in range(1, nr_symbols + 1):
    password_list += random.choice(symbols)

# Generate numbers for the password
for char in range(1, nr_numbers + 1):
    password_list += random.choice(numbers)

# Shuffle the password list to mix characters
random.shuffle(password_list)

# Convert the password list to a string
password = ""
for char in password_list:
    password += char

# Print the generated password
print(f"Your password is: {password}")
