import os
os.system('cls')


def greeting(name = 'Guest'):
  print(f'Hi {name}!')

greeting()
greeting('Kristine')

# Nope
def some_function(collection = []): # ¡OJO! no se debe usar una lista como argumento por defecto.
  collection.append(1)              # al ser un elemento mutable se almacena en memoria y permanece activo
  print(id(collection))             # para siguientes llamadas
  return collection
 
  
print(some_function())
print(some_function())
print(some_function())


# ejercicio
def counter(initial_count = 0):
  initial_count += 1
  return initial_count

print (counter(5))
print (counter())