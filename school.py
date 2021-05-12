ALLOWED_COMMANDS = ("student", "teacher", "tutor", "stop")
dict_of_students = {}  # global dictionary of students
dict_of_teachers = {}  # global dict of all teachers
dict_of_tutors = {}  # -//- tutors


class Group:  # school class
    def __init__(self, st):
        self.tutor = ''  # co tutaj, jeśli klasa ma wstępie może mieć pustego wychowawcę, a potem nadanego?
        self.students = st  # list of students in the class

    def add_student(self, new_student):  # new_student comes from input
        self.students.append(new_student)

    def print_students(self):  # prints all students from the class
        for student in self.students:
            print(student)


class Student:
    def __init__(self, nm, grp):
        self.group = grp
        self.name = nm
        self.subjects = []  # co tutaj, jeśli chcę, żeby domyślnie była to pusta lista, ale potem chcę ją móc wypełniać

    def add_student(self):
        dict_of_students[self.name] = {"group": self.group}  # each student is a key-value pair,
        # and the value is another dict with one key - group.

    def add_subjects(self):
        pass


#   def data(self):
#       student_data = {self.name: {"group": self.group, "subjects": self.subjects}}
#      return student_data


class Tutor:
    def __init__(self, grps, nm):
        self.groups = grps
        self.name = nm

    def data(self):
        tutor_data = {self.name: {"groups": self.groups}}
        return tutor_data

    # def add_student(self):
    # dict_of_students[self.name] = {"group": self.group}


class Teacher:
    def __init__(self, sb, nm, grps):
        self.subject = sb
        self.name = nm
        self.groups = grps

    # def data(self):
        # teacher_data = {self.name: {"subject": self.subject, "groups": self.groups}}
        # return teacher_data

    def add_teacher(self):
        dict_of_teachers[self.name] = {"subject": self.subject, "group": self.groups}


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
        # subjects = []
        # subject = input("Type subject: ")
        # while subject:
        # ####subjects.append(subject)
        # ####subject = input("Type next subject: ")
        student_object = Student(name, group)  # we create an object of a class Student with given params
        student_object.add_student()  # and we add it to the dictionary
        print(dict_of_students)
    if user == "teacher":
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
