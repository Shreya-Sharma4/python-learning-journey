"""
Topic: Operators
Description: Demonstrates arithmetic, comparison, logical, assignment, and membership operators.
"""

# Taking input
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

print("\n----- Arithmetic Operators -----")
print("Addition:", num1 + num2)
print("Subtraction:", num1 - num2)
print("Multiplication:", num1 * num2)
print("Division:", num1 / num2)
print("Floor Division:", num1 // num2)
print("Modulus:", num1 % num2)
print("Exponent:", num1 ** num2)

print("\n----- Comparison Operators -----")
print("Equal:", num1 == num2)
print("Not Equal:", num1 != num2)
print("Greater Than:", num1 > num2)
print("Less Than:", num1 < num2)
print("Greater Than or Equal:", num1 >= num2)
print("Less Than or Equal:", num1 <= num2)

print("\n----- Logical Operators -----")
print("AND:", num1 > 0 and num2 > 0)
print("OR:", num1 > 0 or num2 > 0)
print("NOT:", not (num1 > num2))

print("\n----- Assignment Operator -----")
value = num1
value += 5
print("After += 5:", value)

print("\n----- Membership Operator -----")
numbers = [10, 20, 30, 40, 50]
print("20 in numbers:", 20 in numbers)
print("100 not in numbers:", 100 not in numbers)