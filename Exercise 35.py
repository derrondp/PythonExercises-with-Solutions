# Question 35:
# Define a function which can generate a dictionary where the keys are numbers between 1 and 20 (both included) and the values are square of keys. The function should just print the keys only.


def printDict():
    d = {}

    for i in range(1, 21):
        d[i] = i ** 2
    
    for k, v in d.items():
        print(k)


printDict()