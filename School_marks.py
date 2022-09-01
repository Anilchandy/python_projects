"""A python scrip where you can enter the rollnumber,name and marks for students in class and script will provide the 
student name with highest mark"""


class_strength = int(input("Enter the number of students in class :"))
i = 1
studentList_dict = {}
studentMark_dict = {}
while i <=class_strength:
    roll = int(input("Enter the roll number of student :"))
    name = str(input("Enter the name of student :"))
    Marks = int(input("Enter the marks :"))
    studentList_dict.update({roll:name})
    studentMark_dict.update({roll:Marks})
    i+=1
student_roll_list = list(studentList_dict.keys())
student_name_list = list(studentList_dict.values())
student_mark_list = list(studentMark_dict.values())
max_marks = max(student_mark_list)
max_marks_student = student_name_list[student_mark_list.index(max_marks)]
print(f"The student with max mark is {max_marks_student} and {max_marks_student} got {max_marks} marks ")
