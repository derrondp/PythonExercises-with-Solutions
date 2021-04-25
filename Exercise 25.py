# Question 25
# Level 1

# Question:
# Define a class, which has a parameter and an instance parameter.


class MyClass:
    name = "Derron's Class"

    def __init__(self, name=None):
        self.name = name


me = MyClass("Derron")
print(f"{MyClass.name}\'s name is {me.name}")