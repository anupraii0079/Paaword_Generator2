import random
import string
import pyperclip

# Function to assess password strength
def assess_password_strength(password):
    length = len(password)
    has_upper = any(char.isupper() for char in password)
    has_lower = any(char.islower() for char in password)
    has_digits = any(char.isdigit() for char in password)
    has_symbols = any(char in string.punctuation for char in password)
    
    # Simple strength rules based on character variety and length
    if length >= 12 and has_upper and has_lower and has_digits and has_symbols:
        return "Strong"
    elif length >= 8 and (has_upper or has_digits or has_symbols):
        return "Medium"
    else:
        return "Weak"

# Function to generate a password
def generate_password(length, use_numbers=True, use_symbols=True, use_uppercase=True):
    # Base characters (lowercase letters)
    characters = string.ascii_lowercase
    
    # Add numbers, symbols, and uppercase letters if specified
    if use_numbers:
        characters += string.digits
    if use_symbols:
        characters += string.punctuation
    if use_uppercase:
        characters += string.ascii_uppercase
    
    # Generate a random password
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

# Get user preferences
length = int(input("Enter the password length: "))
use_numbers = input("Include numbers? (y/n): ").lower() == 'y'
use_symbols = input("Include symbols? (y/n): ").lower() == 'y'
use_uppercase = input("Include uppercase letters? (y/n): ").lower() == 'y'

# Generate the password
generated_password = generate_password(length, use_numbers, use_symbols, use_uppercase)

# Copy the password to clipboard
pyperclip.copy(generated_password)

# Assess the strength of the generated password
password_strength = assess_password_strength(generated_password)

# Display the results
print(f"Generated Password: {generated_password}")
print(f"Password Strength: {password_strength}")
print("Password has been copied to the clipboard!")

