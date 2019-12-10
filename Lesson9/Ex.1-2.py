# Ex 1
class Car:
    def __init__(self, year, fuel, colour):
        self.year=year
        self.fuel=fuel
        self.colour=colour
    
    def age(self, year=2019):
        return year-self.year
    def type_fuel(self):
        print(self.fuel)
    def new_colour(self, new_colour='white'):
        self.colour=new_colour

    
a = Car(1999, 'diesel', 'black')
print(a.age())
a.type_fuel()
print(a.type_fuel())
a.new_colour()
print(a.colour)

# Ex 2

class Student:

    def __init__(self, avg_grade):
        self.avg_grade = avg_grade

    @classmethod
    def create_with_list(cls, grades_list):
        return cls(sum(grades_list) / len(grades_list))

    

s1 = Student(10)
s2 = Student.create_with_list([1,3,10, 8])
print(s1.avg_grade)
print(s2.avg_grade)