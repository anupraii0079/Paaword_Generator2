import random 
import string 
#Function to generate password
def generate_password(length, use_numbers=True, use_symbols=True, use_uppercase=True):
    characters = string.ascii_lowercase

    #Add numbers, letter, symbols if specified 
    if use_numbers:
        characters += string.digits
    if use_symbols:
        characters += string.punctuation
    if use_uppercase:
        characters += string.ascii_uppercase
    
    #Generate a random password

    password = ''.join(random.choice(characters) for _ in range(length))
    return password

#Get user preferences
length = int(input("Enter the password length: "))
use_numbers = input("Include numbers?(y/n): ").lower() == 'y'
use_symbols = input("Include symbols?(y/n): ").lower() == 'y'
use_uppercase = input("Iclude uppercase letters? (y/n): ").lower() == 'y'

#Generate and display the password
generate_password = generate_password(length, use_numbers, use_symbols, use_uppercase)
print(f"Generated password: {generate_password}")
