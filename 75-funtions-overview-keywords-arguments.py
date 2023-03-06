import os
os.system('cls')

# para utilizar este tipo de argumentos (nombre y valor) se añade un segundo
# * (**) al inicio de la variable y se le antepone, por convención, el prefijo 'kw'.
# Mientras que añadir u asterisco nos creaba una tupla, añadir dos crea un diccionario.
def greeting(**kwargs):  
  print(kwargs)


greeting()
greeting(first = 'Kristine', last = 'Hudgens')

def greeting(**kwargs):
  if kwargs:
    print(f"Hi {kwargs['first']} {kwargs['last']}, have a great day!")
  else:
    print('Hi Guest!')


greeting()
greeting(first = 'Kristine', last = 'Hudgens')