# Link to website for viewing the questions: https://pynative.com/python-string-exercise/

# 1A: Create a string made of the first, middle and last character

str1 = "James"

first = str1[0]
if(len(str1) % 2 == 0):
    middle = len(str1) // 2 - 1 
else:
    middle = len(str1) // 2

middle_string = str1[middle]

last = str1[-1]
result = first + middle_string + last

print("Result:", result, "\n")


# 1B: Create a string made of the middle three characters

str1 = "JhonDipPeta"
str2 = "JaSonAy"

middle1 = len(str1) // 2
middle2 = len(str2) // 2

result1 = str1[middle1 - 1:middle1 + 2]
result2 = str2[middle2 - 1:middle2 + 2]

print("Results are: {} and {}".format(result1, result2), "\n")

# 2: Append new string in the middle of a given string
s1 = "Ault"
s2 = "Kelly"
if(len(s1) % 2 == 0):
    middle1 = len(s1) // 2 - 1 
else:
    middle1 = len(s1) // 2
first = s1[:middle1 + 1]
string_append = s2
last = s1[middle1 + 1:]

result = first + string_append + last
print(result, "\n")

# 3: Create a new string made of the first, middle, and last characters of each input string

s1 = "America"
s2 = "Japan"

if(len(s1) % 2 == 0):
    middle1 = len(s1) // 2 - 1 
    middle2 = len(s2) // 2 - 1 
else:
    middle1 = len(s1) // 2
    middle2 = len(s2) // 2

print(s1[0]+s2[0]+s1[middle1]+s2[middle2]+s1[-1]+s2[-1], "\n")

# 4: Arrange string characters such that lowercase letters should come first

str1 = "PyNaTive"
lower = ""
upper = ""
for i in str1:
    if(i.islower()):
        lower = lower + i
    else:
        upper = upper + i
# result = lower + upper # second option
result = "".join(lower + upper) 

print(result, "\n")

# 5: Count all letters, digits, and special symbols from a given string

str1 = "P@#yn26at^&i5ve"

chars = 0
digits = 0
symbols = 0
for i in str1:
    if (i.isalpha()):
        chars += 1
    elif (i.isdigit()):
        digits += 1
    elif (not i.isspace()):
        symbols += 1

print("Total counts of chars, digits, and symbols")
print("Chars: {} \nDigits: {} \nSymbols: {}".format(chars, digits, symbols))

# 6: Create a mixed String using the following rules

s1 = "Abc"
s2 = "Xyzsd"
result = ""
i1 = 0
i2 = len(s2) - 1

while(i1 < len(s1) or i2 >= 0):
    if(i1 < len(s1)):
        result = result + s1[i1]
    if(i2 >= 0):
        result = result + s2[i2]
    i1 += 1
    i2 -= 1

print(result, "\n")

# 7: String characters balance Test

def string_balance_check(s1, s2):
    for i in s1:
        if(not i in s2):
            return False
        # result = False if not i in s2 else True
        
    return True

print(string_balance_check("Yn","PYnative"))
print(string_balance_check("Ynf","PYnative"))
print()

# 8: Find all occurrences of a substring in a given string by ignoring the case

################ 1st option ################

# str1 = "Welcome to USA. usa usa awesome, isn't it?" 
# substring = "USA"

# print("The \"{}\" count in \"Welcome usa USA. usa us awesome, isn't it?\" is: ".format(substring), str1.lower().count(substring.lower()), "\n")

# print()

################ 2nd option ################

# def find_occurence (str1, str2) -> int:
#     str1 = str1.upper()
#     str2 = str2.upper()
#     count = 0
#     a = 0
    
#     for i in range(len(str2)):
#         stor = i
#         if(str2[i] == str1[a]):
#             while (str2[i] == str1[a] and a < len(str1) - 1):
#                 i += 1
#                 a += 1
#                 if(a == len(str1) - 1 and str2[i] == str1[a]):
#                     count = count + 1
#         i = stor + 1
#         a = 0

#     return count

# str1 = "USA"
# str2 = "Welcome usa USA. usa us awesome, isn't it?"

# print("The \"{}\" count in \"Welcome usa USA. usa us awesome, isn't it?\" is:".format(str1), find_occurence(str1, str2), "\n")

################ 3rd option ################

def find_occurrence(str1, str2) -> int: 
    str1 = str1.upper()  
    str2 = str2.upper()  
    count = 0
    for i in range (len(str2) - len(str1) + 1):
        if(str2[i:i + len(str1)] == str1):
            count += 1
    return count

str1 = "USA"
str2 = "Welcome usa USA. usa us awesome, isn't it?"

print("The \"{}\" count in \"{}\" is: {}".format(str1, str2, find_occurrence(str1, str2)), "\n")


# 9: Calculate the sum and average of the digits present in a string

str1 = "PYnative29@#8496"
summ = 0
count = 0

for i in str1:
    if(i.isdigit()):
        summ = summ + int(i)
        count += 1

average = summ / count

print("Sum is: %d \nAverage is: %f\n" % (summ, average))

################# 2nd option #################
# import re 

# str1 = "PYnative29@#8496"

# digits = [int(num) for num in re.findall(r'\d', str1)]

# total = sum(digits)
# average = total / len(digits)

# print("Sum is: %d \nAverage is: %f" % (total, average))

# 10: Write a program to count occurrences of all characters within a string

str1 = "Apple"
result = {str1[0] : str1.count(str1[0])}

for i in str1:
    result[i] = str1.count(i)

print(result, "\n")
    
# 11: Reverse a given string

str1 = "PYnative"

reverse = str1[::-1]
print("Reversed version of {1}: {0}".format(reverse, str1), "\n")

# 12: Find the last position of a given substring

str1 = "Emma is a data scientist who knows Python. Emma works at google."
str2 = "Emma"

last_position = str1.rfind(str2)
print("Last occurrence of Emma starts at index %d" % last_position, "\n")

# 13: Split a string on hyphens

str1 = "Emma-is-a-data-scientist"

result = str1.split("-") # return list

print("Displaying each substring\n")

for i in result:
    print(i)

print()

# 14: Remove empty strings from a list of strings

##################### 1st option #####################

str_list = ["Emma", "Jon", "", "Kelly", None, "Eric", ""]

result = []

for i in str_list:
    # if(i != None and i != ""):
    if(i):
        result.append(i) # returns None so no need to assign to smth

print(result, "\n")

##################### 2nd option #####################

str_list = ["Emma", "Jon", "", "Kelly", None, "Eric", ""]

new_str_list = list(filter(None, str_list)) # built-in function filter to filter empty value, works with None

print(result, "\n")

# 15: Remove special symbols / punctuation from a string

##################### 1st option #####################

str1 = "/*Jon is @developer & musician"
result = ""
i = 0
while (i < (len(str1))):
    if(str1[i].isalnum()):
        result += str1[i]
        i += 1
    elif(str1[i].isspace()):
        result += str1[i]
        while(not str1[i].isalnum()):
            i += 1
    else:
        i += 1

print(result, "\n")

##################### 2nd option #####################

import string
str1 = "/*Jon is @developer & musician"
new_string = str1.translate(str1.maketrans("", "", string.punctuation))

print(new_string, "\n")

##################### 3rd option #####################

import re

str1 = "/*Jon is @developer & musician"
new_string = re.sub(r"[^\w\s]", "", str1)

print(new_string, "\n")

# 16: Removal all characters from a string except integers

##################### 1st option #####################

str1 = 'I am 25 years and 10 months old'
result = ""

for i in str1:
    if(i.isdigit()):
        result += i

print(result, "\n")

##################### 2nd option #####################

import re

str1 = 'I am 25 years and 10 months old'

digits_list = re.findall(r"\d", str1) # returns list
result = ""

for i in digits_list:
    result += i

print(result, "\n")

# 17: Find words with both alphabets and numbers

##################### 1st option #####################

import re 

str1 = "Emma25 is Data, scientist50 and AI Expert"

regex_string = re.split("[^\w|_]", str1)

for i in regex_string:
    if(i.isalnum()):
        print(i, "\n")


##################### 2nd option #####################
import string

str1 = "Emma25 is Data scientist50 and AI Expert"
str1 = str1.split()

for i in str1:
    if(i.isalnum()):
        print(i, "\n")

# 18: Replace each special symbol with # in the following string

##################### 1st option #####################

import string

str1 = '/*Jon is @developer & musician!!'
length = len(string.punctuation)
result = str1.translate(str1.maketrans(string.punctuation, "#"*length))

print(result, "\n")

##################### 2nd option #####################

import string

str1 = '/*Jon is @developer & musician!!'
replacement = "#"

for char in string.punctuation:
    str1 = str1.replace(char, replacement)

print(str1, "\n")

# print(type(str.maketrans("a", "b"))) # returns dictionary type
