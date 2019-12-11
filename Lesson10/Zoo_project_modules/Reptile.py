from Animal import Animal

class Reptile(Animal):
    def __init__(self, name, age, color, tail):
        super().__init__(name, age, 'reptile')
        self.color=color
        self.tail=tail

    def change_color(self, new_color):
        self.color=new_color
    
    def change_tail(self, new_tail):
        self.tail=new_tail
    
    def display(self):
        print(self.name, self.age, self.class_type, self.color, self.tail)
        self.display_favorite_food()
        print('')