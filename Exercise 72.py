# Question 72:

# Please write a binary search function which searches an item in a sorted list. The function should return the index of element to be searched in the list.


# Hints:
# Use if/elif to deal with conditions.


def search(lst, val):
    left = 0
    right = len(lst) - 1

    while left <= right:
        middle = (left + right) // 2
        if lst[middle] > val:
            right = middle - 1
        elif lst[middle] < val:
            left = middle + 1
        else:
            return f"Index: {middle}"


nums = [2,3,4,8,10]
print(search(nums, 2)) 

