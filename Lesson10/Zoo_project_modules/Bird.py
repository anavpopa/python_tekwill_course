from Animal import Animal

class Bird(Animal):
    def __init__(self, name, age):
        super().__init__(name, age, 'bird')
           
    def display(self):
        print(self.name, self.age, self.class_type)
        self.display_favorite_food()
        print('')