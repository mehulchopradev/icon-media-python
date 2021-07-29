n = int(input('Enter a number: '))

# i = 0
# while loop
''' while i <= n:
  if i % 2 == 0:
    print(i)
  i = i + 1 '''

# for loop
'''
  for i in <<sequence of elements>>:
    I1
    I2
    I3
'''

# 0 to n
# n -> 10 : 0 to 10 : (0, 1, 2, 3,....., 10)
# n -> 5 : 0 to 5: (0, 1, 2, 3, 4, 5)
# n : 23 -> (0, 23)

for i in range(0, n + 1): # (0, 23)
  if i % 2 == 0:
    print(i)