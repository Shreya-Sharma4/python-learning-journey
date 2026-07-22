import random

colors = ["Red", "Black", "Blue", "Pink"]

print(f"Random Integer : {random.randint(1000, 9999)}")
print(f"Random Float   : {random.random()}")
print(f"Random Range   : {random.randrange(1, 10, 2)}")
print(f"Random Choice  : {random.choice(colors)}")
print(f"Random Choices : {random.choices(colors, k=2)}")

random.shuffle(colors)
print(f"Shuffled List  : {colors}")