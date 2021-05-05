# Question: 76

# Please write a program to output a random number, which is divisible by 5 and 7, between 0 and 10 inclusive using random module and list comprehension.


from random import choice

print(choice([i for i in range(11) if i % 5 == 0 and i % 7 == 0]))
