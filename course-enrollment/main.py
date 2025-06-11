class Course:
    def __init__(self, course_id, name, instructor):
        self.course_id = course_id
        self.name = name
        self.instructor = instructor
       
    def show_info(self):
        print( f'course ID: {self.course_id}, name: {self.name}, taught by: {self.instructor}')
    

class Student:
    def __init__(self, name):
        self.name = name
        self.enrolled_courses = []

    def enroll(self, course):
        if course not in self.enrolled_courses:
            self.enrolled_courses.append(course)
            print(f'{self.name} has enrolled in {course.name}.')
        else:
            print(f'{self.name} is already enrolled in {course.name}.')

    def view_enroll_courses(self):
        print(f'enrolled courses of **{self.name}**')
        if self.enrolled_courses:
            for course in self.enrolled_courses:
                course.show_info()
        else:
            print(f'{self.name} is not enrolled in any courses.')

course1 = Course(101, 'Python Programming', 'MR. Vikram')
course2 = Course(102, 'javascript Programming', 'MR. Ali Ahmed')
course3 = Course(103, 'C# Programming', 'MR. Waqas')

print('=== Student enrolled in the courses ===')

rahul = Student('Rahul')
wajahat = Student('Wajahat')
nouman = Student('Nouman')
samir = Student('Samir')
lana = Student('Lana')
ryan = Student('Ryan')
priya = Student('Priya')

samir.enroll(course1)
rahul.enroll(course2)
ryan.enroll(course3)

lana.enroll(course1)
lana.enroll(course3)
lana.enroll(course2)

print('=== View enrolled courses ===')

samir.view_enroll_courses()

lana.view_enroll_courses()


        
        