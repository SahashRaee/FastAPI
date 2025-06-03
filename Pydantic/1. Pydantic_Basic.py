from pydantic import BaseModel                  

class Student(BaseModel):
    name: str 
    age: int

def insert_student_data(student: Student):
    print(student.age)
    print(student.name)
    print("Data added")

student_info = {'name': 'Sahash', 'age': 19}
student1 = Student(**student_info)

insert_student_data(student1)