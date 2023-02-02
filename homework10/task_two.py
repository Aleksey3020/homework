class ValidationError(Exception):
    pass


class Student:
    def __init__(self, surname, name, group_number, great):
        self.surname = surname
        self.name = name
        self.group_number = group_number
        self.great = great

    @property
    def surname(self):
        return self._surname

    @surname.setter
    def surname(self, value):
        if not isinstance(value, str):
            raise ValidationError

        self._surname = value

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not isinstance(value, str):
            raise ValidationError

        self._name = value


class School:
    def __init__(self, students):
        self.students = list()

    def add_student(self, student):
        self.students.append(student)

    def get_best_students(self):
        result = list()
        for student in self.students:
            count = 0
            for x in student.great:
                if x == 5 or x == 6:
                    count += 1
            if count == 5:
                result.append(student)
        return result

    def get_students(self, group_number):
        self.group_number = group_number
        for student in self.students:
            if self.group_number == student.group_number:
                self.students.append(student)

    def get_students_without_exams(self):
        for student in self.students:
            if sum(student.great) / 5 >= 7:
                self.students.append(student)


t1 = Student(1, 'Aleksey', '109', [5, 6, 8, 8, 7])
print(t1.surname)
print(t1.name)
