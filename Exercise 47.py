# Question 47:
# Write a program which can filter() to make a list whose elements are even number between 1 and 20 (both included).


print(list(filter(lambda x: x % 2 == 0, [i for i in range(1, 21)])))