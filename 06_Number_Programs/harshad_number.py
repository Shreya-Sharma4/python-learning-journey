number = 18

original_number = number
digit_sum = 0

while number > 0:
    digit = number % 10
    digit_sum += digit
    number //= 10

if original_number % digit_sum == 0:
    print(f"{original_number} is a Harshad Number")
else:
    print(f"{original_number} is Not a Harshad Number")