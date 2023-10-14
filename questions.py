#Give me the sum of 2 number as a function
def addNum(num1, num2):
    return num1 + num2

print(addNum(1,2))

#Give me a function that returns the value of array that has 5 numbers
def sum_of_nums(numbers):
    add_num = 0

    for i in numbers:
        add_num = add_num + i

    return add_num

group_one = [1,2,3,4,5]
print(sum_of_nums(group_one))
