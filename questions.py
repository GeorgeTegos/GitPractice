# #Give me the sum of 2 number as a function
def addNum(num1, num2):
    return num1 + num2

print(addNum(1,2))
#
# #Give me a function that returns the value of a list that has 5 numbers
def sum_of_nums(numbers):
    add_num = 0

    for number in numbers:
        add_num = add_num + number

    return add_num

group_one = [1,2,3,4,5,7,8,7,9]
print(sum_of_nums(group_one))

#Give me a function that calculates the length of 2 strings and returns the smaller one

def min_str(str1, str2):
    len_str1 = len(str1)
    len_str2 = len(str2)

    if (len_str1>len_str2):
        return str2
    elif (len_str2>len_str1):
        return str1
    else:
        return "They are equal"


result = min_str("Hello", "Helo")
print(result)
