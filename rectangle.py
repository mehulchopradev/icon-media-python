# User defined functions
def perimeter_rectangle(length, breadth):
  p = 2 * (length + breadth)
  return p

def area_rectangle(length, breadth):
  a = length * breadth
  return a

# input() -> str
# input() -> '4'
# input() -> '3.14'

# str -> int
l = int(input('Hey user, enter the length: ')) # '10' -> 10
b = int(input('Even enter the breadth: ')) # '4' -> 4

p = perimeter_rectangle(l, b)
ar = area_rectangle(l, b)

# Python has its own built in functions
# print

print('Perimeter is ' + str(p))
print('Area is ' + str(ar))