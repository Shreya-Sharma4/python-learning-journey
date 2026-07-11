number = 25

binary = ""

while number > 0:
    remainder = number % 2
    binary = str(remainder) + binary
    number //= 2

print(binary)