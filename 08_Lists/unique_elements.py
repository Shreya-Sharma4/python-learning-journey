numbers = [10, 20, 30, 20, 40, 10, 50]

unique_elements = []

for number in numbers:
    if numbers.count(number) == 1:
        unique_elements.append(number)

print(f"Unique Elements: {unique_elements}")