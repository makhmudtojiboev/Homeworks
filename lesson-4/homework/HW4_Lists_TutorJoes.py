# 1: Write a Python program to sum all the items

list1 = [1,7,-10,34,2,-8]

print("Sum all the items =", sum(list1), "\n")

# 2: Write a Python program to multiply all the items in a list

list1 = [3,4,5,4,7]
multiply = 1

for i in list1:
    multiply = multiply * i

print("Multiplied result:", multiply, "\n")

# 3: Write a Python program to get the largest number from a list

list1 = [1,7,10,34,2,8]
max1 = list1[0]
for i in list1:
    if(i > max1):
        max1 = i

print("Maximum number:", max1, "\n")

# print(max(list1))

# 4: Write a Python program to get the smallest number from a list

list1 = [51,7,10,34,2,8]
minimum = list1[0]

for i in list1:
    if(i < minimum):
        minimum = i

print("Minimum number:",minimum, "\n")

# 5: Write a Python program to count the number of strings where the string length
#    is 2 or more and the first and last character are same from a given list of strings

list1 = ['abc', 'xyz', 'aba', '1221']
count = 0

for i in list1:
    if(len(i) >= 2 and i[0] == i[-1]):
        count += 1

print("First and Last Character are same:", count, "\n")

# 6: Write a Python program to remove duplicates from a list

list1 = [1,2,3,7,2,1,5,6,4,8,5,4, 3, 3,1,2]  # 1st option
no_duplicate = []
for i in range(len(list1)):
    if(list1[:i+1].count(list1[i]) == 1):
        no_duplicate.append(list1[i])

no_duplicate.sort()

print("Without duplicates:", no_duplicate, "\n")

# no_duplicate = set(list1)  # 2nd option
# print(no_duplicate)

# dup = set()                # 3rd option
# for i in list1:
#     if i not in dup:
#         dup.add(i)

# print(dup, "\n")

# 7: Write a Python program to check a list is empty or not

list1 = [34,45,6,5,4,56,7]

if (len(list1) == 0):
    print("String {} is empty".format(list1), "\n")
else:
    print("String {} is not empty".format(list1), "\n")

# 8: Write a Python program to clone or copy a list

from copy import deepcopy

list1 = [10, 22, 44, 23, 4]
copied_list1 = list1
copied_list2 = list1[:]
copied_list3 = list1.copy()    # shallow copy
copied_list4 = deepcopy(list1) # deep copy
copied_list5 = list(list1)

print("Original:", list1)
print("1st copied:", copied_list1)
print("2nd copied:", copied_list2)
print("3rd copied:", copied_list3)
print("4th copied:", copied_list4)
print("5th copied:", copied_list5, "\n")

# 9: Write a Python program to find the list of words that are longer than n from a given list of words

str1 = "Find the List of Words that are Longer than n from a given List of Words"
str1 = str1.split(" ")
n = 4
result = []

for i in str1:
    if(len(i) > n):
        result.append(i)

print(result, "\n")

# 10: Write a Program that get two lists as input and check if they have at least one common member

def check_common (list1, list2) -> str:
    for i in list1:
        if (i in list2):
            return "Lists have at least one common member"
    
    return "Lists don't have any common member"

str1 = [1,2,3,4,5]
str2 = [5,6,7,8,9]

print(check_common(str1, str2), "\n")

# 11: Write a Python program to print a specified list after removing the 0th, 4th and 5th elements. (enumerate)

# str1.extend([1,2,3,4])

str1 = ["Cat", "Dog", "Elephant", "Fox", "Tiger", "Lion", "Ponda"]
# str1.remove(str1[0])
# str1.remove(str1[4])
# str1.remove(str1[5])


########## 1st option ##########
result = []

for i in range(len(str1)):
    if(i not in (0, 4, 5)):
        result.append(str1[i])

print(result, "\n")

########## 2nd option ##########

# print(type(enumerate(str1))) # class enumerate
result = []

# for (i, x) in enumerate(str1):
#     if i not in (0, 4, 5):
#         result.append(x)

result = [x for (i, x) in enumerate(str1) if i not in (0, 4, 5)]

print(result, "\n")        

# 12: Write a Python program to print the numbers of a specified list after removing even numbers from it

list1 = [7,32,81,20,25,14,23,27]

for i in list1:
    if(i % 2 == 0):
        list1.remove(i)

# list1 = [i for i in list1 if i % 2 != 0 ]

print(list1, "\n")

# 13: Write a Python program to shuffle and print a specified list (shuffle)

from random import shuffle

list1 = ["Cat", "Dog", "Elephant", "Fox", "Tiger", "Lion", "Ponda"]

shuffle(list1)
print(list1, "\n")

# 14: Write a Python program to generate and print a list of first 
#     and last 5 elements where the values are square of numbers between 1 and 30

list1 = range(1, 30)

list2 = []

for i in list1:
    list2.append(i**2)

first_five = list2[:5]
# last_five = list2[len(list2) - 6:]
last_five = list2[-5:]

print("First 5 elements:", first_five)
print("Last 5 elements:", last_five, "\n")

# 15: Write a Python program to generate all permutations of a list in Python. (itertools)

from itertools import permutations 

list1 = [1,2,3]
result = list(permutations(list1))

print("Result:", result, "\n")

# 16: Write a Python program to convert a list of characters into a string

list1 = ['T','u','t','o','r',' ','J','o','e','s']

str1 = ""

# for i in list1:    # 1st option
#     str1 += i

str1 = "".join(list1)

print("String:", str1, "\n")

# 17: Write a Python program to find the index of an item in a specified list

######################## 1st option ########################
list1 = [20, 70, 30, 90, 10, 30, 90, 10, 80]
item_to_find = 30

for i in range(len(list1)):
    if(list1[i] == item_to_find):
        index = i
        break

print("Index number:", index, "\n")
######################## 2nd option ########################

list1 = [20, 70, 30, 90, 10, 30, 90, 10, 80]
item_to_find = 30

index = list1.index(item_to_find)
print("Index number:", index, "\n")

# 18: Write a Python program to flatten a shallow list

######################## 1st option ########################

list1 = [[20,30,70],[30,90,10], [30,20], [70,90,10,80]]
result = []

for i in list1:
    for a in i:
        result.append(a)

print("Result:", result, "\n")

######################## 2nd option ########################

from itertools import chain

list1 = [[20,30,70],[30,90,10], [30,20], [70,90,10,80]]
result = list(chain.from_iterable(list1))

print("Result:", result, "\n")

######################## 3rd option ########################

from itertools import chain

list1 = [[20,30,70],[30,90,10], [30,20], [70,90,10,80]]
result = list(chain(*list1))

print("Result:", result, "\n")

# 19: Write a Python program to add a list to the second list

######################## 1st option ########################

from itertools import chain

list1 = [10, 20, 30, 40]
list2 = ["Cat", "Dog", "Lion", "Ponda"]

result = list(chain(list1, list2))

print(result, "\n")

######################## 2nd option ########################

list1 = [10, 20, 30, 40]
list2 = ["Cat", "Dog", "Lion", "Ponda"]

result = list1 + list2

print(result, "\n")

# 20: Write a Python program to select an item randomly from a list Using random.choice()

from random import choice

list1 = ["Cat", "Dog", "Elephant", "Fox", "Tiger", "Lion", "Ponda"]

print("Random animal from {} is".format(list1), choice(list1), "\n")

# 21: Write a python program to check whether two lists are circularly identical

####### 1st option #######

list1 = [8, 8, 12, 12, 8]
list2 = [8, 8, 8, 12, 12]
list3 = [1, 8, 8, 12, 12]

def compare_circular_identity(list1, list2) -> bool:
    length = len(list1)
    cycled_list = []
    cycled_list.extend(list1)

    while (length >= 0):
        for i in range(len(list1)):
            if(i == 0):
                cycled_list[i] = list1[-1]
            else:
                cycled_list[i] = list1[i-1]
        if (cycled_list == list2):
            return True
        length -= 1
        list1 = cycled_list

    return False

print("{} => {}:".format(list1, list2),compare_circular_identity(list1, list2), "\n")
print("{} => {}:".format(list1, list3),compare_circular_identity(list1, list3), "\n")

####### 2nd option #######

list1 = [8, 8, 12, 12, 8]
list2 = [8, 8, 8, 12, 12]
list3 = [1, 8, 8, 12, 12]

print("{} => {}:".format(list1, list2), " ".join(map(str, list1)) in " ".join(map(str, list1 * 2)))
print("{} => {}:".format(list1, list3), " ".join(map(str, list1)) in " ".join(map(str, list1 * 2)), "\n")

# print(list(map(str, list1)))

# 22: Write a Python program to find the second smallest number in a list

list1 = [2, 2, 4,56,78,4,34,5,8,9]

dup = set()
unique_list = list()

for i in list1:
    if i not in dup:
        dup.add(i)
        unique_list.append(i)
unique_list.sort()

second_smallest = unique_list[1]

print("Second smallest:", second_smallest, "\n")

# 23: Write a Python program to find the second largest number in a list

list1 = [82,4,56,78,4,34,5,100,9]

dup = set()
unique_list = list()

for i in list1:
    if i not in dup:
        dup.add(i)
        unique_list.append(i)
unique_list.sort()

second_smallest = unique_list[-2]

print("Second largest:", second_smallest, "\n")

# 24: Write a Python program to get unique values from a list

list1 = [82, 4, 10, 56, 78, 4, 34, 5, 10, 9]

no_dup = set()
unique = []

for i in list1:
    if i not in no_dup:
        no_dup.add(i)
        unique.append(i)

print("Unique values of %s: %s" % (list1, unique), "\n")

# 25: Write a Python program to get the frequency of the elements in a list.

####### 1st option #######

list1 = [10, 30, 50, 10, 20, 60, 20, 60, 40, 40, 50, 50, 30]
mapping = dict()

for i in list1:
    mapping[i] = list1.count(i)

print(mapping, "\n")

####### 2nd option #######

import collections 
list1 = [10, 30, 50, 10, 20, 60, 20, 60, 40, 40, 50, 50, 30]

mapping_frequency = dict(collections.Counter(list1))

print(mapping_frequency)

# 26: Create a list by concatenating a given list which range goes from 1 to n

####### 1st option #######

list1 = ['T', 'J']
result = []
temp = list1.copy()
n = 10

for i in range(1, n + 1):
    for j in range(len(list1)):
        temp[j] = list1[j] + str(i)
    result.extend(temp)
        
print(result, "\n")

####### 2nd option #######

list1 = ['T', 'J']

result = ["{}{}".format(a, b) for b in range(1, n + 1) for a in list1]

print(result, "\n")

# 27: Write a Python program to get variable unique identification number or string

x = 30
s = "Tutor Joes"

print("Unique Identification Number of {}".format(x), id(x))
print("Unique Identification String of {}".format(s), id(s))


print(format(id(x), 'x'))
print(format(id(s), 'x'), "\n")

# 28: Write a Python program to find common items from two lists

### 1st option ###

list1 = [23,45,67,78,89,34]
list2 = [34,89,55,56,39,67]
match = []

for i in list1:
    for j in list2:
        if(i == j):
            match.append(i)

### 2nd option ###

print(match, "\n")

list1 = [23,45,67,78,89,34]
list2 = [34,89,55,56,39,67]

print(list(set(list1) & set(list2)), "\n")

# 29: Write a Python program to split a list based on the first character of word

### 1st option ###

list1 = ["cat", "dog", "cow", "tiger", "lion", "Fox", "Shark", "Snake", "turtle", "mouse", "monkey", "bear"]

mapping = set()

for i in list1:
    mapping.add(i[0])

mapping = list(mapping)
for i in mapping:
    print(i)
    for j in list1:
        if(i == j[0]):
            print("   ",j)
print(mapping)

### 2nd option ###

from itertools import groupby
from operator import itemgetter

list1 = ["cat", "dog", "cow", "tiger", "lion", "Fox", "Shark", "Snake", "turtle", "mouse", "monkey", "bear"]


# for letter, word in (groupby(sorted(list1), key = lambda x : x[0])):
for letter, word in (groupby(sorted(list1), key = itemgetter(0))):
    print(letter)
    for i in word:
        print(" ", i)

print()

# 30: Write a Python program to select the odd number of a list

### 1st option ###

list1 = [1,2,4,3,6,7,5,8,9,7,8,9,10]
unique = []
result = [i for i in list1 if i % 2 == 1 and (i not in unique and not unique.append(i))]

print(result, "\n")

### 2nd option ###

list1 = [1,2,4,3,6,7,5,8,9,7,8,9,10]

list1 = set(list1)
list1 = list(list1)

result = [i for i in list1 if i % 2 == 1]

print(result, "\n")

### 3rd option without uniqueness ###

list1 = [1,2,4,3,6,7,5,8,9,7,8,9,10]
result = [i for i in list1 if i % 2 == 1]

print(result, "\n")

# 31: Write a Python Program to count unique values inside a list

### 1st option ###

str1 = [10, 20, 30, 50, 80, 70, 70, 80, 10]
unique = set(str1)
count = len(unique)

print("No of unique items:", count)

### 2nd option ###

str1 = [10, 20, 30, 50, 80, 70, 70, 80, 10]
new_list = []
count = 0

for i in str1:
    if(i not in new_list):
        new_list.append(i)
        count += 1

print("No of unique items:", count, "\n")

# 32: Write a Python Program to List product excluding duplicates

list1 = [2, 1, 2, 4, 6, 4, 3, 2, 1]

unique_numbers = set(list1)
multiplication = 1

for i in unique_numbers:
    multiplication *= i

print("Duplication removal list product: %d" % multiplication, "\n")

# 33: Write a Python Program to Extract elements with Frequency greater than K
import collections

list1 = [4, 6, 4, 3, 3, 4, 3, 7, 8, 8]
k = 2

frequencies = dict(collections.Counter(list1))

list2 = []

for i, j in frequencies.items():
    if(j > 2):
        list2.append(i)

print(list2, "\n")

print(frequencies.items())

# 34: Write a Python Program to Test if List contains elements in Range

list1 = [4, 5, 6, 7, 3, 9, 10]

result = True
i, j = 3, 10

for i in list1:
    if i not in range(i, j):
        result = False

print("Does list contain all elements in range:", result)

list1 = [4, 5, 6, 7, 3, 9]

result = True
i, j = 3, 10

for i in list1:
    if i < i or i >= j:
        result = False

print("Does list contain all elements in range:", result)

# 35: Write a Python program to check if the list contains three consecutive common numbers in Python

list1 = [18, 18, 18, 6, 3, 4, 9, 9, 9]
consecutive_nums = set()

for i in range(len(list1) - 2 ):
    if(list1[i] == list1[i + 1] and list1[i] == list1[i + 2]):
        consecutive_nums.add(list1[i])
    
print(list(consecutive_nums))

# 36: Write a Python program to find the Strongest Neighbour

list1 = [10,20,30,20,30,400]
new_list = []

for i in range(len(list1) - 1):
    new_list.append(max(list1[i], list1[i+1]))

print(new_list)

# 37: Write a Python Program to print all Possible Combinations from the three Digits

from itertools import permutations 

list1 = [1,2,3]
result = list(permutations(list1))

print("Result:", result, "\n")

list1 = [1, 2, 3]
for i in range(3):
    for j in range(3):
        for k in range(3):
            if(i != j and i != k and j != k):
                print(list1[i], list1[j], list1[k])

# 38: Write a Python program to find all the Combinations in the list with the given condition

################ 1st option ################

list1 = ['Tutor Joes', ['Software', 'Computer'], ['Solution', 'Education']]

sep_list = []

result = []

for i in range(len(list1[1])):
    for j in list1:
        if(type(j) is not type(list1)):
            sep_list.append(j)
            print(type(j))
        else:
            sep_list.append(j[i])
    result.append(list(sep_list))
    sep_list.clear()

print(result, "\n")

################ 2nd option ################

val = ["Tutor Joes",["Software","Computer"],
			["Solution", "Education"]]
print("Original List : " + str(val))
a = 2
l = []
c = 0
while c <= a - 1:
	t = []
	for i in val:
		if not isinstance(i, list):
			t.append(i)
		else:
			t.append(i[c])
	c += 1
	l.append(t)

print(l, "\n")

# 39: Write a Python program to get all unique combinations of two Lists

from itertools import permutations

list1 = ['A', 'B', 'C']
list2 = [1, 2, 3]

result = []

permut = permutations(list1, len(list2))

for comb in permut:
    zipped = zip(comb, list2)
    result.append(list(zipped))

print(result, "\n")

# 40: Write a Python program to remove all the occurrences of an element from a list

############## 1st option ##############

list1 = [1, 3, 4, 6, 5, 1]
n = 1

for i in list1:
    if(n == i):
        list1.remove(n)

print(list1)

############## 2nd option ##############

list1 = [1, 3, 4, 6, 5, 1]
n = 1
removing_element = set()

removing_element.add(n)

list1 = set(list1)

result = list(list1 - removing_element)

print(result)

# 41: Write a Python Program to Remove Consecutive K element records

    

 