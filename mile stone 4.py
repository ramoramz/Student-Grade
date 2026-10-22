Class under_graduate(student):
def __init__(self, name, student_id, grade, major)
super().__init__(self, name, student_id):
        self.name= name
        self.student_id= student_id
        self.grade= grade
        self.major= major

def display_info(self):
print("Student Name:", self.name)

print("Student ID:", self.student_id)

print("Grades:", self.grade)

print("major:", self.major)

Class graduate(student):
def __init__(self, name, student_id, grade, program_title)
super().__init__(self, name, student_id):
        self.name= name
        self.student_id= student_id
        self.grade= grade
        self.major= program_title

def display_info(self):
print("Student Name:", self.name)

print("Student ID:", self.student_id)

print("Grades:", self.grade)

print("program_title:", self.program_title)