from statistics import median

# Read from a file line by line

# connect to a file on the file system

file = open('data/employees.csv', encoding='utf-8')

# read line by line from the file
''' for line in file:
  print(line) '''

# reading all lines together from the file
''' lines = file.readlines()
print(lines) '''

# read all the contents of the file together in an str object
''' data = file.read()
print(data) '''

# find out the median salary amongst the entire group
lines = file.readlines()
lines_2 = lines[1:]

salaries = []
gender_salaries = {}
# {
#   'm': [560, 700, 8000]
#   'f': [700, 500, 600, 700]
# }

for line in lines_2:
  l = line.rstrip() # remove the line break \n from the line
  tokens = l.split(',')
  salaries.append(int(tokens[-1]))

  gender = tokens[-2]
  if gender not in gender_salaries:
    gender_salaries[gender] = [int(tokens[-1])]
  else:
    es = gender_salaries[gender]
    es.append(int(tokens[-1]))

print(salaries)
print(gender_salaries)

print(median(salaries))

fwrite = open('gender_media_salaries.csv', mode='w', encoding='utf-8')

# find out the median salary grouped by gender
for gender in gender_salaries:
  ms = median(gender_salaries[gender])
  fwrite.write('{0},{1}\n'.format(gender, ms))

fwrite.close() # otherwise you will just see an empty file!
file.close() # always good to close the file resources
  