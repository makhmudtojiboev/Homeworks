import re

# def main():
#     user_input = input("Please enter your email: ")
#     check_email(user_input)

def check_email(email:str):
    pattern = r'^[a-zA-Z0-9][a-zA-Z0-9-._]*[a-zA-Z0-9]*\@[a-zA-Z][a-zA-Z]+\.[a-zA-Z][a-zA-Z]+$|[a-zA-Z0-9]\@[a-zA-Z][a-zA-Z]+.[a-zA-Z][a-zA-Z]+$'
    print("Your email:", list(re.findall(pattern, email))[0], "\n")
    before_at_last_index = email.find('@')
    dict_symbols = {'_' : 0, '%' : 0, '.' : 0, '-' : 0, '+' : 0}

    for i in email:
        if i == '_':
            dict_symbols[i] += 1
        elif i == '-':
            dict_symbols[i] += 1
        elif i == '.':
            dict_symbols[i] += 1
        else:
            pass

    check_if_not_consecutive_symbol = True

    for i in dict_symbols.values():
        if i > 1:
            check_if_not_consecutive_symbol = False

    if re.match(pattern, email) and len(email[:before_at_last_index]) <= 64 and check_if_not_consecutive_symbol:
        print("You can use this email!\n\n**************************\n")
    else:
        print("Oops, you cannot use this email, length is too big (more than 64) or you did not follow the validity format, please try again!\n\n**************************\n")
        # main()

email1 = 't2_-r'*50 +'@gmail.mm'
email2 = 'tojiboevm12@gmail.com'
email3 = 'toj_..2@aza.com'
email4 = 'toj_i.s@aza.com'
check_email(email1)
check_email(email2)
check_email(email3)
check_email(email4)


# re.findall(pattern, string, flags) -> Returns a list containing all matches
# re.split(pattern, string, maxsplit, flags) -> Returns a list where the string has been split at each match
# re.sub(pattern, repl, string, count, flags)	-> Replaces one or many matches with a string
# re.match() ->  checks if the pattern exists from the very start of the string
# re.search(pattern, string, flags) -> Returns a Match object if there is a match anywhere in the string (first occurence)

############# re.findall() #############

# pattern = '[0-5][a-z]ez'
# text = '4kez'
# print(re.findall(pattern, text))

# ############# re.split() #############
# # maxsplit -> third parameter in re.split(pattern, text, maxsplit)

# pattern = r'\s+' # split the string into list of substrings by white-space character(s)
# text = 'Hello my name is Makhmud'
# print(re.split(pattern, text))

# print(re.split(pattern, text, 2))
# print(re.split(pattern = pattern, string = text, maxsplit = 2))

# ############# re.search() #############

# # flags: (Optional) Modifiers like re.IGNORECASE, re.MULTILINE, etc., to change the behavior of the search.
# # group(): The matched substring.
# # start(): The starting position of the match.
# # end(): The ending position of the match.
# # span(): A tuple (start, end) representing the range of the match.

# pattern = r'\SD.$'
# text = 'sdas sdf'
# print(re.search(pattern, text, re.IGNORECASE)) # returns a Match Object -> <re.Match object; span=(5, 8), match='sdf'> span means from 5th to 7th index 
# match = re.search(pattern, text, re.IGNORECASE)
# print(match.group()) # returns matched substring
# print(match.start()) # returns starting index of the substring
# print(match.end())   # returns ending index of the substring
# print(match.span())  # returns tuple of (start, end) indexes of the substring

# ############# re.sub() #############

# pattern = 'bb|o' ## bb (or) o
# text = 'AbbOS'

# print(re.sub(pattern, '_', text, count = 2, flags = re.IGNORECASE)) # prints -> A__s

# ############# re.match() #############

# pattern = 'python'
# text1 = 'Python is the best!:)'
# text2 = 'Is it worth to learn Python?;)'

# result1 = re.match(pattern, text1, re.IGNORECASE)
# result2 = re.match(pattern, text2, re.IGNORECASE)
# print(result1.group())
# print(result2.group() if result2 else None)