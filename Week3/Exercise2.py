from abc import ABC, abstractmethod


class Person(ABC):
    def __init__(self, name, yob):
        self._name = name
        self._yob = yob

    def get_yob(self):
        return self._yob

    @abstractmethod
    def describe(self):
        pass


class Student(Person):
    def __init__(self, name, yob, grade):
        super().__init__(name=name, yob=yob)
        self.__grade = grade

    def describe(self):
        print(f"Student: {self._name}, YoB: {
              self._yob}, Grade: {self.__grade}")


class Doctor(Person):
    def __init__(self, name, yob, specialist):
        super().__init__(name=name, yob=yob)
        self.__specialist = specialist

    def describe(self):
        print(f"Doctor: {self._name}, YoB: {
              self._yob}, Specialist: {self.__specialist}")


class Teacher(Person):
    def __init__(self, name, yob, subject):
        super().__init__(name=name, yob=yob)
        self.__subject = subject

    def describe(self):
        print(f"Teacher: {self._name}, YoB: {
              self._yob}, Subject: {self.__subject}")


class Ward:
    def __init__(self, name):
        self.__name = name
        self.__list_people = []

    def add_person(self, person: Person):
        self.__list_people.append(person)

    def describe(self):
        print(f"Name: {self.__name}")
        for person in self.__list_people:
            person.describe()

    def count_doctor(self):
        count = 0
        for person in self.__list_people:
            if isinstance(person, Doctor):
                count += 1
        print(f"Count Doctor: {count}")

    def sort_yob(self):
        self.__list_people.sort(key=lambda x: x.get_yob(), reverse=True)
        self.describe()

    def compute_average(self):
        count = 0
        total_year = 0
        for p in self.__list_people:
            if isinstance(p, Teacher):
                count += 1
                total_year += p.get_yob()
        print(f"Teacger average age: {total_year/count}")


ward1 = Ward("Ward1")

ward1.add_person(Student("Student1", 2000, "A"))
ward1.add_person(Student("Student2", 2001, "B"))
ward1.add_person(Doctor("Doctor1", 1990, "Cardiologist"))
ward1.add_person(Teacher("Teacher1", 1980, "Math"))
ward1.add_person(Doctor("Doctor2", 1995, "Dentist"))
ward1.add_person(Teacher("Teacher2", 1975, "English"))

ward1.describe()

ward1.count_doctor()

ward1.sort_yob()

ward1.compute_average()
