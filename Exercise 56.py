# Question: 56
# Define a custom exception class which takes a string message as attribute.


class Error(Exception):
    def __init__(self, message):
        self.message = message
    

error = Error("Error occured!")