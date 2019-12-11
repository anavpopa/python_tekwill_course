from Food import Food

class Animal:
    def __init__(self, name, age, class_type):
        self.name=name
        self.age=age
        self.class_type=class_type

    @classmethod
    def from_birth_year(cls, name, birth_year, class_type):
        return cls(name, date.today().year-birth_year, class_type)
    
    def display(self):
        print(self.name, self.age, self.class_type)
        self.display_favorite_food() # why here?
        print('')

    def display_favorite_food(self):
        print(self.name, 'likes ', Food[self.class_type])