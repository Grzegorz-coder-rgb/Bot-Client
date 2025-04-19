import random


password_characters = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
password = ""

def gen_pass():
    length = random.randint(1, 100)  # losowa długość od 1 do 100
    password = ""
    for i in range(length):
        password += random.choice(password_characters)
    return password


def gen_emoji():
    emodji = ["\U0001f600", "\U0001f642", "\U0001F606", "\U0001F923"]
    return random.choice(emodji)


def flip_coin():
    flip = random.randint(0, 2)
    if flip == 0:
        return "Orzeł"
    else:
        return "Rzeszka"
