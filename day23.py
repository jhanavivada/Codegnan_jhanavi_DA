class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
class Student(Person):
    def __init__(self,name,age,student_id,fee):
        Person.__init__(self,name,age)
        self.student_id=student_id
        self.fee=fee
        self.courses=[]
    def add_course(self,course):
        self.courses.append(course)
class Professor(Person):
    def __init__(self,name,age,emp_id):
        Person.__init__(self,name,age)
        self.emp_id=emp_id
        self.courses=[]
    def add_course(self,course):
        self.courses.append(course)
class NonTeachingStaff(Person):
    def __init__(self,name,age,staff_id):
        Person.__init__(self,name,age)
        self.staff_id=staff_id
class ITStaff(NonTeachingStaff):
    def __init__(self,name,age,staff_id,department,role):
        NonTeachingStaff.__init__(self,name,age,staff_id)
        self.department=department
        self.role=role
class Vehicle:
    def __init__(self,bus,car,van,auto):
        self.bus=bus
        self.car=car
        self.van=van
        self.auto=auto
class Driver(NonTeachingStaff):
    def __init__(self,name,age,staff_id,vehicle_type):
        NonTeachingStaff.__init__(self,name,age,staff_id)
        self.vehicle_type=vehicle_type
class Course:
    def __init__(self,name):
        self.name=name
        self.students=[]
        self.professor=None
    def add_student(self,student):
        self.students.append(student)
    def set_professor(self,professor):
        self.professor=professor
s1=Student("Janu",22,1119,50000)
s2=Student("Satya",21,1129,45000)
s3=Student("Honey",25,1103,48000)
p1=Professor("Bhanu",60,1911)
p2=Professor("Teja",65,1903)
it1=ITStaff("Lucky",35,2001,"IT Department","System Admin")
it2=ITStaff("Kiran",30,2002,"IT Department","Network Engineer")
vehicles=Vehicle(5,10,3,4)
d1=Driver("Pranay",45,3001,"Bus")
d2=Driver("Vamsi",40,3002,"Car")
python_course=Course("Python")
java_course=Course("Java")
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
print("Student Details:-")
for s in [s1,s2,s3]:
    print("\nName:",s.name)
    print("Age:",s.age)
    print("Student ID:",s.student_id)
    print("Fee:",s.fee)
    print("Courses:",s.courses)
print("\nProfessor Details:-")
for p in [p1,p2]:
    print("\nName:",p.name)
    print("Age:",p.age)
    print("Employee ID:",p.emp_id)
    print("Courses Teaching:",p.courses)
print("\nNon-Teaching Staff Details:-")
for staff in [it1,it2,d1,d2]:
    print("\nName:",staff.name)
    print("Age:",staff.age)
    print("Staff ID:",staff.staff_id)
print("\nIT Staff Details:-")
for it in [it1,it2]:
    print("\nName:",it.name)
    print("Age:",it.age)
    print("Staff ID:",it.staff_id)
    print("Department:",it.department)
    print("Role:",it.role)
print("\nVehicle Details:-")
print("Buses:",vehicles.bus)
print("Cars:",vehicles.car)
print("Vans:",vehicles.van)
print("Autos:",vehicles.auto)
print("\nDriver Details:-")
for d in [d1,d2]:
    print("\nName:",d.name)
    print("Age:",d.age)
    print("Staff ID:",d.staff_id)
    print("Vehicle Type:",d.vehicle_type)
print("\nCourse Details:-")
for c in [python_course,java_course]:
    print("\nCourse Name:",c.name)
    print("Professor:",c.professor.name)
    print("Students:")
    for stu in c.students:
        print(stu.name)
        
        
        
        
         
