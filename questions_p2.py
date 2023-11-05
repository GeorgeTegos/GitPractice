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

listOfPeople = []

def whoLikes(list):
    pass
    # Code Here !


print(whoLikes(listOfPeople))