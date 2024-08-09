def is_armstrong_number(number):
    num = str(number)
    num_len = len(num)
    sum_of = 0
    for i in num:
        sum_of = sum_of + int(i)**num_len
    return sum_of == number

number = 153
if is_armstrong_number(number):
    print(f"{number} is an Armstrong number")
else:
    print(f"{number} is not an Armstrong number")