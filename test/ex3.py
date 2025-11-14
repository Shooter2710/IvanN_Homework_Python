from student import Student
from courseGroup import CourseGroup

student = Student("Василий", "Петров", 30, "Инженер")
classmate1 = Student("Егор", "Зайцев", 28, "Инженер")
classmate2 = Student("Ольга", "Воронина", 27, "Инженер")
classmate3 = Student("Анна", "Иванова", 31, "Инженер")

course_group = CourseGroup(student, [classmate1, classmate2, classmate3])

print(course_group)