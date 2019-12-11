from datetime import date
from Animal import Animal
from Reptile import Reptile
from Mammal import Mammal
from Bird import Bird
from Fish import Fish
from Zoo import Zoo

# print(Food)

zoo = Zoo()
zoo.add_animal(Mammal('cow', 10))
zoo.add_animal(Animal('cow', 10, 'mammal'))
zoo.add_animal(Animal('tiger', 10, 'mammal'))
zoo.add_animal(Reptile('snake', 30, 'green',40))
zoo.add_animal(Animal('lizard', 2, 'reptile'))
zoo.add_animal(Bird('Chicken', 1))


print('Total animals:', zoo.total_animals, '\n')
zoo.display('mammal')
zoo.display('bird')
zoo.display('reptile')
zoo.display('fish')
