#Loop solution
def sum_of_digits(num):
    sum_num = 0
    num = str(num)
    for digit in num:
        sum_num += int(digit)
    return sum_num
print(sum_of_digits(1234))

#Recursive solution
def recursive_sum(num):
    rec_sum_num = 0
    str_num = str(num)
    #Recurses forever; revise
    return rec_sum_num + recursive_sum(str_num)
    
    #return rec_sum_num + recursive_sum(digit-1)
print(recursive_sum(123))

#Loop solution
def prod_of_digits(other_num):
    prod_num = 1
    other_num = str(other_num)
    for digit in other_num:
        prod_num *= int(digit)
    return prod_num
print(prod_of_digits(1234))