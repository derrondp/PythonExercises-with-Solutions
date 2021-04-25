# Question 46:
# Write a program which can map() and filter() to make a list whose elements are square of even numbers in [1,2,3,4,5,6,7,8,9,10].


print(list(map(lambda x: x ** 2, filter(lambda x: x % 2 == 0, [i for i in range(1, 11)]))))