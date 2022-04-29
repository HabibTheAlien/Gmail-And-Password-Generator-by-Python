import string
import random


first_name = input("Enter your First Name:")
last_name = input("Enter your Last Name:")
password_length = int(input(("Enter the length of password:-")))

all_characters = string.ascii_letters+string.digits

email = first_name.lower()+"."+last_name.lower()+"@gmail.com"
password = " "

for character in range(password_length):
    random_character = random.choice(all_characters)
    password = password+random_character


print("Your Gmail ID is:" + email)
print("Your password is:" + password)
