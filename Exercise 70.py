# Question 70:

# Please write assert statements to verify that every number in the list [2,4,6,8] is even.


l = [0,1,2,3,4]

for i in l:
    try:
        assert i % 2 == 0
    except AssertionError:
        print(str(i),"is not even")