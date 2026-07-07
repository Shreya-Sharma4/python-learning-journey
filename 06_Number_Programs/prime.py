number = 29

is_prime = number > 1

for divisor in range(2, int(number ** 0.5) + 1):
    if number % divisor == 0:
        is_prime = False
        break

print(f"{number} is {'Prime' if is_prime else 'Not Prime'}")