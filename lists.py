# animals = ["dog", "cat", "lion"]

# one_to_ten = list(range(11))

# print(animals)
# print("----------------")
# print(one_to_ten)

#List Comprehension

import math

even_list = [i*2 for i in range(20)]
for k in even_list:
    print(k, end=", ")
print()

num_list = [1,2,3,4,5]
list_of_powers = [[math.pow(m,2), math.pow(m,3), math.pow(m,4)] for m in num_list]

for p in list_of_powers:
    print(p, end=", ")
print()