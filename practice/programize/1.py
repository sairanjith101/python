import random

def password_generator():
    char = '!@#$%&*+'
    size = random.randint(5,6)
    return ''.join(random.choice(char) for i in range(size))

print(password_generator())