class Student:
  def __init__(self, name, roll_number, cgpa):
    self.name = name
    self.roll_number = roll_number
    self.cgpa = cgpa
def sort_students(student_list):
  sorted_students = sorted(student_list,
                           key=lambda student: student.cgpa,
                           reverse=True)
  return sorted_students
students = [
    Student("Dhinesh", "E1012", 9.9),
    Student("Sharan", "E1232", 7.6),
    Student("Kisshore", "E8975", 5.3),
    Student("Yaasar", "E1420", 8.0),
]
sorted_students = sort_students(students)
for student in sorted_students:
  print("Name: {}, Roll Number: {}, CGPA: {}".format(student.name,
                                                     student.roll_number,
                                                     student.cgpa))
