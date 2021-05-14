# Question 84:

# Please write a program to generate all sentences where the subject is in ["I", "You"], the verb is in ["Play", "Love"] and the object is in ["Hockey","Football"].


subject = ["I", "You"]
verb = ["Play", "Love"]
object = ["Hockey", "Football"]


for i in subject:
    for j in verb:
        for k in object:
            print(f"{i} {j} {k}")