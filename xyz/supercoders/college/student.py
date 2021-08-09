class Student:
  def get_details(self):
    # self - s1, s2, s3
    return 'Name: ' + self.name + '\nGender: ' + self.gender \
    + '\nRoll: ' + str(self.roll) + '\nMarks: ' + str(self.marks)

  def get_name_roll(self):
    return (self.name, self.roll)