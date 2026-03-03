import random

def generate_token():
    return str(random.random())  # Not secure

def format_name(first, last):
    return first + " " + last

def calculate_discount(price, percentage):
    return price - (price * percentage)