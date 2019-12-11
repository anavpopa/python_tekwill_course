from Animal import Animal

class Mammal(Animal):
    def __init__(self, name, age):
        super().__init__(name, age, 'mammal')
           
    def display(self):
        print(self.name, self.age, self.class_type)
        self.display_favorite_food()
        print('')