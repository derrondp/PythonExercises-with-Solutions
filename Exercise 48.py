# Question 48:
# Write a program which can map() to make a list whose elements are square of numbers between 1 and 20 (both included).


print(list(map(lambda x: x ** 2, filter(lambda x: x % 2 == 0, [i for i in range(1, 21)]))))