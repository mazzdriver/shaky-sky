
# 7 kyu Digit*Digit

def square_digits(num):     # my solution
    # Your code here
    output = ''
    for i in str(num):
        output += str(int(i) ** 2)
    return int(output)


def square_digits(num):     # less strings
    return int(''.join(str(int(d)**2) for d in str(num)))
