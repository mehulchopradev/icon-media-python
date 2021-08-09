# store a student data together - name, gender, roll
student = ('mehul', 'm', 10)

print(type(student)) # class tuple
print(student)

# empty tuple
et = ()
print(type(et))

# single element tuple
s2 = ('jane',)
print(type(s2))

# most of the Object oriented methods that were there in a list, are not there in a tuple, since a tuple once created cannot be modified

# access elements from a tuple
print(student[0])
print(student[2])
print(student[-1])

# slice from a tuple
t = student[0:2]
print(t)

tt = student[-2:]
print(tt)


# size of a tuple
print(len(student))
print(len(et))

# a tuple can be fed directly to a for loop in python
for v in student:
  print(v)