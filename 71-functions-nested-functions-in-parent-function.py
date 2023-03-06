import os
os.system('cls')


def greeting(first, last):
  def full_name():
    return f'{first} {last}'

  print(f'Hi {full_name()}!')


greeting('Kristine', 'Hudgens')


def greeting(first, last):
  def full_name():    # no hace falta volver a indicar 'first' y 'last' porque la función anidada 
                      # tiene acceso a los argumentos recibidos en la función principal.
    return f'{first} {last}'

  return f'¡Hola {full_name()}!'


nombre = greeting('David', 'Gómez')
print (nombre)


# ejercicio

def greeting(persons_name):
  return f"Hello, {persons_name}"

print (greeting("David"))