# Question 69:

# Please write a program using generator to print the numbers which can be divisible by 5 and 7 between 0 and n in comma separated form while n is input by console.

# Example:
# If the following n is given as input to the program:

# 100

# Then, the output of the program should be:

# 0,35,70

def Gen(n):
    for i in range(n+1):
        yield i


n = int(input())
print(','.join(str(i) for i in [i for i in Gen(n)] if i % 5 == 0 and i % 7 == 0))

# # ORRRR...
# print(','.join(str(i) for i in list(filter(lambda x: x % 5 == 0 and x % 7 == 0, [i for i in Gen(n)]))))
