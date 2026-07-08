number = 145

original_number = number
factorial_sum = 0

while number > 0:
    digit = number % 10

    factorial = 1
    for value in range(2, digit + 1):
        factorial *= value

    factorial_sum += factorial
    number //= 10

if original_number == factorial_sum:
    print("Strong Number")
else:
    print("Not a Strong Number")