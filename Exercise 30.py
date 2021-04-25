# Question 30:
# Define a function that can accept two strings as input and print the string with maximum length in console. If two strings have the same length, then the function should print al l strings line by line.


def maxStr(s1, s2):
    if len(s1) == len(s2):
        return s1 + "\n" + s2
    return s1 if len(s1) > len(s2) else s2


print(maxStr("den", "ron"))