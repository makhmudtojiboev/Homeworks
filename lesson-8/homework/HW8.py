########################### LIST EXERCISES ###########################

# https://pynative.com/python-list-exercise-with-solutions/

# Exercise 1. Reverse a list in Python

list1 = [100, 200, 300, 400, 500]

print(list1[::-1])

# Exercise 2: Concatenate two lists index-wise

list1 = ["M", "na", "i", "Ke"]
list2 = ["y", "me", "s", "lly"]
list3 = [i + j for i, j in zip(list1, list2)]

print(list3)

# Exercise 3: Turn every item of a list into its square

numbers = [1, 2, 3, 4, 5, 6, 7]
square_numbers = [i**2 for i in numbers]
print(square_numbers)

# Exercise 4: Concatenate two lists in the following order

list1 = ["Hello ", "take "]
list2 = ["Dear", "Sir"]

# result = [] # 1st option
# for i in list1:
#     for j in list2:
#         result.append(i + j)

result = [i + j for i in list1 for j in list2]

print(result)

# Exercise 5: Iterate both lists simultaneously

list1 = [10, 20, 30, 40]
list2 = [100, 200, 300, 400]

# for i in range(len(list1)): # 1st option
#     print(f"{list1[i]} {list2[len(list2) - 1 - i]}")

for i, j in zip(list1, list2[::-1]):
    print("{} {}".format(i, j))

# Exercise 6: Remove empty strings from the list of strings

list1 = ["Mike", "", "Emma", "Kelly", "", "Brad"]

# result = [i for i in list1 if i]
result = list(filter(None, list1))

print(result)

# Exercise 7: Add new item to list after a specified item

list1 = [10, 20, [300, 400, [5000, 6000], 500], 30, 40]

list1[2][2].append(7000)

print(list1)

# Exercise 8: Extend nested list by adding the sublist

list1 = ["a", "b", ["c", ["d", "e", ["f", "g"], "k"], "l"], "m", "n"]

# sub list to add
sub_list = ["h", "i", "j"]

list1[2][1][2].extend(sub_list)

print(list1)

# Exercise 9: Replace list’s item with new value if found

list1 = [5, 10, 15, 20, 25, 50, 20]

removable_value = 20
adding_value = 200

# result = [] # 1st option
# for i in list1:
#     if(removable_value == i and adding_value not in result):
#         result.append(adding_value)
#     else:
#         result.append(i)

index = list1.index(removable_value)

list1[index] = adding_value

print(list1)

# Exercise 10: Remove all occurrences of a specific item from a list.

list1 = [5, 20, 15, 20, 25, 50, 20]

# list1 = [i for i in list1 if i != 20] # 1st option

# for i in list1:  # 2nd option
#     if(i == 20):
#         list1.remove(i)

while 20 in list1:
    list1.remove(20)

print(list1)


########################### DICT EXERCISES ###########################

# https://pynative.com/python-dictionary-exercise-with-solutions/

# Exercise 1: Convert two lists into a dictionary

keys = ['Ten', 'Twenty', 'Thirty']
values = [10, 20, 30]
result = {}

for i, j in zip(keys, values):
    result[i] = j

print(result)

# Exercise 2: Merge two Python dictionaries into one

dict1 = {'Ten': 10, 'Twenty': 20, 'Thirty': 30}
dict2 = {'Thirty': 30, 'Fourty': 40, 'Fifty': 50}

# for i, j in dict2.items(): # 1st option
#     dict1[i] = j

# dict3 = dict1.copy() # 2nd option
# dict3.update(dict2)

dict3 = {**dict1, **dict2}

print(dict3)

# Exercise 3: Print the value of key ‘history’ from the below dict

sampleDict = {
    "class": {
        "student": {
            "name": "Mike",
            "marks": {
                "physics": 70,
                "history": 80
            }
        }
    }
}

print(sampleDict["class"]["student"]["marks"]["history"])

# Exercise 4: Initialize dictionary with default values

employees = ['Kelly', 'Emma']
defaults = {"designation": 'Developer', "salary": 8000}

# result = {} # 1st option
# for i in employees:
#     result[i] = defaults

result = dict.fromkeys(employees, defaults)

print(result)

# Exercise 5: Create a dictionary by extracting the keys 
# from a given dictionary

sample_dict = {
    "name": "Kelly",
    "age": 25,
    "salary": 8000,
    "city": "New york"}

# Keys to extract
keys = ["name", "salary"]

# result = {} #1st option
# for i in keys:
#     result[i] = sample_dict[i]

result = {i : sample_dict[i] for i in keys}

print(result)

# Exercise 6: Delete a list of keys from a dictionary

sample_dict = {
    "name": "Kelly",
    "age": 25,
    "salary": 8000,
    "city": "New york"
}

# Keys to remove
keys = ["name", "salary"]

# sample_dict = {i: j for i, j in sample_dict.items() if i not in keys} # 1st option

# for i in keys: # 2nd option
#     sample_dict.pop(i)

sample_dict = {i : sample_dict[i] for i in sample_dict.keys() - keys}

print(sample_dict)

# Exercise 7: Check if a value exists in a dictionary

sample_dict = {'a': 100, 'b': 200, 'c': 300}

# exists = False  # 1st option
# for i in sample_dict.values():
#     if(i == 200):
#         exists = True
#         break
# if(exists):
#     print("200 is present in a dict")
# else:
#     print("200 is not present in a dict")

if 200 in sample_dict.values():
    print("200 is present in a dict")
else:
    print("200 is not present in a dict")

# Exercise 8: Rename key of a dictionary

sample_dict = {
  "name": "Kelly",
  "age": 25,
  "salary": 8000,
  "city": "New york"
}

sample_dict["location"] = sample_dict.pop("city")

print(sample_dict)

# Exercise 9: Get the key of a minimum value from the following dictionary

sample_dict = {
  'Physics': 82,
  'Math': 65,
  'history': 75
}

# minimum = list(sample_dict.values())[0] # 1st option
# for i in sample_dict.values():          
#     if i < minimum:
#         minimum = i
# print(minimum)

print(min(sample_dict, key=sample_dict.get))

# Exercise 10: Change value of a key in a nested dictionary

sample_dict = {
    'emp1': {'name': 'Jhon', 'salary': 7500},
    'emp2': {'name': 'Emma', 'salary': 8000},
    'emp3': {'name': 'Brad', 'salary': 500}
}

sample_dict["emp3"]["salary"] = 8500

print(sample_dict)

########################### SET EXERCISES ###########################

# https://pynative.com/python-set-exercise-with-solutions/

# Exercise 1: Add a list of elements to a set

sample_set = {"Yellow", "Orange", "Black"}
sample_list = ["Blue", "Green", "Red"]

# for i in sample_list: # 1st option
#     sample_set.add(i)

sample_set.update(sample_list)

print(sample_set)

# Exercise 2: Return a new set of identical items from two sets

set1 = {10, 20, 30, 40, 50}
set2 = {30, 40, 50, 60, 70}

set3 = set1 & set2
# set3 = set1.intersection(set2) # 2nd option

print(set3)

# Exercise 3: Get Only unique items from two sets

set1 = {10, 20, 30, 40, 50}
set2 = {30, 40, 50, 60, 70}

# set1.update(set2) # 1st option
# set1.union(set2)  # 2nd option
set1 = set1 | set2
print(set1)

# Exercise 4: Update the first set with items that don’t exist in the second set

set1 = {10, 20, 30}
set2 = {20, 40, 50}

# set1 = set1 - set2    # 1st option
# set1.difference(set2) # 2nd option
set1.difference_update(set2)

print(set1)

# Exercise 5: Remove items from the set at once

set1 = {10, 20, 30, 40, 50}

removing_items = [10,  20, 30]
set1.difference_update(removing_items)

# set1 = set1 - set(removing_items) # 2nd option

# Exercise 6: Return a set of elements present in Set A or B, but not both

set1 = {10, 20, 30, 40, 50}
set2 = {30, 40, 50, 60, 70}

# set1.symmetric_difference_update(set2) # 1st option
# set1 = set1 ^ set2                     # 2nd option
set1 = set1.symmetric_difference(set2)

print(set1)

# Exercise 7: Check if two sets have any elements in common. If yes, display the common elements

set1 = {10, 20, 30, 40, 50}
set2 = {60, 70, 80, 90, 10}

# if set1.intersection(set2):  
#    print("Two sets have items in common {}".format(set1.intersection(set2)))  # 1st option

if set1.isdisjoint(set2):
    print("Two sets have no items in common")  
else:
    print("Two sets have items in common {}".format(set1.intersection(set2)))  


# Exercise 8: Update set1 by adding items from set2, except common items

set1 = {10, 20, 30, 40, 50}
set2 = {30, 40, 50, 60, 70}

set1.symmetric_difference_update(set2)

print(set1)

# Exercise 9: Remove items from set1 that are not common to both set1 and set2

set1 = {10, 20, 30, 40, 50}
set2 = {30, 40, 50, 60, 70}

# set3 = set1 - set2
# set1.difference_update(set3)  # 1st option

set1.intersection_update(set2)

print(set1)

########################### IF ELSE EXERCISES ###########################

# https://pynative.com/python-if-else-and-for-loop-exercise-with-solutions/

# Exercise 1: Print first 10 natural numbers using while loop

i = 1

while i < 11:
    print(i)
    i += 1

# Exercise 2: Print the following pattern

# 1 
# 1 2 
# 1 2 3 
# 1 2 3 4 
# 1 2 3 4 5


for i in range(1, 6):
    for j in range(i):
        print(j+1, end = " ")
    print()

# Exercise 3: Calculate sum of all numbers from 1 to a given number

# number = int(input("Enter number: "))
number = 10
result = 0
for i in range(1, number + 1):
    result = result + i
print("Sum is", result)

# Exercise 4: Print multiplication table of a given number

num = 2
for i in range(1, 11):
    print(num*i)

# Exercise 5: Display numbers from a list using a loop

numbers = [12, 75, 150, 180, 145, 525, 50]

result = []

for i in numbers:
    if i > 150 and i <= 500:
        continue
    if i > 500:
        break
    if i % 5 == 0:
        result.append(i)
print(result)

# Exercise 6: Count the total number of digits in a number

num = 75869
count = 0
for i in str(num):
    count += 1

print(count)

# Exercise 7: Print the following pattern

# 5 4 3 2 1 
# 4 3 2 1 
# 3 2 1 
# 2 1 
# 1

for i in range(5, 0, -1):
    for j in range(i, 0, -1):
        print(j, end =" ")
    print()
    
# Exercise 8: Print list in reverse order using a loop

list1 = [10, 20, 30, 40, 50]

# list1.reverse() # 1st option

# reversed(list1) # 2nd option
# for i in list1:
#     print(i)

for i in range(len(list1) - 1, -1, -1):
    print(list1[i])

# Exercise 9: Display numbers from -10 to -1 using for loop

for i in range(-10, 0):
    print(i)

# Exercise 10: Display a message “Done” after the successful execution of the for loop

for i in range(5):
    print(i)
else:
    print("Done!")

# Exercise 11: Print all prime numbers within a range

start = 25
end = 50

for i in range(start, end + 1):
    is_prime = True
    for j in range(2, 10):
        if i % j == 0 and i != j:
            break
    else:
        print(i)
    
# Exercise 12: Display Fibonacci series up to 10 terms: 0  1  1  2  3  5  8  13  21  34

n = 10

# fibonacci = [0, 1]   

# for i in range(n - len(fibonacci)):
#     fibonacci.append(fibonacci[-1] + fibonacci[-2])   # 1st option 

# for i in fibonacci:
#     print(i, end=" ")

num1, num2 = 0, 1

for i in range(n):
    print(num1, end = " ")
    res = num1 + num2

    num1 = num2
    num2 = res
print()

# Exercise 13: Find the factorial of a given number

number = 5

if number < 0:
    print("Wrong input, factorial must be more or equal to zero")
elif number == 0:
    print("The factorial of zero is 1")
else:
    factorial = 1

    for i in range(number, 0, -1):
        factorial *= i

    print(factorial)

# Exercise 14: Reverse a integer number

number = 76542

# reversed_number = int(str(number)[::-1]) # 1st option

reversed_number = 0

while number > 0:
    remainder = number % 10
    reversed_number = (reversed_number * 10) + remainder
    number = number // 10

print(reversed_number)

# 15: Exercise 15: Print elements from a given list present at odd index positions

my_list = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

# for i in range(len(my_list)):     # 1st option
#     if i % 2 != 0:
#         print(my_list[i], end = " ")

for i in my_list[1::2]:
    print(i, end = " ")
print()

# Exercise 16: Calculate the cube of all numbers from 1 to a given number

input_number = 6

for i in range(1, input_number + 1):
    print("Current number is :", i, "and the cube is", i**3)

# Exercise 17: Find the sum of the series up to n terms

n = 5
number = 2
new_number = 0
sum_sequence = 0

for i in range(n):
    new_number = new_number*10 + number
    sum_sequence += new_number
    if i != n - 1:
        print(new_number, end = " + ")
    elif i == n - 1:
        print(new_number, end = " = ")
    else:
        print(sum_sequence)

print(sum_sequence)

# Exercise 18: Print the following pattern 

# * 
# * * 
# * * * 
# * * * * 
# * * * * * 
# * * * * 
# * * * 
# * * 
# *

for i in range(1, 10):
    if(i <= 5):
        print("*" * i)
    else:
        print("*" * (10 - i))


########################### TUPLE EXERCISES ###########################

# https://pynative.com/python-tuple-exercise-with-solutions/

# Exercise 1: Exercise 1: Reverse the tuple

tuple1 = (10, 20, 30, 40, 50)
# tuple1 = reversed(tuple1) # 1st option
tuple1 = tuple1[::-1]

print(tuple(tuple1))

# Exercise 2: Access value 20 from the tuple

tuple1 = ("Orange", [10, 20, 30], (5, 15, 25))

print(tuple1[1][1])

# Exercise 3: Create a tuple with single item 50

tuple1 = 50, # or tuple1= (50, )

print(tuple1)

# Exercise 4: Unpack the tuple into 4 variables

tuple1 = (10, 20, 30, 40)

a, b, c, d = tuple1
a, b, c, d = 10, 20, 30, 40 # the same

print(a)
print(b)
print(c)
print(d)

# Exercise 5: Swap two tuples in Python

tuple1 = (11, 22)
tuple2 = (99, 88)

tuple1, tuple2 = tuple2, tuple1

print("tuple1:", tuple1)
print("tuple2:", tuple2)

# Exercise 6: Copy specific elements from one tuple to a new tuple

tuple1 = (11, 22, 33, 44, 55, 66)

tuple2 = tuple1[3:5]

print("tuple2:", tuple2)

# Exercise 7: Modify the tuple

tuple1 = (11, [22, 33], 44, 55)

# for i in tuple1:
#     if type(i) is list:
#         for j in range(len(i)):
#             if i[j] == 22:
#                 i.remove(22)
#                 i.insert(j, 222) # 1st option

tuple1[1][0] = 222

print(tuple1)

# Exercise 8: Sort a tuple of tuples by 2nd item

tuple1 = (('a', 23),('b', 37),('c', 11), ('d',29))

# sorted_2nd = sorted([i[1] for i in tuple1])                    # 1st option
# sorted_tuple = tuple([j  for i in sorted_2nd for j in tuple1 if i == j[1]]) 

sorted_tuple = tuple(sorted(list(tuple1), key = lambda x: x[1]))

print(sorted_tuple)

# Exercise 9: Counts the number of occurrences of item 50 from a tuple

tuple1 = (50, 10, 60, 70, 50)

# count = 0
# for i in tuple1:
#     if i == 50:
#         count += 1
# print(count)            # 1st option

print(tuple1.count(50))

# Exercise 10: Check if all items in the tuple are the same

tuple1 = (45, 45, 45, 45)

print(True if tuple1.count(tuple1[0]) == len(tuple1) else False)
# print(all(tuple1[0] == i for i in tuple1)) # 2nd option