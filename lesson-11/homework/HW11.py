######################### FIRST TASK #########################

# 1. Write a Python function gcd(a, b) that calculates the greatest common divisor of a and b.

def gcd(a, b) -> int:
    small = min([a, b])
    big = max([a, b])
    greatest_divisor = [i for i in range(1, small + 1) if (small % i == 0) \
                        and big % i == 0]
    
    return greatest_divisor[-1]

print(gcd(20, 40))
print(gcd(20, 30))
print(gcd(10, 11))

# 2. Write a Python function find_all_trues(lst) that returns 
#    the indices of all Truevalues in a list of boolean values.

def find_all_trues(lst):
    return [i for i in range(len(lst)) if lst[i]]

print(find_all_trues([True, False, False, True, False, True]))

# 3. Write a Python function count_vowels(s) that counts the 
#    number of vowels in a string.

def count_vowels(s: str):
    count_list = [1 for i in s.lower() if i in {"a", "e", "i", "o", "u"}]
    count = len(count_list)
    return count

print(count_vowels("I love you babe"))

# 4. Write a Python function remove_duplicates(lst) 
#    that removes duplicates from a list while preserving the order.

def remove_duplicates(lst: list):
    result_set = set()
    result = [ i for i in lst if i not in result_set and not result_set.add(i)]
    return result

print(remove_duplicates([1, 2, 3, 5, 6, 2, 3, 8, 8, 9, 1]))

######################### SECOND TASK #########################

# SQL dagi concat_ws ni pythonda func qilib yozish
# Example: select CONCAT_WS(', ', city, state, country) from users

def concat_ws(separator: str, *args: str) -> str:
    result_string = args[0]
    for i in range(1, len(args)):
        result_string = result_string + separator + args[i]
    return result_string

print(concat_ws(" ", "Makhmud", "Tojiboev", "Axror o'g'li"))
        