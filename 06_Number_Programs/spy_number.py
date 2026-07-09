number = 123

original_number = number
digit_sum = 0
digit_product = 1

while number > 0:
    digit = number % 10
    digit_sum += digit
    digit_product *= digit
    number //= 10

if digit_sum == digit_product:
    print(f"{original_number} is a Spy Number")
else:
    print(f"{original_number} is Not a Spy Number")