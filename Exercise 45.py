# Question 45:
# Write a program which can map() to make a list whose elements are square of elements in [1,2,3,4,5,6,7,8,9,10].


print(list(map(lambda x: x ** 2, [i for i in range(1, 11)])))