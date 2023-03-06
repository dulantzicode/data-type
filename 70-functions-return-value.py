import os
os.system('cls')

def full_name(first, last):
  return f'{first} {last}'


kristine = full_name('Kristine', 'Hudgens')

# print(kristine)

def greeting(name):
  print(f'Hi {name}!')


greeting(kristine)


# Ejercicio

def sum_two_numbers(num_one, num_two):
  return (num_one + num_two)

print (sum_two_numbers(10,15))