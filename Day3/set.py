"""
This is data structure used for data that can be repeated, it can contains tuple, but not 
dict or lists because they are mutable
"""

my_set={1,2,3,4}
my_list=[4,5,6,7]

print(set(my_list))

print(type(my_set))


"""
set doesnt accept item assignment
my_set[1]=2
"""