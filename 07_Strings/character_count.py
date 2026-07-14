text = "Python Programming"

character = "m"
count = 0

for value in text:
    if value == character:
        count += 1

print(f"'{character}' occurs {count} times.")