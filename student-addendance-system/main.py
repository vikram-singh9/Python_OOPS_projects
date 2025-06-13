from abc import ABC, abstractmethod

class Person(ABC):
    def __init__(self, name):
        self._name = name  # Encapsulated

    @abstractmethod
    def get_info(self):
        pass
class Student(Person):
    def __init__(self, student_id, name):
        super().__init__(name)  # Inheriting from Person
        self.__student_id = student_id   # Encapsulated
        self.__attendance = []

    def mark_attendance(self, date):
        self.__attendance.append(date)

    def get_info(self):
        return f"{self._name} (ID: {self.__student_id})"

    def show_attendance(self):
        print(f"\n📘 Attendance for {self.get_info()}:")
        if not self.__attendance:
            print("❌ No attendance recorded.")
        else:
            for date in self.__attendance:
                print(f"✅ Present on: {date}")
class Teacher(Person):
    def __init__(self, name, subject):
        super().__init__(name)
        self.subject = subject

    def get_info(self):
        return f"👩‍🏫 Teacher: {self._name}, Subject: {self.subject}"
class AttendanceSystem:
    def __init__(self):
        self.students = {}

    def add_student(self, student: Student):
        self.students[student.get_info()] = student
        print(f"✅ {student.get_info()} added successfully!")

    def mark_attendance(self, student_info, date):
        if student_info in self.students:
            self.students[student_info].mark_attendance(date)
            print(f"✅ Attendance marked for {student_info} on {date}")
        else:
            print("❌ Student not found.")

    def view_attendance(self, student_info):
        if student_info in self.students:
            self.students[student_info].show_attendance()
        else:
            print("❌ Student not found.")

    @classmethod
    def welcome(cls):
        print("🎓 Welcome to the Student Attendance System")
AttendanceSystem.welcome()

system = AttendanceSystem()

# Add students
s1 = Student(101, "Vikram Singh")
s2 = Student(102, "Ayesha Noor")

system.add_student(s1)
system.add_student(s2)

# Use polymorphism
t1 = Teacher("Ahmed Sir", "Math")
print(t1.get_info())

# Mark attendance
system.mark_attendance(s1.get_info(), "2025-06-04")
system.mark_attendance(s2.get_info(), "2025-06-04")
system.mark_attendance(s1.get_info(), "2025-06-05")

# View attendance
system.view_attendance(s1.get_info())
system.view_attendance(s2.get_info())
