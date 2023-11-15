import random

async def randomize():
    chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!@£$%^&*().,?0123456789'
    passwords=[]
    for pwd in range(1):
        password=""
    for c in range(12):
        password+=random.choice(chars)
    passwords.append(password)
    print(password)
    return password