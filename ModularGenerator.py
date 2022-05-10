# FInd the Smallest generator modular 7 that prints 1 as the first and last element 
g = 10
for i in range(7):
    print((g**i)%7)