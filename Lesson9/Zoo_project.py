from datetime import date

Food={} # create dictionary with faforite food for each class_type
Food['mammal']='meat'
Food['bird']='corn'
Food['fish']='worms'
Food['reptile']='grass'

# print(Food)

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

class Mammal(Animal):
    def __init__(self, name, age):
        super().__init__(name, age, 'mammal')
           
    def display(self):
        print(self.name, self.age, self.class_type)
        self.display_favorite_food()
        print('')

class Bird(Animal):
    def __init__(self, name, age):
        super().__init__(name, age, 'bird')
           
    def display(self):
        print(self.name, self.age, self.class_type)
        self.display_favorite_food()
        print('')

class Fish(Animal):
    def __init__(self, name, age):
        super().__init__(name, age, 'fish')
           
    def display(self):
        print(self.name, self.age, self.class_type)
        self.display_favorite_food()
        print('')

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


class Zoo:  # Add all animals to a dictionary with 4 keys as class_type
    total_animals=0

    animals={
        'mammal': [], 
        'bird':[],
        'fish':[],
        'reptile':[]
    }

    def add_animal(self, animal):
        if animal.class_type=='mammal':
            self.animals['mammal'].append(animal)
        elif animal.class_type=='bird':
            self.animals['bird'].append(animal)
        elif animal.class_type=='fish':
            self.animals['fish'].append(animal)
        elif animal.class_type=='reptile':
            self.animals['reptile'].append(animal)
        self.total_animals+=1
    
        
    def display(self, class_type):
        print(class_type, ': ', len(self.animals[class_type]))
        for animal in self.animals[class_type]:
            animal.display()


zoo = Zoo()
zoo.add_animal(Mammal('cow', 10))
zoo.add_animal(Animal('cow', 10, 'mammal'))
zoo.add_animal(Animal('tiger', 10, 'mammal'))
zoo.add_animal(Reptile('snake', 30, 'green', 40))
zoo.add_animal(Animal('Chicken', 1, 'bird'))


print('Total animals:', zoo.total_animals, '\n')
zoo.display('mammal')
zoo.display('bird')
zoo.display('reptile')
zoo.display('fish')
