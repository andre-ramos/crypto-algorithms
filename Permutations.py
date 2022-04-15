from itertools import permutations
import cProfile

my_list = [1,2,3]
list_of_permutations = permutations(my_list)
count = 0
for permutation in list_of_permutations:
    count += 1

def recursive(n):
    if n <= 1:
        return n
    else:
        return n * recursive(n-1)

print(len(my_list), count)


cProfile.run("print(recursive(765))")