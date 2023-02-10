# # 7 kyu You're a square!
# Task
# Given an integral number, determine if it's a square number:
# # In mathematics, a square number or perfect square is an integer
# # that is the square of an integer; in other words, it is
# # the product of some integer with itself.


def is_square(n: int):      # my solution
    if n < 0:
        return False
    if n == 0:
        return True
    return n**0.5 == round(n**0.5)


def cw_is_square(n):        # looks smarter
    return n > -1 and n**0.5 % 1 == 0


# # 6 kyu Detect Pangram
# A pangram is a sentence that contains every single letter of
# the alphabet at least once. For example, the sentence
# "The quick brown fox jumps over the lazy dog" is a pangram,
# because it uses the letters A-Z at least once (case is irrelevant).
# Given a string, detect whether or not it is a pangram.
# Return True if it is, False if not.
# Ignore numbers and punctuation.


def is_pangram(s: str):     # my solution
    alphabet = 'qwertyuiopasdfghjklzxcvbnm'
    for c in alphabet:
        if c not in s.lower():
            return False
    return True


def cw_is_pangram(s):       # not my solution, but looks good
    return set('qwertyuiopasdfghjklzxcvbnm').issubset(s.lower())


# # 7 kyu Disemvowel Trolls
# Trolls are attacking your comment section!
# A common way to deal with this situation is to remove all
# of the vowels from the trolls' comments, neutralizing the threat.
# Your task is to write a function that takes a string and
# return a new string with all vowels removed.
# For example, the string "This website is for losers LOL!"
# would become "Ths wbst s fr lsrs LL!".
# Note: for this kata y isn't considered a vowel.


def disemvowel(string_):    # my solution
    vowels = {'a', 'A', 'o', 'O', 'u', 'U', 'i', 'I', 'e', 'E'}
    for i in vowels:
        string_ = string_.replace(i, '')
    return string_


def cw_disemvowel(string):  # less strings but looks harders
    return "".join(c for c in string if c.lower() not in "aeiou")


# # 8 kyu Keep Hydrated!
# Nathan loves cycling.
# Because Nathan knows it is important to stay hydrated, he
# drinks 0.5 litres of water per hour of cycling.
# You get given the time in hours and you need to return the
# number of litres Nathan will drink, rounded to the smallest value.


def litres(time):           # only my perfect solution idk
    return time // 2


# # 8 kyu MakeUpperCase
# Write a function which converts the input string to uppercase.


def make_upper_case(s):     # only my perfect solution idk
    return s.upper()


# # 8 kyu Returning Strings
# Make a function that will return a greeting statement
# that uses an input; your program should return,
# "Hello, <name> how are you doing today?".


def greet(name):            # my first solution
    # Good Luck (like you need it)
    return 'Hello, ' + str(name) + ' how are you doing today?'


def cw_greet(name):         # enhanced, looks so beauty
    return f'Hello, {name} how are you doing today?'

# # 7 kyu Digit*Digit


def square_digits(num):     # my solution
    # Your code here
    output = ''
    for i in str(num):
        output += str(int(i) ** 2)
    return int(output)


def cw_square_digits(num):     # less strings
    return int(''.join(str(int(d)**2) for d in str(num)))
