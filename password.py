import random
import string

print('Welcome to the secure password generator!!!!')
password = ''
password_lenght = input('How many characthers the password will contain?: ')
password_lenght = int()

print('Here are your secure password: ')

for c in range(password_lenght):
        password += random.choice(string.ascii_letters + string.digits+string.punctuation)

print(password)