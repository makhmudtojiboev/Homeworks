
#################### SUM() ####################

def sum(a):
    addition = 0
    for i in a:
        addition += i
    return addition


list1 = [1, 2, 3, 4, 5]

print(sum(list1))

#################### POW() ####################

def pow(a, b):
    power = 1
    while b > 0:
        power = power * a
        b -= 1
    return power

print(pow(4, 2))
        
#################### MAX() ####################

def max(a):
    maximum = a[0]
    for i in a:
        if maximum < i:
            maximum = i
    return maximum

print(max(list1))

#################### MIN() ####################

def max(a):
    minimum = a[0]
    for i in a:
        if minimum > i:
            minimum = i
    return minimum

print(max(list1))

#################### LEN() ####################

def len(a):
    length = 0
    for i in a:
        length += 1

    return length

print(len(list1))

#################### ZIP() ####################

def zip(*args: iter):
    length = len(args[0])
    number_iterables = len(args)
    list1 = []
    for i in range(number_iterables):
        list1 += args[i]

    list2 = []
    final_list = []
    for i in range(length):
        for j in range(number_iterables):
            list2.append(args[j][i])
        final_list.append(tuple(list2))
        list2.clear()

    return final_list

# print(zip([1, 2, 3], [2, 3, "he"], [2, 3, "go"], [3, 4, "you"]))

#################### enumerate() ####################

def enumerate(a, start_index = 0):
    list1 = list()
    for i in a:
        tuple1 = (start_index, i)
        list1.append(tuple1)
        start_index += 1

    return list1
    
# print(enumerate([1, 2, 3, 4], 4))

print(list(range(1, 5)))

def range(first, second = 0, by = 1):
    result = list()

    if second == 0:
        element = 0
        while ( element < first):
            result.append(element)
            element += by
    else:
        element = first
        while ( element < second):
            result.append(element)
            element += by

    return result

# print(range(5, 88, 2))


    
        
        
        


        

