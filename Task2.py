import random
import string
def generate_password(length, use_letters, use_numbers, use_symbols):
    characters = ''
    if use_letters == 'y':
        characters += string.ascii_letters
    if use_numbers == 'y':
        characters += string.digits
    if use_symbols == 'y':
        characters += string.punctuation
    if not characters:
        print("You must select at least one character type (letters, numbers, or symbols).")
        return None
    password = ''.join(random.choice(characters) for _ in range(length))
    return password
def main():
    print("Welcome to the Password Generator!")
    length = int(input("Enter the desired password length: "))
    use_letters = input("Include letters (y/n)? ").lower()
    use_numbers = input("Include numbers (y/n)? ").lower()
    use_symbols = input("Include symbols (y/n)? ").lower()
    password = generate_password(length, use_letters, use_numbers, use_symbols)
    if password:
        print(f"Generated Password: {password}")

if __name__ == "__main__":
    main()