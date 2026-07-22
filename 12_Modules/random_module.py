import random

numbers = [10, 20, 30, 40, 50]

print(f"Random Number: {random.randint(1, 100)}")
print(f"Random Choice: {random.choice(numbers)}")

random.shuffle(numbers)
print(f"Shuffled List: {numbers}")