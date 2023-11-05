#Create a function where.
#Given this string of numbers
string = "7476075448"

#Print me this String
# "7476-075-338"

# option 1
#         [START : END : STEP ]
x = string[0 : 4]
y = string[4 : 7]
z = string[7::]

listOfString = [x,y,z]
print(listOfString)
finalString = "-".join(listOfString)
print(finalString)

# option 2
finalString2 = x + "-" + y + "-" + z
print(finalString2)

# option 3string 
finalString3 = f"{x}-{y}-{z}"
print(finalString3)


#You probably know the "like" system from Facebook and other pages. 
# People can "like" blog posts, pictures or other items. 
# We want to create the text that should be displayed next to such an item.

# Implement the function which takes an array containing the names of people that like an item. 
# It must return the display text as shown in the examples:

# []                                -->  "no one likes this"
# ["Peter"]                         -->  "Peter likes this"
# ["Jacob", "Alex"]                 -->  "Jacob and Alex like this"
# ["Max", "John", "Mark"]           -->  "Max, John and Mark like this"
# ["Alex", "Jacob", "Mark", "Max"]  -->  "Alex, Jacob and 2 others like this"
# Note: For 4 or more names, the number in "and 2 others" simply increases.

listOfPeople = ["Tina"]

def whoLikes(list):
    if len(list) == 0:
        return "no one likes this"
    elif len(list) == 1:
        return f"{list[0]} likes this"
    elif len(list) == 2:
        return f"{list[0]} and {list[1]} like this"
    elif len(list) == 3:
        return f"{list[0]}, {list[1]} and {list[2]} like this"
    elif len(list) >= 4:
        return f"{list[0]}, {list[1]} and {len(list)-2} others like this"


print(whoLikes(listOfPeople))


# Task
# Sum all the numbers of a given array ( cq. list ),
#  except the highest and the lowest element ( by value, not by index! ).

# The highest or lowest element respectively is a single element at each edge, even if there are more than one with the same value.

# Mind the input validation.

# Example
# [ 6, 2, 1, 8, 10 ] => 16
# [ 1, 1, 11, 2, 3 ] => 6

listOfNumbers = [6, 2, 1]

def sumNoMinNoMax(list):
    # min_num = min(list)
    # max_num = max(list)
    # result = sum(list) - max_num - min_num
    # return result
    return sum((list-(max(list)-min(list))))

print(sumNoMinNoMax(listOfNumbers))

# Write a method, that will get an integer array as parameter and will process every number from this array.

# Return a new array with processing every number of the input-array like this:

# If the number has an integer square root, take this, otherwise square the number.

# Example
# [4,3,9,7,2,1] -> [2,9,3,49,4,1]
