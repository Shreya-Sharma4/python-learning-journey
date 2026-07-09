number = 19
original_number = number

while number != 1 and number != 4:
    total = 0

    while number > 0:
        digit = number % 10
        total += digit ** 2
        number //= 10

    number = total

if number == 1:
    print(f"{original_number} is a Happy Number")
else:
    print(f"{original_number} is Not a Happy Number")