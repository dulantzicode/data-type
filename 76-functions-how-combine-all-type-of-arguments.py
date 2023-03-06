import os
os.system('cls')


def greeting(time_of_day, *args, **kwargs):
  print(f"Hi {' '.join(args)}, I hope that you're having a good {time_of_day}.")

  if kwargs:
    print('Your tasks for the day are:')
    for key, val in kwargs.items():
      print(f'{key} -> {val}')


greeting('Morning',
         'Kristine', 'Hudgens',
         first = 'Empty dishwasher',
         second = 'Take pupper out',
         third = 'math homework')
# cuando se trabaja con distintos tipos de datos como argumento
# se suelen poner cada uno de ellos en distintas líneas
# para facilitar la lectura del programa.  