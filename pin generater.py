import random
import string

def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for i in range(length))
    return password

# Generate a random password with a length of 12 characters
password = generate_password(12)
print("Generated Password:", password)
