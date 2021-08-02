from xyz.supercoders.college.student_ops import get_details, get_grade

name = 'Mehul'
gender = 'm'
roll_no = 10
marks = 45


a = get_details(name, gender, roll_no, marks)
print(a)

grade = get_grade(marks)
print(grade)