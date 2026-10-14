class Student:
    def __init__(self, name, ID, grade):
        self.name = name
        self.ID = ID
        self.grade = grade

    def display_info(self):
        print(f"Name: {self.name}, ID: {self.ID}, Grade: {self.grade}")

student1 = Student("Omar", "2501238", 90)
student1.display_info()