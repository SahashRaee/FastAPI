#@ DEPENDENCIES:                     
from pydantic import BaseModel                                                  # Importing BaseModel class from pydantic for data validation            
from typing import List, Dict, Optional , TypedDict ,                                        
#@ MODEL DEFINITON:
class Student(BaseModel):                                                       # Defining the student model inheriting from BaseModel
    name: str 
    age: int
    married: Optional[str] = None

def insert_student_data(student: Student):                                      # Function to insert and display student data
    print(student.age)
    print(student.name)
    print("Data added")

#@ DATA PREPARATION:
student_info = {'name': 'Sahash', 'age': 19}                                    # Dictionary holding student information

#@ MODEL INSTANTIATION
student1 = Student(**student_info)                                              # Creating an instance of Student class using unpacked dictionary

insert_student_data(student1)                                                   # Function calling