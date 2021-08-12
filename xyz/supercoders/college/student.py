class Student:
  def get_details(self):
    # self - s1, s2, s3
    ''' return 'Name: ' + self.name + '\nGender: ' + self.gender \
    + '\nRoll: ' + str(self.roll) + '\nMarks: ' + str(self.marks) '''

    # return 'Name: {0}\nGender: {1}\nRoll: {2}\nMarks: {3}'.format(self.name, self.gender, self.roll, self.marks)
    return 'Name: {name}\nGender: {gender}\nRoll: {roll}\nMarks: {marks}'.format(name=self.name, roll=self.roll, gender=self.gender, marks=self.marks)

  def get_name_roll(self):
    return (self.name, self.roll)