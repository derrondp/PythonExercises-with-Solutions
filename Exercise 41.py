# Question 41:
# With a given tuple (1,2,3,4,5,6,7,8,9,10), write a program to print the first half values in one line and the last half values in one line. 


def genTuple():
    tup = tuple(i for i in range(10))
    print(str(tup[:5]))
    print(str(tup[5:]))


genTuple()