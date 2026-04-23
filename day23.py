class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
class Student(Person):
    def __init__(self, name, age, student_id, fee):
        Person.__init__(self, name, age)
        self.student_id = student_id
        self.fee = fee
        self.courses = []
    def add_course(self, course):
        self.courses.append(course)
class Professor(Person):
    def __init__(self, name, age, emp_id):
        Person.__init__(self, name, age)
        self.emp_id = emp_id
        self.courses = []
    def add_course(self, course):
        self.courses.append(course)
class Course:
    def __init__(self, name):
        self.name = name
        self.students = []
        self.professor = None
    def add_student(self, student):
        self.students.append(student)
    def set_professor(self, professor):
        self.professor = professor
s1 = Student("Janu", 22, 1119, 50000)
s2 = Student("Satya", 21, 1129, 45000)
s3 = Student("Honey", 25, 1103, 48000)
p1 = Professor("Bhanu", 60, 1911)
p2 = Professor("Teja", 65, 1903)
python_course = Course("Python")
java_course = Course("Java")
python_course.set_professor(p1)
java_course.set_professor(p2)
p1.add_course("Python")
p2.add_course("Java")
python_course.add_student(s1)
python_course.add_student(s2)
java_course.add_student(s2)
java_course.add_student(s3)
s1.add_course("Python")
s2.add_course("Python")
s2.add_course("Java")
s3.add_course("Java")

print("Student Detalis:-")
students = [s1, s2, s3]
for s in students:
    print("\nName:", s.name)
    print("Age:", s.age)
    print("Student ID:", s.student_id)
    print("Fee:", s.fee)
    print("Courses:", s.courses)
    
print("\nProfessor Detalis:-")
profs = [p1, p2]
for p in profs:
    print("\nName:", p.name)
    print("Age:", p.age)
    print("Employee ID:", p.emp_id)
    print("Courses Teaching:", p.courses)
    
print("\nCourse Detalis:-")
courses = [python_course, java_course]
for c in courses:
    print("\nCourse Name:", c.name)
    print("Professor:", c.professor.name)
    print("Students:")
    for stu in c.students:
        print(stu.name)


        
        
        
        
         
