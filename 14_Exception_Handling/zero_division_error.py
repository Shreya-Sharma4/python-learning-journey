print("start")

try:
    print(10 / 0)
except ZeroDivisionError:
    print("Don't divide by zero")

print("program end")