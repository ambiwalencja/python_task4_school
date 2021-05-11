import sys


class Group:  # school class
    def __init__(self, tutor, students):
        self.tutor = tutor
        self.students = students  # list of tuples?

    def add_student(self, new_student):  # new_student comes from input
        self.student.append(new_student)

    def print_students(self):
        for first_name, last_name in self.students:
            print(first_name, last_name)


class Student:
    def __init__(self, group, first_name, last_name, subjects):
        self.group = group
        self.first_name = first_name
        self.last_name = last_name
        self.name = (first_name, last_name)
        self.subjects = subjects


class Tutor:
    def __init__(self, groups, first_name, last_name,):
        self.groups = groups
        self.first_name = first_name
        self.last_name = last_name
        self.name = (first_name, last_name)


class Teacher:
    def __init__(self, subject, first_name, last_name,):
        self.subject = subject
        self.first_name = first_name
        self.last_name = last_name
        self.name = (first_name, last_name)


#while True:
print("test")