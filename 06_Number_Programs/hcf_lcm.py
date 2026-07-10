first_number = 12
second_number = 18

smaller = first_number

if second_number < first_number:
    smaller = second_number

hcf = 1

for value in range(1, smaller + 1):
    if first_number % value == 0 and second_number % value == 0:
        hcf = value

lcm = (first_number * second_number) // hcf

print(f"HCF: {hcf}")
print(f"LCM: {lcm}")
