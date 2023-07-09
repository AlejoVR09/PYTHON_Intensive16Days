"""
Implicit cast of a variable, python do this for default
"""

num1=20
print(type(num1))

num2=20.2
print(type(num2))

num1=num1+num2
print(type(num1))

"""
Explicit cast of a variable
"""

num1=1.2
num1=int(num1)
print(type(num1))