student_1 = {
    "full_name": "Alex Brown",
    "email": "a@a.a",
    "age":20,
    "belt_grades": [9.8, 7, 8.1, 10],
    "status": "active"
}

student_2 = {
    "full_name": "Alice Smith",
    "email": "s@s.s",
    "age":25,
    "belt_grades": [9.5, 8.7, 8, 9.4,8],
    "status": "graduated"
}

# ?OOP : Object Oriented Programming
# ? Classes: template = factory to create objects 
# attributes : caracteristics of the object
# methods: actions of the object

# * Naming convention for classes: (PascalCase) First letter Capitalized, and singular
class Student:
    # class attributes
    school = "Coding Dojo"
    all_students = []
    # *Constructor
    def __init__(self, name, email, age, grades, car, status="active"):
        # instance attributes
        self.full_name = name
        self.email = email
        self.age = age
        self.belt_grades = grades
        self.status = status
        Student.all_students.append(self)
        self.car = car
        
    
    # Instance Methods
    def display_info(self):
        print(f"Full Name: {self.full_name}\n Grades: {self.belt_grades}\nstatus: {self.status}")
        return None
    
    def change_status(self, new_status):
        self.status = new_status
    
    # Class Methods
    @classmethod
    def change_school(cls, new_school_name):
        cls.school = new_school_name
    
# Instances
student_4 = Student("Maria Doe", "d@d.d", 22, [7, 8])
# print(student_3.full_name)
# student_3.display_info()
# student_3.change_status("active")
# print("*"*100)
# student_3.display_info()

# print(student_3.school)
# print(student_4.school)
# print(Student.school)
# print(Student.all_students)
# for one_student in Student.all_students:
#     print(one_student.full_name)
print(Student.school)
Student.change_school("Nefel Education")
print(Student.school)
class Car:
    def __init__(self, model, color, motor, nb_of_doors):
        self.model = model
        self.color = color
        self.motor = motor
        self.nb_of_doors = nb_of_doors
        self.speed = 0
    
    def accelaration(self,new_speed):
        self.speed += new_speed
        return self
    
    def display_speed(self):
        print(f"Speed: {self.speed}km/h")
        return self

# car_1 = Car("Mercedes", "Black", "V8", 4)
# car_1.accelaration(20).display_speed().accelaration(30).display_speed().accelaration(10).accelaration(40).display_speed()
# # car_1.display_speed()
# # car_1.accelaration(30)
# # car_1.display_speed()
student_3 = Student("Mark Jack", "m@m.m", 30, [10, 10, 9],Car("Mercedes", "Black", "V8", 4), "postponed")
    