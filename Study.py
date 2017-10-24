class Person(object):
    def __init__(self, first_name, second_name, last_name, age):
        self.__first_name = first_name
        self.__second_name = second_name
        self.__last_name = last_name
        self.__age = age

    def set_first_name(self, first_name):
        self.__first_name = first_name

    def get_first_name(self):
        return self.__first_name

    def set_second_name(self, second_name):
        self.__second_name = second_name

    def get_second_name(self):
        return self.__second_name

    def set_last_name(self, last_name):
        self.__last_name = last_name

    def get_last_name(self):
        return self.__last_name

    def set_age(self, age):
        self.__age = age

    def get_age(self):
        return self.__age


class Teacher(Person):
    def __init__(self, first_name, second_name, last_name, age, specialty, qualification):
        self.__specialty = specialty
        self.__qualification = qualification
        super().__init__(first_name, second_name, last_name, age)

    def set_specialty(self, specialty):
        self.__specialty = specialty

    def get_specialty(self):
        return self.__specialty

    def set_qualification(self, qualification):
        self.__qualification = qualification

    def get_second_name(self):
        return self.__qualification


class Student(Person):
    def __init__(self, first_name, second_name, last_name, age, student_id, start_year):
        self.__student_id = student_id
        self.__start_year = start_year
        super().__init__(first_name, second_name, last_name, age)

    def set_student_id(self, student_id):
        self.__student_id = student_id

    def get_student_id(self):
        return self.__student_id

    def set_start_year(self, start_year):
        self.__start_year = start_year

    def get_start_year(self):
        return self.__start_year


class Group(object):
    def __init__(self, group_id, teacher, students):
        self.__group_id = group_id
        self.__teacher = teacher
        self.__students = students

    def set_group_id(self, group_id):
        self.__group_id = group_id

    def get_group_id(self):
        return self.__group_id

    def set_teacher(self, teacher):
        self.__teacher = teacher

    def get_teacher(self):
        return self.__teacher

    def set_students(self, students):
        self.__students = students

    def get_students(self):
        return self.__students

    def add_student(self, student):
        self.__students.append(student)

    def exclude_student(self, student):
        if student in self.__students:
            self.__students.remove(student)
            return True
        return False


class Course(object):
    def __init__(self, name_of_course, groups):
        self.__name = name_of_course
        self.__groups = groups

    def set_name(self, name_of_course):
        self.__name = name_of_course

    def get_name(self):
        return self.__name

    def set_groups(self, groups):
        self.__groups = groups

    def get_groups(self):
        return self.__groups

    def add_group(self, group):
        self.__groups.append(group)

    def exclude_group(self, group):
        if group in self.__groups:
            self.__groups.remove(group)
            return True
        return False


def main():
    teacher_mathematics = Teacher('Ololo', 'Ololoevich', 'Ololoev', 45, 'mathematics', 'phd')
    teacher_physics = Teacher('Ururu', 'Ururuevich', 'Ururuev', 55, 'physics', 'phd')

    student1 = Student('K', 'Kevich', 'Kev', 21, 1809, 2010)
    student2 = Student('J', 'Jevich', 'Jev', 22, 1810, 2010)
    student3 = Student('Z', 'Zevich', 'Zev', 21, 1909, 2010)
    student4 = Student('A', 'Aevich', 'Aev', 20, 1879, 2011)
    student5 = Student('S', 'Sevich', 'Sev', 23, 1249, 2011)

    group1 = Group(11, teacher_mathematics, [student1, student2, student3])
    group2 = Group(12, teacher_physics, [student4, student5])

    course_of_math = Course('math', [group1, ])
    course_of_phys = Course('phys', [group2, ])

    student6 = Student('R', 'Revich', 'Rev', 19, 1579, 2009)
    group2.add_student(student6)


main()
