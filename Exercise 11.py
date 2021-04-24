# Question 11
# Level 2

# Question:
# Write a program which accepts a sequence of comma separated 4 digit binary numbers as its input and then check whether they are divisible by 5 or not. The numbers that are divisible by 5 are to be printed in a comma separated sequence.
# Example:
# 0100,0011,1010,1001
# Then the output should be: 1010


nums = input().split(',')
new = []

try:
    for i in nums:
        if int(i, 2) % 5 == 0:
            new.append(i)
except ValueError:
    print('Values must be binary numbers')

if len(new) > 1:
    print(','.join(new))
else:
    for i in new:
        print(i)



