number = 9

square = number ** 2
digit_sum = 0

while square > 0:
    digit = square % 10
    digit_sum += digit
    square //= 10

if digit_sum == number:
    print(f"{number} is a Neon Number")
else:
    print(f"{number} is Not a Neon Number")