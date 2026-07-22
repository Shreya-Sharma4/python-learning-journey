import random

numbers = [10, 20, 30, 40, 50]

print(f"Random Integer      : {random.randint(1, 100)}")
print(f"Random Float        : {random.uniform(1, 10)}")
print(f"Random Choice       : {random.choice(numbers)}")
print(f"Random Sample       : {random.sample(numbers, 3)}")

random.shuffle(numbers)
print(f"Shuffled List       : {numbers}")

print(f"Random Range Value  : {random.randrange(10, 51, 5)}")