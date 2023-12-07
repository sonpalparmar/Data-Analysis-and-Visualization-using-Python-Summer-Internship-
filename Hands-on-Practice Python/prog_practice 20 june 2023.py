class Course:
    def __init__(self,coursename):
        self.__coursename=coursename
        self.__students=[]
    def add_student(self,student):
        self.__students.append(student)
    def get_student(self):
        return self.__students
    def get_no_students(self):
        return len(self.__students)
    def get_course_name(self):
        return self.__coursename
    def drop_student(self,student):
        if(student in self.__students):
            self.__students.remove(student)
        else:
            print("student does not exist")
course1=Course("python")
course2=Course("Computer Networks")
course1.add_student("Riya")
course1.add_student("Abhi")
course1.add_student("Harsirat")
course2.add_student("Riya")
course2.add_student("Kabir")
print("Number of student in course1")
print(course1.get_no_students())
print("Number of student in course2")
print(course2.get_no_students())
students=course1.get_student()
print("students in course 1")
for i in range(len(students)):
    print(students[i])
print("students in course 2")
students=course2.get_student()
for i in range(len(students)):
    print(students[i])
student_delete=input("enter whom to delete")
course1.drop_student(student_delete)
new_list=course1.get_student()
print("updated list of students in course 1")
for i in range(len(new_list)):
    print(new_list[i])


