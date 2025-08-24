class ClassRoom:
    def __init__(self, grade=0, homeRoomTeacher="", studentList=None):
        self.__grade = grade
        self.__homeRoomTeacher = homeRoomTeacher
        self.__studentList = studentList if studentList is not None else []
        self.__numStudents = len(self.__studentList)

    def get_grade(self):
        return self.__grade

    def get_homeroom_teacher(self):
        return self.__homeRoomTeacher

    def get_student_list(self):
        return self.__studentList

    def get_num_student(self):
        return self.__numStudents

    def set_grade(self, grade):
        self.__grade = grade

    def set_homeroom_teacher(self, teacher):
        self.__homeRoomTeacher = teacher

    def set_student_list(self, studentList):
        if len(studentList) <= 10:
            self.__studentList = studentList
            self.__numStudents = len(studentList)

    def set_num_student(self, num):
        if 0 <= num <= 10:
            self.__numStudents = num

    # Methods
    def get_student_no(self, n) -> str:
        # n is 1-based
        if 1 <= n <= self.__numStudents:
            return self.__studentList[n - 1]
        return ""

    def add_student(self, student_name) -> bool:
        if self.__numStudents < 10:
            self.__studentList.append(student_name)
            self.__numStudents += 1
            return True
        return False

    def change_student(self, n, new_name) -> bool:
        if 1 <= n <= self.__numStudents:
            self.__studentList[n - 1] = new_name
            return True
        return False

    def remove_student(self, student_name) -> bool:
        if student_name in self.__studentList:
            self.__studentList.remove(student_name)
            self.__numStudents -= 1
            return True
        return False

    def remove_student_no(self, n) -> bool:
        if 1 <= n <= self.__numStudents:
            self.__studentList.pop(n - 1)
            self.__numStudents -= 1
            return True
        return False

    def __str__(self) -> str:
        students = ", ".join(self.__studentList)
        return f"Grade: {self.__grade}\nHomeroom Teacher: {self.__homeRoomTeacher}\nStudents: {students}"
