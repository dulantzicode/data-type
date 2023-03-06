import os
os.system('cls')


def full_name(first, last):
  print(f'{first} {last}')


# Por convención se dejan dos líneas en blanco después de una función.

full_name('Kristine', 'Hudgens')


def auth(email, password):
  if email == 'kristine@hudgens.com' and password == 'secret':
    print('You are authorized')
  else:
    print('You are not authorized')


auth('kristine@hudgens.com', 'asdf')

def hundred():
  for num in range(1, 21):
    print(num)


hundred()

def counter(max_value):
  for num in range(1, max_value):
    print(num)


counter(11)

#ejercicio
def greeting():
    print ('hello')

greeting()