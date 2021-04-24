# Question 20
# Level 3

# Question:
# Define a generator function which can iterate the numbers, which are divisible by 7, between a given range 0 and n.


def GenObj(n):
    for i in range(n):
        if i % 7 == 0:
            yield i

genobj = GenObj(80)
for i in genobj:
    print(i)



#   I TRIED DOING IT WITH A CLASS, DIDN'T WORK OUT TOO WELL
        # class Gen:
        #     def __init__(self,n):
        #         self.n = n
        #         self.i = 0
            
        #     def __next__(self):
        #         return self.next()
            
        #     def next(self):
        #         if self.i == self.n:
        #             raise StopIteration()
                
        #         self.i += 1
        #         if self.i % 7 == 0:
        #             return self.i


# genClass = Gen(80)
# while True:
#     try:
#         print(next(genClass))
#     except StopIteration:
#         break