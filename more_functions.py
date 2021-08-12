# Define a function `addition` that can take 0 to n inputs to be added and returns back the sum
# variable number of inputs
def addition(*numbers):
  # print(numbers) # tuple
  # all the inputs will be packed in a tuple
  return sum(numbers)


print(addition()) # 0
print(addition(54)) # 54
print(addition(3, 4, 5, 2, 1)) # 


# define perimeter_rectangle() such that it can be called only using function input names syntax
def perimeter_rectangle(**stats):
  # print(stats) # stats is a dict data structure
  # return 2 * (length + breadth)
  return 2 * (stats['length'] + stats['breadth'])


# print(perimeter_rectangle(7, 3))
print(perimeter_rectangle(length=7, breadth=3))
print(perimeter_rectangle(breadth=3, length=7))