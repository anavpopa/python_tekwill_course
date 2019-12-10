class Car:
    age=10
    color='red'
    engine='N/A'

    count_e=0
    count_d=0

    @classmethod
    def count_total(cls):
        print(cls.count_d + cls.count_e)

    def get_engine_type(self):
        print(self.engine)

class DieselCar(Car):
    engine='Diesel'
    def __init__(self):
        Car.count_d+=1

class ElectricCar(Car):
    engine='li-on bateries'
    def __init__(self):
        Car.count_e+=1


for i in range(4):
    d=DieselCar()
for i in range(3):
    e=ElectricCar()

Car.count_total()