#####################################
###            Numbers            ###
#####################################

1 # is 1
#Math is self explanatory
1 + 1   # gives you 2
8 - 1   # gives you 7
10 * 2  # gives you 20

# division, one /, gives you deciaml numbers
# also known as floats
35 / 5.0  # gives you 7.0 not 7

# division, two /, gives you the equivelant of a floor function
# floor function is rounding down
# meaning it gives you how many times you can put a number in another number
5 // 3       # 5 divided by 3 will give you 1.666666, round that down and you will get 1.
6.8 // 3.2   # 6.8 divided by 3.2 will give you 2.125, round that down and you will get 2.0, because input is a float.
-5 // 3      # -5 divided by 3 will give you -1.666666, round that down and you will get 2.
-5.0 // 3.0  # gives you -2.0

# When you use a float, results are floats
3 * 2.0  # gives you 6.0

# Modulo operation
# opposite of //
# gives you the remainder of the division
7 % 3  # 7/3 = 2 with remainder of 1; answer is 1
9 % 2  # 9/4 = 4 with remainder of 1; answer is 1
27 % 6 # 27/6 = 4 with remainder of 3

# normal exponents
# ** instead of ^
2**4 # 2 raised to the power of four = 16
3**3 # 3 raised to the power of 3 == 27

# normal parentheses
#calculate or evaluate what is inside the parentheses first
(1 + 3) * 2  # gives you 8
# Python follows PEMDAS

#####################################
###            Boolean            ###
#####################################

# Boolean are truth values. 1 or 0. True or False
# case sensitive; ie: T and F have to be capatalized

# not reverses the truth values
not True   # gives you False
not False  # gives you True

# and takes a boolean before it and a boolean after it
# a and b will be true if and only if a and b are true. Pretty straight forward
True and True  # gives you True
True and False  # gives you False
False and True  # gives you False
False and False  # gives you False

# or takes a boolean before it and a boolean after it
# a or b will be true if and only if a or b is true. Pretty straight forward
True or True  # gives you True
True or False  # gives you True
False or True  # gives you True
False or False  # gives you False

# Note "and" and "or" are case-sensitive

# to check if two variables are equal use ==
# you can read a == b as: if a is equal to b then True
1 == 1  # gives you True
2 == 1  # gives you False
True == True # gives you True

# to check if two variables are NOT equal use !=
1 != 1  # gives you False
2 != 1  # gives you True
True != True # gives you False

# inequality signs are exactley like in Algebra
1 < 10  # gives you True
1 > 10  # gives you False
2 <= 2  # gives you True
2 >= 2  # gives you True

# Comparisons can be chained!
1 < 2 < 3  # gives you True
2 < 3 < 2  # gives you False

#####################################
###            Strings            ###
#####################################
# String are a bunch of characters together
# any thing can be in a string

# Strings are created with " or '
"This is a string."
'This is also a string.'

# Strings can be added too! But try not to do this.
"Hello " "world!"  # gives you "Hello world!"
# Strings can be added using '+'
"Hello " + "world!"    # gives you "Hello world!"

# use the print function to print variables
print("Hello World") # prints Hello World

# a common way to take input from the user is by
# the input function
input("Enter your name")

# input returns a string, so you need to cast
# your input to the type of variable you want
# you cast like this
int(var) # transforms var into an integer

print(input("Please input a number") + 1) # will give you an error
print(int(input("Please input a number") + 1)) # will give you your number plus 1

# Just to check u understand:
# Now, create a program that takes an input from a user
# Then, checks if that number is even or not
# NEXT: lists and similars
