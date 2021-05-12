import sys

ALLOWED_COMMANDS = ("student", "stop")
list_of_students = []  # global list of dicts?


class Group:  # school class
    def __init__(self, t, s):
        self.tutor = t
        self.students = s  # list of ???


#   def add_student(self, new_student):  # new_student comes from input
#       self.students.append(new_student)

#   def print_students(self):
#      for first_name, last_name in self.students:
#          print(first_name, last_name)


class Student:
    def __init__(self, nm, grp, sbjct):
        self.group = grp
        # self.first_name = first_name
        # self.last_name = last_name
        self.name = nm
        self.subjects = sbjct

    def data(self):
        student_data = {self.name: {"group": self.group, "subjects": self.subjects}}
        return student_data


class Tutor:
    def __init__(self, groups, nm):
        self.groups = groups
        self.name = nm


class Teacher:
    def __init__(self, sbjct, nm):
        self.subject = sbjct
        self.name = nm


while True:
    user = input("Type a user: ")
    if user not in ALLOWED_COMMANDS:
        print(f"allowed commands are: {ALLOWED_COMMANDS}")
        continue
    if user == "stop":
        break
    if user == "student":
        name = input("Type name: ")
        group = input("Type group: ")
        subjects = []
        subject = input("Type subject: ")
        while subject:
            subjects.append(subject)
            subject = input("Type next subject: ")
        student_object = Student(name, group, subjects)
        list_of_students.append(student_object.data())
        print(list_of_students)
