# Question 17
# Level 2

# Question:
# Write a program that computes the net amount of a bank account based a transaction log from console input. The transaction log format is shown as following:
# D 100
# W 200

# D means deposit while W means withdrawal.
# Suppose the following input is supplied to the program:
# D 300
# D 300
# W 200
# D 100
# Then, the output should be:
# 500

account = 0

while True:
    s = input()

    if not s:
        break

    vals = s.split(" ")
    mode = vals[0].upper()
    amount = int(vals[1])

    if mode == 'W':
        account -= amount
    elif mode == 'D':
        account += amount
    else:
        pass

    print(len(vals))

print(account)

    