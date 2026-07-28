class AgeError(Exception):
    pass


print("start")

try:
    age = int(input("Enter age: "))

    if age > 18:
        print("Eligible")
    else:
        raise AgeError("Age should be greater than 18")

except AgeError as error:
    print(error)

finally:
    print("Program finished")

print("end")
