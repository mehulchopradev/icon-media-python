'''
// Menu driven program
1. Even nos
2. Odd nos
3. Grade calculator
4. Exit
Please enter ur choice: 1
Please enter n: 5
0 2 4
1. Even nos
2. Odd nos
3. Grade calculator
4. Exit
Please enter ur choice: 2
Please enter n: 5
1 3 5
1. Even nos
2. Odd nos
3. Grade calculator
4. Exit
Please enter ur choice: 3
Please enter marks: 75
A
1. Even nos
2. Odd nos
3. Grade calculator
4. Exit
Please enter ur choice: 4
'''

from math import factorial

# from mathfunctions import even_nos, odd_nos
# import mathfunctions
import xyz.supercoders.lib.mathfunctions as mf
from xyz.supercoders.lib.school import grader

while True:
  print('1. Even nos')
  print('2. Odd nos')
  print('3. Grade calculator')
  print('4. Factorial')
  print('5. Exit')
  
  choice = int(input('Please enter ur choice: '))

  if choice == 5:
    break

  if choice == 1:
    n = int(input('Please enter n: '))
    mf.even_nos(n)
  elif choice == 2:
    n = int(input('Please enter n: '))
    mf.odd_nos(n)
  elif choice == 3:
    marks = float(input('Please enter ur marks: '))
    grader(marks)
  elif choice == 4:
    n = int(input('Please enter n: '))
    print(factorial(n))
  else:
    print('Heyy please enter choice 1 to 4')
