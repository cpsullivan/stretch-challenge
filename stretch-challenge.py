def sum_of_digits(num):
    sum_num = 0
    num = str(num)
    for digit in num:
        digit = int(digit)
        sum_num += digit
    return sum_num
print(sum_of_digits(1234))

def prod_of_digits(other_num):
    prod_num = 1
    other_num = str(other_num)
    for digit in other_num:
        digit = int(digit)
        prod_num *= digit
    return prod_num
print(prod_of_digits(1234))