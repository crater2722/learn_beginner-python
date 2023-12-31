#imports and stuff here

import math

#variables

worlds = "food is food"
print(worlds)


#NUMBERS:


# + normal addition

print(5+5) #gives 10 as the total

# - normal subtraction

print(5-3) #gives 2 as the difference

# * normal multiplication

print(3*3) #gives 9 as the product

#  ** power of a number

print(10**3) #gives 1000 as the cube of 10

#  / normal division

print(10/5) #gives 2 as the answer

#  // integer division

print(10//3) #gives 3 as the quoefficent

#  %  remainder of division

print(10%3) #gives 1 as the remainder

# that can all be done using variables

num_test1 = 10
num_test2 = 5
num_test3 = 3
print(num_test1/num_test2) #gives 2
print(num_test1+num_test2) #gives 15
print(num_test1-num_test2) #gives 5
print(num_test1*num_test2) #gives 50
print(num_test1**num_test3) #gives 1000
print(num_test1//num_test3) #gives 3
print(num_test1%num_test3) #gives 1


#STRINGS


#you can put words (which is called a string) in a variable

string_thing = "this is a string"

# \n enter but in print statements

print("hello, this is an enter: \n") #gives an extra line below the sentence because it is an enter key input

# \x is a way to put in hexadecimals in python

print("\x41") #gives A because of hexadecimals

# \t is tab but in print statements

tab_input = "S\tr\ti\tm\ta\ta\tn\n"
print(tab_input)
#gives a large space between the letters because of the \t or tab input

#  '' can use in prints and variables to input strings

single_quote = 'I can put strings in single quotes and double quotes'

#  , you can use commas to input 2 or more string values at the same time

print(worlds, single_quote) #gives 'food is food I can put strings in single quotes and double quotes'

# + you can use plus signs to input 2 or more string values at the same time but they do not have a space in the middle.

print(worlds+single_quote) #gives 'food is foodI can put strings in single quotes and double quotes' there is no space between the values

#double quotes and single quotes work the same way with the exception of working with quotes inside.

single_quotes1 = 'He said "Hi"' #if you have single quotes surronding the string, then double quotes can work inside.
print(single_quotes1)

double_quotes1 = "He said \"Hi\"" #but if you need to use the same quote inside, you need to put a \ in front so python does not think it is the end of the string.
print(double_quotes1)

single_quotes2 = 'I\'m learning!' #the same thing above applies here
print(single_quotes2)

double_quotes2 = "I'm learning!" #the same thing above applies here
print(double_quotes2)


# \  you need to put 2 back slashes to input one because of python thinking you want to combine the current line with the past line. I will get to that in line 116

print("\\") #gives \
#you can also do this to the enter and tab inputs:
print('\\t') #gives \t
print('\\n') #gives \n

# () you can combine the words on 2 lines together

line_combine1 = ("line""_"
"combine")
print(line_combine1)
#gives 'line_combine'

# """ you can also combine lines by placing 3 double quotes at the start and end of the string. it automattically puts a new line for the second string

line_combine2 = ("""this is line 1
and this is line 2""")
print(line_combine2)

"""
This is a comment
the code above prints:
ss
s
because of the extra enter key at the end and because it is combined
"""

# \ you can also combine string sentences between the big string value to combine the sentence in the output even though it is seperated in the code.

line_combine3 = ("""this is a big sentence and \
it just got combined""")
print(line_combine3)
#combines sentences and gives "this is a big sentence and it just got combined"

# []  you can place a number in those parentheses and the it will grab the letter starting from the left side of the variables.

grab_a_letter_from_me = "Try and grab a letter or part of me if you can"
print(grab_a_letter_from_me[2])
#gives 'y' as output because I grabbed one letter

# you do the same thing above but also grab a part of a variable by putting a : after the number. You can put it before the number to get everything before it instead.

print(grab_a_letter_from_me[4:]) #gives everything after the word 'try'. so the output would be: " and grab a letter or part of me if you can"
print(grab_a_letter_from_me[:12]) #gives everything before the space after the word 'grab'. so the output would be: "Try and grab"

# you can do the same thing but instead of everything after, you can grab a part by putting a number after the :

print(grab_a_letter_from_me[4:21]) #gives everything between the word 'try' and space after the word 'letter'. so the output would be: "and grab a letter"

# ---From line 123 to line 136---This is called indexing and it is zero based. This means 0 will get the very first character. Also, when selecting a part of a variable, it INCLUDES only the starting value and doesn't include the ending value.
'''
BUT....
'''
# If you want to grab a character starting from the left, the last character would be considered '-1'. It is '-1' instead of '-0' is because '-0' and '0' are the same thing.

print(grab_a_letter_from_me[-1]) #gives 'n' because it is the last character in the string.

# using this, all indexing stuff above also works.

print(grab_a_letter_from_me[-21:]) #gives "part of me if you can"
print(grab_a_letter_from_me[:-25]) #gives "Try and grab a letter"
print(grab_a_letter_from_me[-38:-11]) #gives "grab a letter or part of me"

#you can also assign a indexed character to variables or in print statements

indexed_letter1 = 2
print(grab_a_letter_from_me[indexed_letter1], "u eat my cookies?")
#gives 'y u eat my cookies'
indexed_letter2 = 8
print(grab_a_letter_from_me[indexed_letter2:indexed_letter2+13])
#gives 'grab a letter'

# when you create a variable, the computer stores the value of the variable somewhere. To make sure that the value of a variable stays the same, we use the 'id' command in python.

value_checker = "I am learning python"
print(id(value_checker))
print(id(value_checker))
print(id(value_checker))
#in the output, all 3 numbers should have the same value. but if I change the value of the variable...
value_checker = "I am still learning python"
print(id(value_checker))
#the print statement above should have a different number because I changed the value.

#the same we used 'id' wen can also use 'len' to find the length of a variable.

print(len(value_checker)) #it will give 26 because it is showing how many characters there are.

#you can also get a certain character using indexing and the 'len' method

print(value_checker[len(value_checker) - 1]) #this will give 'n' because it is the last character.

# str()  you can use this to turn numbers into string values. Used 'len' as an example below.

print("The variable value checker was "+ str(len(value_checker))+ " characters long.") 
#gives "The variable value checker was 26 characters long." Using the 'len' function, you can also just use commas to not use the 'str' function and automatticly add spaces, but this wouldn't be very useful.
print("The variable value checker was", len(value_checker),"characters long.") 
#gives "The variable value checker was 26 characters long."

#