number = 28

sum_of_factors = 0

for factor in range(1, number):
    if number % factor == 0:
        sum_of_factors += factor

if sum_of_factors == number:
    print("Perfect Number")
else:
    print("Not a Perfect Number")