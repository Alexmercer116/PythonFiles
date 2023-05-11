
import re
# PyPackage Containing Regexp

# Following are some wild Card Characters
# ^ -> starts with ,
# $ -> Ends With ,
# . -> Matches any character,
# * -> Matches 0 or more character,
# + -> Matches 1 or more character,
# ? -> Matches a single character or don't be greedy
# /S -> Matches any non-whitespace characters
# /s -> Matches any white space characters
# Following is an Example :
# ^X-/s*:
# The above regexp means : Find  a line that starts with an X followed by a '-'
# followed by a 0 or more non-whitespace char followed by a ':'. 

# [a-z] -> Matches the character mentioned in range 

# re.search() finds the pattern and returns true or false
# find() finds the first occurence of the string
# re.findall() returns all the strings that matches regular expression

# Example one : 

x = "My name is Akr123 and My age is 23 and I'm 1"
y = re.findall('[0-9]+',x)
print(y)

# The Above says to find [0-9] gives one digit and we're adding + which
# means 1 or more digits.

# Example Two : 

str1 = "From : Myself Using the frat:"
res = re.findall(".+?:",str1)
print(res)

# The above exp means : . matches any char and adding + means Match one or more characters
# ? stop when you find one :

# Example two :
str2 = "From stephen.marquard@uct.co.in sat Jun 5 20:08:19 2022"
res1 = re.findall("@([^ ]*)",str2)
print(res1)

# The [^ ] : Inside the [] the ^ means not and we are providing space which means not space means non-blank chars.

