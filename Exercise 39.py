# Question 39:
# Define a function which can generate a list where the values are square of numbers between 1 and 20 (both included). Then the function needs to print all values except the first 5 elements in the list.


def genList():
    print([i ** 2 for i in range(1, 21)][5:])


genList()