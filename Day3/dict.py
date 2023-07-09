"""
This data structure works with the key:value method, so there are not indexes for identifying 
the position
"""

my_dict={"c1":"value1","c2":"value2"}

print(my_dict["c1"])
"""
it can't be my_dict[0] because there is not a key 0 in the dict
"""

"""
we can take the keys and values data
"""

print(my_dict.keys())
print(my_dict.values())
print(my_dict.items())

my_dict["c3"]="value3"
print(my_dict)