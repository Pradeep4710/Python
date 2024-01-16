# type casting -> Converting the datatype of a variable to another datatype.

x = 1 #int
y = 2.0 #float
z = "3" #string

print(x)
print(int(y)) #temporary typecast
print(type(y))

print(int(z)) #temporary typecast

y = int(y) #permanent typecast
print(type(y))

x = float(x) #permanent typecast
print(x)
print(type(x))

z = int(z) #permanent typecast
print(z)
print(type(z))