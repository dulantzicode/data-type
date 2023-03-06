import os
os.system('cls')


full_name = lambda first, last: f'{first} {last}'


def greeting(name):
  print(f'Hi there {name}')


greeting(full_name('Kristine', 'Hudgens'))

print(full_name('Kristine', 'Hudgens'))




#  In the code below, create a variable called "greeting" and assign it a lambda function
#  that accepts a name as an argument, and return the string "Hi, name".
#  Example: If you pass in the name "Jordan", it should return "Hi, Jordan".

def lambda_practice():
    
    greeting = lambda name: f'Hi, {name}' #respuesta al ejercicio
    
    return greeting






# name = lambda full_name: f'Hi, {full_name}'

def lambda_practice(name):
    
    greeting = lambda name: f'Hi, {name}' #respuesta al ejercicio

    print(greeting (name))
    
    return greeting


lambda_practice('david')