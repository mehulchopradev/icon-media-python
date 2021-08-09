from xyz.supercoders.college.student import Student


s1 = Student()
s1.name = 'mehul'
s1.roll = 10
s1.gender = 'm'
s1.marks = 90


s2 = Student()
s2.name = 'jane'
s2.roll = 14
s2.gender = 'f'
s2.marks = 89

''' print(s1)
print(s2)
print(type(s1))
print(type(s2)) '''

''' print(s1.name)
print(s1.gender)

print(s2.name)
print(s2.gender) '''


print(s1.get_details())
# Python internally
# print(Student.get_details(s1))


print(s2.get_details())
# Python internally
# print(Student.get_details(s2))



# print(s1.get_grade())
# print(s2.get_grade())

t = s1.get_name_roll()
print(t[0])
print(t[1])