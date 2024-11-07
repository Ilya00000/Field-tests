class Person:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
class Student(Person):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = []
        self.courses_in_progress = []
        self.finished_courses = []
    def add_grade(self, grade, course):
        self.grades.append((grade, course))
    def get_average_grade(self):
        return sum(grade for grade, _ in self.grades) / len(self.grades) if self.grades else 0
    def __str__(self):
        return (f"Имя: {self.name}\n"
                f"Фамилия: {self.surname}\n"
                f"Средняя оценка: {self.get_average_grade():.1f}\n"
                f"Курсы в процессе изучения: {', '.join(self.courses_in_progress)}\n"
                f"Завершенные курсы: {', '.join(self.finished_courses)}")
class Reviewer(Person):
    def __str__(self):
        return f"Имя: {self.name}\nФамилия: {self.surname}"
class Lecturer(Person):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = []
    def add_grade(self, grade, course):
        self.grades.append((grade, course))
    def get_average_grade(self):
        return sum(grade for grade, _ in self.grades) / len(self.grades) if self.grades else 0
    def __str__(self):
        return (f"Имя: {self.name}\n"
                f"Фамилия: {self.surname}\n"
                f"Средняя оценка: {self.get_average_grade():.1f}")
    def __lt__(self, other):
        return self.get_average_grade() < other.get_average_grade()
def average_student_grade(students, course):
    total_grades = []
    for student in students:
        for grade, c in student.grades:
            if c == course:
                total_grades.append(grade)
    return sum(total_grades) / len(total_grades) if total_grades else 0
def average_lecturer_grade(lecturers, course):
    total_grades = []
    for lecturer in lecturers:
        for grade, c in lecturer.grades:
            if c == course:
                total_grades.append(grade)
    return sum(total_grades) / len(total_grades) if total_grades else 0

student1 = Student("Иван", "Иванов")
student1.courses_in_progress = ["Python", "Git"]
student1.finished_courses = ["Введение в программирование"]
student1.add_grade(8, "Python")
student1.add_grade(9, "Python")
student2 = Student("Анна", "Петрова")
student2.courses_in_progress = ["Python", "Git"]
student2.finished_courses = ["Введение в программирование"]
student2.add_grade(10, "Python")
student2.add_grade(7, "Git")
reviewer1 = Reviewer("Алексей", "Алексеев")
reviewer2 = Reviewer("Мария", "Сидорова")
lecturer1 = Lecturer("Петр", "Петров")
lecturer1.add_grade(9, "Python")
lecturer1.add_grade(8, "Git")
lecturer2 = Lecturer("Сергей", "Сергеев")
lecturer2.add_grade(10, "Python")
lecturer2.add_grade(6, "Git")

print(student1)
print(student2)
print(lecturer1)
print(lecturer2)

course_name = "Python"
average_grade_students = average_student_grade([student1, student2], course_name)
print(f"Средняя оценка студентов по курсу {course_name}: {average_grade_students:.1f}")

average_grade_lecturers = average_lecturer_grade([lecturer1, lecturer2], course_name)
print(f"Средняя оценка лекторов по курсу {course_name}: {average_grade_lecturers:.1f}")
