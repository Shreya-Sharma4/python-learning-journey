number = 12345

digit_sum = 0

while number > 0:
    digit = number % 10
    digit_sum += digit
    number //= 10

print(f"Sum of digits: {digit_sum}")