ALLOWED_COMMANDS = ("student", "teacher", "tutor", "stop")
dict_of_students = {}  # global dictionary of students
dict_of_teachers = {}  # global dict of all teachers
dict_of_tutors = {}  # -//- tutors
dict_of_groups = {}

# classes for all our types of objects: roles and groups.


class Group:  # school class: matching tutor is found in tutors' attributes, students are found in students' attr.
    def __init__(self):
        self.tutor = ''
        self.students = []
        self.subjects = {}  # key - subject, value - teacher

    def add_student(self, new_student):  # new_student comes from dict of students.
        self.students.append(new_student)

    def print_students(self):  # prints all students from the class - we need to print keys of dicts!
        for student in self.students:
            print(student)  # as well as i remember, this prints keys by default?


class Student:  # student: group given by user, subjects is found in teacher's attributes
    def __init__(self):
        self.group = ''
        self.name = ''

    def get_person_data(self):
        self.name = input("Type name: ")
        self.group = input("Type group: ")

    def add_person(self):
        dict_of_students[self.name] = {"group": self.group}  # each student is a key-value pair,
        # and the value is another dict with one key - group.
        if self.group not in dict_of_groups:
            dict_of_groups[self.group] = Group()
        dict_of_groups[self.group].add_student(self)

    def print_person_data(self):
        group = dict_of_groups[self.group]
        for subject, teacher in group.subjects.items():
            print(subject, teacher.name)  # teacher is an object


class Tutor:  # tutor: groups are given by the user, students will be found in group's attributes
    def __init__(self, nm, grps):
        self.name = nm
        self.groups = grps

    def add_tutor(self):
        dict_of_tutors[self.name] = {"groups": self.groups}


class Teacher:  # teacher: subject and groups are given by the user, tutors are found in groups' attributes.
    def __init__(self):
        self.name = ''
        self.subject = ''
        self.groups = []

    def get_person_data(self):
        self.name = input("Type name: ")
        self.subject = input("Type subject: ")
        local_group = input("Type group: ")
        while local_group:  # we keep asking for next group until the user types enter
            self.groups.append(local_group)
            local_group = input("Type next group: ")

    def add_person(self):
        dict_of_teachers[self.name] = {"subject": self.subject, "groups": self.groups}

"""
def get_person_data(local_role):
    local_name = input("Type name: ")
    if local_role == 'teacher':  # for teacher we need a subject, the rest is the same for tutor and teacher
        local_subject = input("Type subject: ")
    local_groups = []
    local_group = input("Type group: ")
    while local_group:  # we keep asking for next group until the user types enter
        local_groups.append(local_group)
        local_group = input("Type next group: ")
    if local_role == 'teacher':
        return Teacher(local_name, local_subject, local_groups)
    return Tutor(local_name, local_groups)
"""

while True:
    role = input("Type a role: ")
    if role not in ALLOWED_COMMANDS:
        print(f"allowed commands are: {ALLOWED_COMMANDS}")
        continue
    if role == "stop":
        break
    if role == "student":
        person_object = Student()  # we create an object of a class Student with given params
        """
    elif role == "tutor":
        tutor_object = get_person_data(role)
        tutor_object.add_tutor()
        print(dict_of_tutors)
        """
    elif role == "teacher":
        person_object = Teacher()  # we create an object of a class Student with given params
    person_object.get_person_data()  # and we add it to the dictionary
    person_object.add_person()
    print(dict_of_students)
    print(dict_of_teachers)

# next the program will get a phrase and print results according to following scheme:
# <group_name>: tutor and students
# <tutor_name>: students of all tutor's groups
# <teacher_name>: tutors of all classes, the teacher has classes with
# <student_name>: all subjects and their teachers


print("Next action: type a name of a person (student, tutor or teacher) or a name of a class"
      "to get information.")
phrase = input("Type person's name: ")
while phrase:
    if phrase in dict_of_students:
        
        print("a student")
    elif phrase in dict_of_tutors:
        print("a tutor")
    elif phrase in dict_of_teachers:
        print('a teacher')
    else:
        print("a class")
    phrase = input("Type person's name: ")