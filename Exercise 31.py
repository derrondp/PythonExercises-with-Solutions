# Question 31:
# Define a function that can accept an integer number as input and print the "It is an even number" if the number is even, otherwise print "It is an odd number".


def check(num):
    return "It is an even number" if num % 2 == 0 else "It is an odd number"


print(check(2))
print(check(3))