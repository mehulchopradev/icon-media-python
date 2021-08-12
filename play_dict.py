# dictionary of student data

ed = {}
print(type(ed))
print(ed)

student_data = {10:('mehul', 'm'), 3:('jane', 'f')} # know the data at the time of creating the dict
print(student_data)
print(type(student_data))

# add a new student to the above dict
student_data[34] = ('jill', 'f')
print(student_data)

# update an existing student in the above dict
student_data[3] = ('john', 'm')
print(student_data)

# check whether a student existing in the dict or no
print(100 in student_data)
print(34 in student_data)

# get student data from a dict by roll no
print(student_data[3])

if 100000 in student_data:
  print(student_data[100000])
else:
  print('Student not found')

# number of students there in the dict
print(len(student_data))

# remove a student from dict by roll no
print(student_data.pop(10))
print(student_data)

# remove student with roll 34
del student_data[34]
print(student_data)

student_data[34] = ('jill', 'f')
student_data[10] = ('mehul', 'm')
print(student_data)

# write logic to print the roll number and name of all the students there in the dict
# Roll: 3, Name: john
# Roll: 34, Name: jill
# Roll: 10, Name: mehul

# prints by default the keys from the dict
for v in student_data:
  print(v)

items = student_data.items()
print(items)
for item in items:
  roll = item[0]
  name = item[1][0]
  gender = item[1][1]
  print('Roll: ', roll, ',', 'Name: ', name, gender)
