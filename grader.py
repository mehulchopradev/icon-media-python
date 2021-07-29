''' 
>= 70 - A
>= 60 - B
>= 40 - C
< 40 - F
< 0 or > 100 - I
'''

marks = float(input('Student, please enter the marks scored: '))

# branching statements
'''
if <<some condition>>:
  I1
  I2
elif <<some condition>>:
  I3
  I4
  I5
elif <<some condition>>:
  I6
  I7
else:
  I8
  I9
'''

if marks < 0 or marks > 100:
  print('I')
elif marks >= 70:
  print('A')
  print('Congratulations')
elif marks >= 60:
  print('B')
elif marks >= 40:
  print('C')
else:
  print('F')