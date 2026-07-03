# Prime Number

number = 29
is_prime = True

if number < 2:
    is_prime = False
else:
    for divisor in range(2, int(number ** 0.5) + 1):
        if number % divisor == 0:
            is_prime = False
            break

print(f"{number} is {'Prime' if is_prime else 'Not Prime'}")


# Factorial

number = 5
factorial = 1

for value in range(1, number + 1):
    factorial *= value

print(f"Factorial of {number}: {factorial}")


# Multiplication Table

number = 7

for multiplier in range(1, 11):
    print(f"{number} x {multiplier} = {number * multiplier}")