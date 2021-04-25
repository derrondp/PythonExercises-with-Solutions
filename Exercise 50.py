# Question 50:
# Define a class named American and its subclass NewYorker. 


class American:
    def __init__(self):
        pass

    def printNationality(self):
        print("American")


class NewYorker(American):
    def __init__(self):
        pass

    def printNationality(self):
        print("NewYorker")
    

american = American()
american.printNationality()
newYorker = NewYorker()
newYorker.printNationality()