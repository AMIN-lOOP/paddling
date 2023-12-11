import math 

z, a, b, c, d, e, f = 1, 2, 3, 4, 5, 6, 7

diameter, length = 13, 12
diameterp, lengthp = 26, 20

aa = a * a  
dz = d - z  
ff = f * f  
abdf = (a + d + f) / a  
cd = (c * d) % d  
fdz = f * d + z  

g = math.sqrt(aa)
h = math.sqrt(dz)
i = math.sqrt(ff)
j = math.sqrt(fdz)
k = math.sqrt(z)

diameterSquare = diameter ** 2
lengthSquare = length ** 2
diameterSquarep = diameterp ** 2
lengthSquarep = lengthp ** 2

Height = math.sqrt(diameterSquare - lengthSquare)
Heightp = math.sqrt(diameterSquarep - lengthSquarep)

print(aa)
print(dz)
print(ff)
print(abdf)
print(cd)
print(fdz)
print(" ")  

print('height of triangle is:', Height)
print('height of triangle is:', Heightp)
print(" ") 

print('square root of number entered:', g)
print('square root of number entered:', h)
print('square root of number entered:', i)
print('square root of number entered:', j)
print('square root of number entered:', k)
