# 1. **Convert Types:**
#     Write a program that:
#         1. Takes a number as input (as a string).
#         2. Converts it to an integer using int().
#         3. Converts the same input to a float using float().
#         4. Prints both converted values along with their types.
print("Problem #1")
number_string = input("Enter the number: ")
number_int = int(number_string)
number_float = float(number_string)
print("Integer: ", number_int, "\nFloat: ", number_float, "\n\n")

# 2. **Working with Numeric Functions:**
#      Write a program that:
#          1. Accepts two numbers from the user.
#          2. Prints the result of divmod() on these numbers.
#          3. Finds the absolute difference between the two numbers using `abs()`.
print("Problem #2")
two_numbers = input("Input the two numbers, example: \"a b\" -> ")
a = int(two_numbers[0])
b = int(two_numbers[2])
print("divmod(" + str(a) + ", " + str(b) + "): ", divmod(a, b))
print("Absolute difference: ", abs(a - b), "\n\n")

# 3.  **String Length and Case Conversion:**
    #  Write a program that:
    #     1. Takes a string input from the user.
    #     2. Prints the length of the string using len().
    #     3. Converts the string to lowercase using .lower() and prints the result.
print("Problem #3")
user_input = input("Input any text: ")
input_length = len(user_input)
lower_string = user_input.lower()

print("Length of the input: ", input_length)
print("Input in the lowercase letters: ", lower_string, "\n\n")

# 4.  **Power Calculation:**
    #  Write a program that:
    #     1. Accepts a base number, an exponent, and a modulus from the user.
    #     2. Calculates (base ** exponent) % modulus using pow().
    #     3. Prints the result.
print("Problem #4")
base_number = int(input("Enter the base number: "))
exponent = int(input("Enter the exponent: "))
modulus = int(input("Enter the modulus: "))

print("Result of using pow() function: ", pow(base_number, exponent, modulus), "\n\n")

# 5.  **String Escape Sequences:**
    #  Write a program that:
    #     1. Prints a sentence that includes a newline (\n), a tab (\t), and a double quote (\") in the same string.
print("Problem #5")
print('''Hello dear sir, \n\n \t\b\b\b\b 1. I need to apologize for yesterday's occasion
      \n\t\b\b\b\b 2. I don't accept your excuses like \"I am sorry\"\n\nBest regards\nMakhmud Tojiboev\n\n''')

# 6.  **String Indexing:**
    #  Write a program that:
    #     1. Accepts a string input from the user.
    #     2. Prints the first, last, and third characters of the string using indexing.
    #     3. Handles cases where the string is shorter than 3 characters.
print("Problem #6")
s_input = input("Enter the 3 or more character string: ")
if(len(s_input) >= 3):
    print("First character: ", s_input[0], "\nThird character: ", s_input[2], "\nLast character: ", s_input[len(s_input) - 1], "\n\n")
else:
    print("Your string is too short, make it the size of three or more characters, thanks!\n\n")

# 7.  **Type Identification:**
    #  Write a program that:
    #     1. Accepts input from the user (it can be a number or text).
    #     2. Identifies whether the input is an integer, float, or string using type().
    #     3. Prints the identified type.
print("Problem #7")
type_input = input("Enter the input: ")
try:
    input_result = int(type_input)
    print("This type is integer\n\n")
except:
    try:
        input_result = float(type_input)
        print("This type is float\n\n")
    except:
        print("This type is string\n\n")

# 8.  **Immutable and Mutable:**
#      Write a program that:
#         1. Accepts a string input from the user.
#         2. Tries to modify a character in the string using indexing and handles the resulting error gracefully.
#         3. Prints a message explaining why the error occurred.
print("Problem #8")
string_input = input("Input the string: ")
try:
    string_input[0] = 'G'
except:
    print("Strings are immutable data types, and cannot be modified\n\n")

# 9.  **Basic Arithmetic:**
#      Write a program that:
#         1. Takes two numbers as input.
#         2. Calculates and prints the results of addition, subtraction, multiplication, division (/), integer division (//), and modulo (%).
print("Problem #9")
a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))
print("\nAddition: ", a + b)
print("Substraction: ", a - b)
print("Multiplication: ", a * b)
print("Division: ", a / b)
print("Integer division: ", a // b)
print("Modulo: ", a % b, "\n\n")

# 10.  **Multi-line Strings:**
    #  Write a program that:
    #     1. Creates a multi-line string using triple quotes (""").
    #     2. Prints the string.
    #     3. Calculates the number of characters in the string using len() and prints the result.
print("Problem #10")
multiline_string = """I am learning Python
Left is not always a good choice"""
print("String: " + multiline_string)
print("Number of characters: ", len(multiline_string))