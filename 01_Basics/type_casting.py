"""
Topic: Type Casting
Description: Demonstrates implicit and explicit type conversion in Python.
"""

# -------------------------------
# Implicit Type Casting
# -------------------------------

integer_value = 10
float_value = 2.5

result = integer_value + float_value

print("Implicit Type Casting")
print("Result:", result)
print("Data Type:", type(result))


# -------------------------------
# Explicit Type Casting
# -------------------------------

print("\nExplicit Type Casting")

number = 25

print("Integer:", number)
print("Float:", float(number))
print("String:", str(number))
print("Boolean:", bool(number))


decimal = 19.85

print("\nOriginal Float:", decimal)
print("Integer:", int(decimal))
print("String:", str(decimal))


text = "150"

print("\nOriginal String:", text)
print("Integer:", int(text))
print("Float:", float(text))


numbers = [10, 20, 30]

print("\nList:", numbers)
print("Tuple:", tuple(numbers))
print("Set:", set(numbers))


colors = ("Red", "Blue", "Green")

print("\nTuple:", colors)
print("List:", list(colors))


unique_numbers = {1, 2, 3}

print("\nSet:", unique_numbers)
print("List:", list(unique_numbers))