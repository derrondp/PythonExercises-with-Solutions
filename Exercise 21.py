# Question 21
# Level 3

# Question��
# A robot moves in a plane starting from the original point (0,0). The robot can move toward UP, DOWN, LEFT and RIGHT with a given steps. The trace of robot movement is shown as the following:
# UP 5
# DOWN 3
# LEFT 3
# RIGHT 2
# ��
# The numbers after the direction are steps. Please write a program to compute the distance from current position after a sequence of movement and original point. If the distance is a float, then just print the nearest integer.
# Example:
# If the following tuples are given as input to the program:
# UP 5  y
# DOWN 3    y
# LEFT 3    x
# RIGHT 2   x
# Then, the output of the program should be:
# 2
import math

pos = [0, 0]

while True:
    s = input()
    if not s:
        break
    
    moves = s.split(" ")
    direction = moves[0].upper()
    steps = int(moves[1])

    if direction == 'UP':
        pos[1] += steps
    elif direction == 'DOWN':
        pos[1] -= steps
    elif direction == 'LEFT':
        pos[0] -= steps
    elif direction == 'RIGHT':
        pos[0] += steps
    else:
        pass


distance = int(math.sqrt(pos[0] ** 2 + pos[1] ** 2))
if type(distance) == float:
    print(round(distance))
else:
    print(distance)


    