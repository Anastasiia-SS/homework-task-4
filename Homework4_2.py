import random

def get_numbers_ticket(min, max, quantity):
    if min < 1 or max > 1000 or quantity > (max - min + 1) or min > max:
        return []
    numbers = random.sample(range(min, max + 1), quantity)
    return sorted(numbers)
print(get_numbers_ticket(600, 1000, 6))