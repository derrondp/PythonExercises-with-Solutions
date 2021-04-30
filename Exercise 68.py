# Question 68:

# Please write a program using generator to print the even numbers between 0 and n in comma separated form while n is input by console.

# Example:
# If the following n is given as input to the program:

# 10

# Then, the output of the program should be:

# 0,2,4,6,8,10

def gen(n):
    for i in range(n+1):
        yield i

n = int(input())
g = gen(n)

print(','.join(str(i) for i in [i for i in g] if i % 2 == 0))


# # ORRRR...
# print(','.join(str(i) for i in list(filter(lambda x: x % 2 == 0, [i for i in g]))))
