from person import Person

class Employee(Person):
    def __init__(self, name,gender,dept):
        super().__init__(name,gender)
        self._dept = dept

    def __str__(self):
        return super().__str__() + " Dept: " + self._dept