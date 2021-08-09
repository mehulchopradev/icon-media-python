# empty list
el = []

# list storing the marks scored out of 10 in a class
marks = [5, 6, 5, 4, 7, 6, 10, 1]

# print(type(el))
# print(type(marks))
print(el)
print(marks)

# add a new student marks at the end in the marks list
marks.append(2)
print(marks)

# add a new student mark at the start of the list
marks.insert(0, 9)
print(marks)

# add a new student mark at position 3 in the list
marks.insert(2, 10)
print(marks)

# remove the last student from the list
print(marks.pop())
print(marks)

# remove the 2nd student from the list
print(marks.pop(1))
print(marks)


# add 3 new student marks at the end of the list
l = [5, 6, 4]

marks.extend(l)
print(marks)

# find out the count of people who have scored 10 marks from the list
p = marks.count(10)
for v in range(1, p+1):
  marks.remove(10)

print(marks)

''' marks.sort() # sorts the list in the ascending order
print(marks)

marks.reverse()
print(marks) '''

# sort the list in descending order
marks.sort(reverse=True)
print(marks)


# can feed a list to a for loop in python
cars = ['audi', 'bmw', 'mercedes']

# print each car from the list in upper case and on new line
for car in cars:
  print(car.upper())