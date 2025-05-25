# arthematic operators

x = 10
y = 5

print(x+y)
print(x-y)
print(x*y)
print(x/y)
print(x//y) 
print(x%y)  
print(x**y) 

# comparison operators
print(x == y)
print(x != y)
print(x > y)
print(x < y)
print(x >= y)
print(x <= y)

# assignment operators
x += y  
x -= y  
x *= y  
x /= y  
x //= y  # x = x // y
x %= y  
x **= y  # x = x ** y



# logical operators
# and, or, not
print(x > 0 and y > 0) 
print(x > 0 or y < 0)  
print(not (x < 0))    

# membership operators
# in, not in
list1 = [1, 2, 3, 4, 5]
print(3 in list1)  
print(6 not in list1)

# identity operators
# is, is not
x = [1, 2, 3]
y = [1, 2, 3]
print(x is y)  
print(x is not y)