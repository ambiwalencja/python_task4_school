ALLOWED_COMMANDS = ("student", "teacher", "tutor", "stop")
dict_of_elements = {}
# classes for all our types of objects: roles and groups.


class Group:  # school class: matching tutor is found in tutors' attributes, students are found in students' attr.
    def __init__(self):
        self.tutor = ''
        self.students = []  # is it a list of objects of a class Student ?
        self.subjects = {}  # key - subject, value - teacher

    def add_student(self, new_student):  # new_student comes from input and it is an object of a class Student.
        self.students.append(new_student)

    def print_info(self):
        print(f'Group tutor is: {self.tutor} \n'
              f'Students:')
        for student in self.students:
            print(student.name)


class Student:  # student: group given by user, subject is found in teacher's attributes
    def __init__(self):
        self.group = ''
        self.name = ''

    def get_person_data(self):
        self.name = input("Type name: ")
        self.group = input("Type group: ")

    def add_person(self):
        dict_of_elements[self.name] = self
        if self.group not in dict_of_elements:
            dict_of_elements[self.group] = Group()  # this will be the first element in our dict: its key is
            # this student's group name and its value is an object of a class Group.
        dict_of_elements[self.group].add_student(self)

    def print_info(self):
        group = dict_of_elements[self.group]
        for subject, teacher in group.subjects.items():
            print(subject, teacher.name)  # teacher is an object


class Tutor:  # tutor: groups are given by the user, students will be found in group's attributes
    def __init__(self):
        self.name = ''
        self.groups = []

    def get_person_data(self):
        self.name = input("Type name: ")
        local_group = input("Type group: ")
        while local_group:  # we keep asking for next group until the user types enter
            self.groups.append(local_group)
            if local_group not in dict_of_elements:
                dict_of_elements[local_group] = Group()
            dict_of_elements[local_group].tutor = self.name  # we assign this tutor to this group
            local_group = input("Type next group: ")

    def add_person(self):
        dict_of_elements[self.name] = self


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
            if local_group not in dict_of_elements:
                dict_of_elements[local_group] = Group()
            dict_of_elements[local_group].subjects[self.subject] = self
            local_group = input("Type next group: ")

    def add_person(self):
        dict_of_elements[self.name] = self

# first step - we enter the data


while True:
    role = input("Type a role: ")
    if role not in ALLOWED_COMMANDS:
        print(f"allowed commands are: {ALLOWED_COMMANDS}")
        continue
    if role == "stop":
        break
    elif role == "student":
        person_object = Student()
    elif role == "tutor":
        person_object = Tutor()
    elif role == "teacher":
        person_object = Teacher()
    person_object.get_person_data()
    person_object.add_person()
    # print(f'Students: {dict_of_students}')
    # print(f'Teachers: {dict_of_teachers}')
    # print(f'Tutors: {dict_of_tutors}')
    # print(f'Groups: {dict_of_groups}')


# step two
print("Next action: type a name of a person (student, tutor or teacher) or a name of a class to get information.")
phrase = input("Type person or group name: ")
while phrase:
    dict_of_elements[phrase].print_info()
    phrase = input("Type person or group name: ")
