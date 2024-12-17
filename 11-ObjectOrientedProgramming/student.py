# class definition
class Student():
    def __init__(self):
        self.name = ""
        self.age = 0
        self.last_name = ""

def main():
    # object creation based on the class
    student1 = Student()
    student2 = Student()
    student3 = Student()
    student1.name = "Dominic"
    student1.age = 19
    student1.last_name = "Some"
    student2.name = "Olivia"
    student2.age = 21
    student2.last_name = "Some"
    student3.name = "Olivia"
    student3.age = 21
    student3.last_name = "Some"

    print('LIST OF STUDENTS')
    print('================')
    print(f'{student1.name}, {student1.age} years old')
    print(f'{student2.name}, {student2.age} years old')

if __name__ == "__main__":
    main()