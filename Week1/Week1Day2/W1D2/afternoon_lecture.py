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

car_1 = Car("Mercedes", "Black", "V8", 4)
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
        
    # static methods
    @staticmethod
    def validate(dict):
        test = True
        if len(dict["full_name"])<2:
            print("Full Name must contain at least 2 characters!")
            test = False
        if dict["age"]<18:
            print("You're too young")
            test = False
        return test
    
# Instances
student_4 = Student("Maria Doe", "d@d.d", 22, [7, 8], None)
student_2_dict = {
    "full_name": "Alice Smith",
    "email": "s@s.s",
    "age":25,
    "belt_grades": [9.5, 8.7, 8, 9.4,8],
    "status": "graduated"
}

student_2 = Student(student_2_dict["full_name"], student_2_dict["email"], student_2_dict["age"], student_2_dict["belt_grades"],car_1, student_2_dict["status"])


if Student.validate(student_2_dict):
    new_student = Student(student_2_dict["full_name"], student_2_dict["email"], student_2_dict["age"], student_2_dict["belt_grades"],car_1, student_2_dict["status"])
    new_student.display_info()
else:
    print("you can't create an instance with this dictionnary")