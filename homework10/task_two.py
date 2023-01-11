class School:
    student_count = 0

    def __init__(self):
        self.students = []

    def add_student(self, *args):
        for student in args:
            self.students.append(student)
            School.student_count += 1

    def get_best_students(self):
        for student in self.students:
            c1, c2, c3, c4 = student.student_info
            for i in c4:
                if i == 5 or i == 6:
                    continue
                else:
                    return None
            print(c1, c2, c3)

    def get_students(self, group_number):
        for student in self.students:
            c1, c2, c3, c4 = student.student_info
            if c3 != group_number:
                continue
            else:
                print(c1, c2, c3)

    def get_students_without_exams(self):
        for student in self.students:
            c1, c2, c3, c4 = student.student_info
            count = 0
            count_max = 0
            for i in c4:
                count += 1
                count_max += i

            if count_max/count >= 7:
                print(c1, c2,)
            else:
                continue


class Student:

    def __init__(self, name, lastName, groupNumber, performance):
        self.name = name
        self.lastName = lastName
        self.groupNumber = groupNumber
        self.performance = performance

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not isinstance(value, str):
            raise ValidationError("Must be str")
        self._name = value

    @property
    def lastName(self):
        return self._lastName

    @lastName.setter
    def lastName(self, value):
        if not isinstance(value, str):
            raise ValidationError("Must be str")
        self._lastName = value

    @property
    def student_info(self):
        return self.name, self.lastName, self.groupNumber, self.performance


class ValidationError(Exception):
    pass


s1 = Student("Sergey", "Frolov", 147, [5, 5, 5, 5, 6])
s2 = Student("Andrey", "Petrov", 148, [5, 4, 4, 4, 6])
s3 = Student("Saveliy", "Ivanov", 149, [9, 9, 9, 9, 10])
s4 = Student("Pavel", "Chamorov", 149, [4, 4, 4, 4, 4])
s5 = Student("Lena", "Golovach", 149, [8, 8, 8, 7, 6])
school = School()
school.add_student(s1, s2, s3, s4, s5)
print(school.student_count)
school.get_best_students()
school.get_students(149)
school.get_students_without_exams()
