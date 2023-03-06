import os
os.system('cls')


def greeting(*args):
  print('Hi ' + ' - '.join(args)) 

# en el caso de trabajar con argumentos "unpacking" el nombre de
# la variable, por convención, es args.

# como en el caso de las listas (nº68) el * antes del nombre de la variable
# indica que esa variable acoge los valores de todos los argumentos suministrados,
# en este caso en forma de una tupla. 

# el método .join(arguments) une los diferentes argumentos en un string
# y los separa con el carácter o string colocado justo antes del punto
# ejemplos ' '.join(args), ' - '.join(args), etc. 


greeting('Kristine', 'M', 'Hudgens')
greeting('Tiffany', 'Hudgens')


def greeting(*names):
  print('Hi ' + ' '.join(names))




greeting('Kristine', 'M', 'Hudgens')
greeting('Tiffany', 'Hudgens')


def greeting(time_of_day, *args):
  print(f"Hi {' '.join(args)}, I hope that you're having a good {time_of_day}")


greeting('Afternoon', 'Kristine', 'M', 'Hudgens')
greeting('Morning', 'Tiffany', 'Hudgens')