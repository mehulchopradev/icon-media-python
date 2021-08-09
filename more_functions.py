# Define a function `addition` that can take 0 to n inputs to be added and returns back the sum
# variable number of inputs
def addition(*numbers):
  # print(numbers) # tuple
  # all the inputs will be packed in a tuple
  return sum(numbers)


print(addition()) # 0
print(addition(54)) # 54
print(addition(3, 4, 5, 2, 1)) # 