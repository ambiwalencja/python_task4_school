ALLOWED_COMMANDS = ("student", "teacher", "tutor", "stop")
dict_of_students = {}  # global dictionary of students
dict_of_teachers = {}  # global dict of all teachers
dict_of_tutors = {}  # -//- tutors

# classes for all our types of objects: roles and groups:


class Group:  # school class: matching tutor is found in tutors' attributes, students are found in students' attr.
    def __init__(self):
        self.tutor = ''  # tutor's name - i will add it later if i can (?)
        self.students = []  # list of students in the class - i hope i can modify this list later

    def add_student(self, new_student):  # new_student comes from dict of students.
        self.students.append(new_student)

    def print_students(self):  # prints all students from the class - we need to print keys of dicts!
        for student in self.students:
            print(student)  # as well as i remember, this prints keys by default?


class Student:  # student: group given by user, subjects is found in teacher's attributes
    def __init__(self, nm, grp):
        self.group = grp
        self.name = nm
        self.subjects = []

    def add_student(self):
        dict_of_students[self.name] = {"group": self.group}  # each student is a key-value pair,
        # and the value is another dict with one key - group.

    def add_subjects(self):
        pass


#   def data(self):
#       student_data = {self.name: {"group": self.group, "subjects": self.subjects}}
#      return student_data


class Tutor:  # tutor: groups are given by the user, students will be found in group's attributes
    def __init__(self, nm, grps):
        self.name = nm
        self.groups = grps

    def add_tutor(self):
        dict_of_tutors[self.name] = {"groups": self.groups}

    # def add_student(self):
    # dict_of_students[self.name] = {"group": self.group}


class Teacher:  # teacher: subject and groups are given by the user, tutors are found in groups' attributes.
    def __init__(self, nm, sb, grps):
        self.name = nm
        self.subject = sb
        self.groups = grps

    # def data(self):
        # teacher_data = {self.name: {"subject": self.subject, "groups": self.groups}}
        # return teacher_data

    def add_teacher(self):
        dict_of_teachers[self.name] = {"subject": self.subject, "groups": self.groups}


while True:
    role = input("Type a role: ")
    if role not in ALLOWED_COMMANDS:
        print(f"allowed commands are: {ALLOWED_COMMANDS}")
        continue
    if role == "stop":
        break
    elif role == "student":
        name = input("Type name: ")
        group = input("Type group: ")
        student_object = Student(name, group)  # we create an object of a class Student with given params
        student_object.add_student()  # and we add it to the dictionary
        print(dict_of_students)
    elif role == "tutor":
        name = input("Type name: ")
        groups = []
        group = input("Type group: ")
        while group:
            groups.append(group)
            group = input("Type next group: ")
        tutor_object = Tutor(name, groups)
        tutor_object.add_tutor()
        print(dict_of_tutors)
    elif role == "teacher":
        name = input("Type name: ")
        subject = input("Type subject: ")
        groups = []
        group = input("Type group: ")
        while group:
            groups.append(group)
            group = input("Type next group: ")
        teacher_object = Teacher(name, subject, groups)
        teacher_object.add_teacher()
        print(dict_of_teachers)


# po wprowadzeniu wszystkich danych dokonujemy wszystkich niezbędnych uzupełnień?
# czy to niepotrzebne i dopiero robimy to, jak nam użytkownik każde? chyba to drugie.

# next the program will get a phrase and print results according to following scheme:
# <group_name>: tutor and students
# <tutor_name>: students of all tutor's groups
# <teacher_name>: tutors of all classes, the teacher has classes with
# <student_name>: all subjects and their teachers

