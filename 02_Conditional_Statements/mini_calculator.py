first_number = 20
second_number = 10
operator = "*"

match operator:
    case "+":
        result = first_number + second_number
    case "-":
        result = first_number - second_number
    case "*":
        result = first_number * second_number
    case "/":
        if second_number != 0:
            result = first_number / second_number
        else:
            result = "Cannot divide by zero."
    case _:
        result = "Invalid operator."

print(result)