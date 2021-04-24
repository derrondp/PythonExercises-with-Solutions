# Question 13
# Level 2

# Question:
# Write a program that accepts a sentence and calculate the number of letters and digits.
# Suppose the following input is supplied to the program:
# hello world! 123
# Then, the output should be:
# LETTERS 10
# DIGITS 3



s = input()

d, l = 0, 0

for i in s:
    if i.isdigit():
        d += 1
    elif i.isalpha():
        l +=1

if d != 0 or l != 0:
    print(f"LETTERS {l}\nDIGITS {d}")