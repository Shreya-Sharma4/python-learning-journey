text = "Python"

reversed_text = ""

for character in text:
    reversed_text = character + reversed_text

print(f"Original String: {text}")
print(f"Reversed String: {reversed_text}")