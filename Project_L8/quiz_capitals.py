# PROJECT: Write a program that will generate question for guessing countrie’s capital with 4 options of

# Create dictionary with countries and capitals
capitals =  {} 
with open('countries.txt', encoding='utf-8') as f:
    for line in f:
        key, value = line.split(',')
        capitals[key] = value[:-1]

import random

country, capital = random.choice(list(capitals.items()))
#print(country,capital)

capitals.pop(country) # Remove the selected country and capital in order to avoid duplicates in other random capitals selected for answers
random_capitals=random.sample(list(capitals.values()),3) # Select other three random capitals for answers
random_capitals.append(capital) # create the list of 4 answers and shuflle
#print(random_capitals)
random.shuffle(random_capitals)

# Create a dictionary with letters as keys and capitals as values for better visualisation of question answer choices
keys=['A','B','C','D']
answers=dict(zip(keys, random_capitals))
# print(answers)

# Print question and answer choices
print('What is the capital of '+country +'?')
for key, value in answers.items():
    print(key, ' ', value)

# Ask for answer
answer=input('Introduce your answer'+'\n')

# Check if answer is correct
if answers.get(answer)==capital:
    print('Correct:' + capital)
else:  
    print('Incorrect:' + 'The capital is '+ capital)   


