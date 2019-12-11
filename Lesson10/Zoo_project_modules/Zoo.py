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