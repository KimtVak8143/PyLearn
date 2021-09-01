import random

feet_in_mile = 5280
meters_in_km = 1000
Mobiles = ["Samsung", "Apple", "Realme", "Oneplus", "Xiaomi", "Nokia"]


def get_file(filename):
    return filename[filename.index(".") + 1:]


def roll_dice(num):
    return random.randint(1, num)
