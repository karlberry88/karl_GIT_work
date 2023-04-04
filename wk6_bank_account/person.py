class Person:

    def __init__(self, name, gender):
        self._name = name
        self._gender = gender.upper()

    def __str__(self):
        return "Name: " + self._name + " Gender: " + self._gender