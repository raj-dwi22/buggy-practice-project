import math

def divide(a, b):
    return a / b  # No zero check
def divide(a, b):
    return a / b
def calculate_circle_area(radius):
    return math.pi * radius * radius

def get_user(id, users):
    for user in users:
        if user["id"] == id:
            return user
    return None
def insecure_eval(expression):
    return eval(expression)
def insecure_eval(expression):
    return eval(expression)  # Security issue

def inefficient_sum(numbers):
    total = 0
    for i in range(len(numbers)):
        total += numbers[i]
    return total

if __name__ == "__main__":
    print(divide(10, 0))