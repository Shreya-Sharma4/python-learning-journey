number = 12345

original_number = number
reversed_number = 0

while number > 0:
    digit = number % 10
    reversed_number = reversed_number * 10 + digit
    number //= 10

print(f"Original Number: {original_number}")
print(f"Reversed Number: {reversed_number}")