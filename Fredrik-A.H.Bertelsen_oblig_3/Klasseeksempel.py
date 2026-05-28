class Student:
    def __init__(self, first_name,last_name, age,student_id):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.student_id = student_id
        self.courses = []
    def get_full_name(self):
        return f"{self.first_name} {self.last_name}"
    def add_course(self, course):
        self.courses.append(course)

nils_nilsen = Student("Nils","Nilsen",22, 123456)
anne_annensen = Student("Anne","Annensen",23, 234567)

print(nils_nilsen.first_name)
print(anne_annensen.first_name)
print(f"{nils_nilsen.first_name} {nils_nilsen.last_name} er {nils_nilsen.age} år gammel og har studentnummeret {nils_nilsen.student_id}")
print(nils_nilsen.get_full_name())

class Course:
    def __init__(self, name, code, credits):
        self.name = name
        self.code = code
        self.credits = credits

