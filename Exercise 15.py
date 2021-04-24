# Question 15
# Level 2

# Question:
# Write a program that computes the value of a+aa+aaa+aaaa with a given digit as the value of a.
# Suppose the following input is supplied to the program:
# 9
# Then, the output should be:
# 11106

n = str(int(input()))
print(sum(int(n * i) for i in range(1,5)))

    # You could use this instead...
        # vals = [n * i for i in range(1,5)]
        # print(sum(int(x) for x in vals))
    #



    