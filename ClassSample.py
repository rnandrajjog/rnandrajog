class Student:
    pass


class AnotherStudent:
    def printstudent(self, name, student_id):
        print(name)


class Calculator:
    def Add(self, n1, n2):
        print("number 1 is", n1)

        return n1 + n2


anotherStudent = AnotherStudent()
anotherStudent.printstudent("John", "as")

s = Student()

calculator = Calculator()
total = calculator.Add(2, 4)
print(total)
anotherTotal = calculator.Add(10, 20)
print(anotherTotal)
