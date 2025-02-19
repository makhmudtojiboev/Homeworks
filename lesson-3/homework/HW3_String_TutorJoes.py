# 1: Write a Python program to calculate the length of a string.
str1 = "Tutor Joes"
print("Length of the string \"{}\": {}\n".format(str1, len(str1)))

# 2: Write a Python program to count the number of characters (character frequency) in a string.

################### 1st option ###################

str1 = "tutorjoes"

result = {}

for i in str1:
    result[i] = str1.count(i)

print(result, "\n")

################### 2nd option ###################

str1 = "tutorjoes"

result = {}

for i in str1:
    keys = result.keys()
    if i in keys:
        result[i] += 1
    else:
        result[i] = 1

print(result, "\n")

# 3: Write a Python program to get a string from a given string where 
#    all occurrences of its first char have been changed to '@', except the first char itself.

str1 = "tutor joes"
str1 = str1[0] + str1[1:].replace(str1[0], "@")

print(str1, "\n")

# 4: Write a Python program to get a single string from two given strings, 
#    separated by a space and swap the first two characters of each string.

str1 = "abc"
str2 = "xyz"

result1 = str2[:2] + str1[2:]
result2 = str1[:2] + str2[2:]

result = " ".join([result1, result2])

print(result, "\n")

# 5: Write a Python program to remove the nth index character from a nonempty string.

str1 = "Tutor Joes"
remove_char = "t"

# result = ""     ### 2nd option ###
# for i in str1:
#     if(not i == remove_char):
#         result += i

result = str1.replace(remove_char, "", str1.count(remove_char))  ### 1st option ###

print(result, "\n")

# 6: Write a Python program to change a given string to a new string where the first and last chars have been exchanged

str1 = "Python"

exchanged = str1[-1] + str1[1:len(str1) - 1] + str1[0]

print(exchanged, "\n")

# 7: Write a Python program to remove the characters which have odd index values of a given string

str1 = "Computer Education"
odd_str = str1[0] # because 0 is neither even nor odd number

for i in range(1, len(str1)): 
    if(i % 2 == 0):
        odd_str += str1[i]

print(odd_str, "\n")

# 8: Write a Python program to count the occurrences of each word in a given sentence

str1 = "To change the overall look your document. To change the look available in the gallery"

import re 
split = re.split("[^\w|_]", str1)
result = {}

for i in split:
    if(i):
        result[i] = split.count(i)

print(result, "\n")

# 9: Write a Python script that takes input from the user and displays that input back in upper and lower cases.

# str1 = input("Insert an input: ")

print("Uppercase: {}\nLowercase: {}".format(str1.upper(), str1.lower()), "\n")


# 10. Write a Python function to reverse a string if it's length is a multiple of 4.

def reverse_if_four(str1) -> str:
    if(len(str1) % 4 == 0):
        return str1[::-1]
    else:
        return str1
    
print("Computer:", reverse_if_four("Computer"))
print("Science:", reverse_if_four("Science"), "\n")