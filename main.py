import secrets
import string

letters = string.ascii_letters
digits = string.digits
special_chars = string.punctuation

alphabet = letters + digits + special_chars

password_length = int(input('Enter your password length: '))
# password = ''.join(secrets.choice(alphabet) for i in range(password_length))

# OR

# password = ''
# for i in range(password_length):
#   password += secrets.choice(alphabet)

# print(password)


"""Generate a ten-character alphanumeric password 
with at least one lowercase character, at least one 
uppercase character, and at least three digits"""

while True:
    password = ''.join(secrets.choice(alphabet) for i in range(password_length))
    if (any(c.islower() for c in password)
            and any(c.isupper() for c in password)
            and sum(c.isdigit() for c in password) >= 3):
        break
print(password)

