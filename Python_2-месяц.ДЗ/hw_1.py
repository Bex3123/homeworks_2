class Person:
    def __init__(self, fullname, age, is_married):
        self.fullname = fullname
        self.age = age
        self.is_married = is_married

    def introduce_myself(self):
        print(f"Меня зовут {self.fullname}, мне {self.age} лет, я женат/замужем {self.is_married}")


class Student(Person):
    def __init__(self, fullname, age, is_married, marks):
        super().__init__(fullname, age, is_married)
        self.marks = marks

    def average_mark(self):
        return round(sum(self.marks.values()) / len(self.marks), 2)


class Teacher(Person):
    base_salary = 10000

    def __init__(self, fullname, age, is_married, experience):
        super().__init__(fullname, age, is_married)
        self.experience = experience

    def salary(self):
        bonus = 0
        if self.experience > 3:
            bonus = 0.05 * (self.experience - 3) * self.base_salary
        return self.base_salary + bonus


teacher = Teacher("Любовь Павловна", 50, True, 20)

teacher.introduce_myself()
print("Зарплата учителя:", teacher.salary())


def create_students():
    students = []
    students.append(Student("Нурлан Насип", 20, False, {"Алгебра": 5, "Химия": 4, "Python": 5}))
    students.append(Student("Эрлан Андашев", 21, False, {"Алгебра": 5, "Химия": 5, "Python": 5}))
    students.append(Student("Мирбек Атабеков", 20, True, {"Алгебра": 3, "Химия": 3, "Pytnon": 4}))
    return students


students = create_students()
for student in students:
    student.introduce_myself()
    print("Средняя оценка ученика:", student.average_mark())
