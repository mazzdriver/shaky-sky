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
