# Question 52:
# Define a class named Rectangle which can be constructed by a length and width. The Rectangle class has a method which can compute the area. 


class Rectangle:
    def __init__(self, length, width):
        self.width = width
        self.length = length
    
    def area(self):
        return self.length * self.width
    

r = Rectangle(2, 2)
print(r.area())