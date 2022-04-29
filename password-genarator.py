import string
import random


def generate_password(size):
    password = " "
    all_characters = string.ascii_letters+string.digits
    for character in range(size):
        random_character = random.choice(all_characters)
        password = password+random_character

    return password


password_length = int(input(("Enter the length of password:-")))
your_password = generate_password(password_length)

print("Your password is:", your_password)
