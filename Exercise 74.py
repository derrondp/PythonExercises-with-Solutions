# Question 74:

# Please generate a random float where the value is between 5 and 95.


import random

num = random.choice([random.random() * i for i in range(6, 96)])
print(num)