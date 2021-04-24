# Question 23
# level 1

# Question:
# Write a method which can calculate square value of number
# Handle Errors and make sure the program runs until the user provides the write input


def square(number):
    try:
        return round(int((number)) ** 2)
    except TypeError:
        return "Please input a number"
    except ValueError:
        return "Please input a number"


number = input("Enter num: ")
