import random
import string
print("How strong do you want your password?")
while True:
    password_length = int(input("Length (8-32 characters): "))

    if password_length < 8 or password_length > 32:
        print("Password length must be between 8 and 32 characters\n")
        continue

    include_numbers = input("Include numbers? (y/n): ").lower()
    include_symbols = input("Include symbols? (y/n): ").lower()
    include_uppercase = input("Include uppercase? (y/n): ").lower()

    # Start with lowercase always
    chars = string.ascii_lowercase

    if include_uppercase == "y":
        chars += string.ascii_uppercase

    if include_numbers == "y":
        chars += string.digits

    if include_symbols == "y":
        chars += string.punctuation

    result = ''.join(random.choice(chars) for _ in range(password_length))
    print(f"\nGenerated password: {result}\n")