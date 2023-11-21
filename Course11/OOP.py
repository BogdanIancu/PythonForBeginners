class University:
    def __init__(self):
        self.__name = "Harvard"

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, new_name):
        self.__name = new_name

    def __add__(self, other):
        return self.name + " " + other.name

    def my_function(self):
        print("University: ", self.name)


class IvyLeagueUniversity(University):

    def __init__(self):
        super().__init__()
        self.rank = 5

    def my_function(self):
        print("Ivy League University: ", self.name)


class Student:
    faculty = "Computer Science"

    def __init__(self, name="Unknown", age=18, grade=0.0):
        self.name = name
        self._age = age
        self.__grade = grade

    def __del__(self):
        print("Here should be some code that "
              "is executed before this object is deleted")

    def get_grade(self):
        return self.__grade

    def set_grade(self, new_grade):
        if isinstance(new_grade, float) and 0 <= new_grade <= 10:
            self.__grade = new_grade

    grade = property(get_grade, set_grade)

    @staticmethod
    def static_method():
        print("This is a static method")

    @classmethod
    def class_method(cls):
        print("Static method called for faculty: " + cls.faculty)

    def __str__(self):
        return f"name={self.name}, age={self._age}, grade={self.__grade}"

    def has_legal_age_to_drive(self, legal_age):
        return self._age >= legal_age

    def __my_method(self):
        print("My method")


myStudent = Student()
print(myStudent)
# print(myStudent._age)
myStudent.height = 1.88
# print(myStudent.__grade)
print(myStudent.__dict__)
print(myStudent.height)

myOtherStudent = Student()
myOtherStudent.name = "John"
myOtherStudent._age = 25
print(myOtherStudent)
print(myOtherStudent.faculty)
Student.faculty = "Biology"
print(myStudent.faculty)
print(myOtherStudent.faculty)
print(myOtherStudent.has_legal_age_to_drive(18))

aStudent = Student("Maria", 27, 9.9)
print(aStudent)
Student.static_method()
Student.class_method()
print(aStudent.get_grade())
aStudent.grade = 8.5
print(aStudent.grade)

univ1 = University()
univ1.name = "MIT"
print(univ1.name)

univ2 = University()
print(univ1 + univ2)

ivyLeagueUni1 = IvyLeagueUniversity()
print(ivyLeagueUni1.name)
print(issubclass(IvyLeagueUniversity, University))

justAnUniversity = ivyLeagueUni1
justAnUniversity.my_function()

