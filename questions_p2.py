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