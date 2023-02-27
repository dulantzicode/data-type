import os
os.system('cls')


players = {
  "ss" : "Correa",
  "2b" : "Altuve",
  "3b" : "Bregman",
  "DH" : "Gattis",
  "OF" : "Springer",
}

"""
Los diccionarios se acceden a través de vistas.
Un diccionario puede ser accedido por diferentes usuarios a la vez
Cada acceso es un hilo
Las vistas son dinámicas. Si alguien cambia un valor la vista se actualiza.
Por ello si queremos trabajar con los valores a los que accedimos
es conveniente realizar una 'copia' del diccionario.
Para ello usamos la clase list() que nos permite trabajar los
diccionarios como si fuesen listas.
"""

player_names = list(players.copy().values())
# la clase list permite trabajar la vista del diccionario
# como si fuese una lista y, en este caso, almacenarla como lista.
# El método .copy() genera una lista del diccionario
# el metodo values() selecciona solo los valores del diccionario
# sin la clave (key) 


print(player_names)

teams = {
  "astros" : ["Altuve", "Correa", "Bregman"],
  "angels":  ["Trout", "Pujols"],
  "yankees": ["Judge", "Stanton"],
  "red sox": ["Price", "Betts"],
}

team_groupings = teams.items() 
# el método items() crea una vista con todo el contenido del diccionario.

"""
[
  ('astros', ['Altuve', 'Correa', 'Bregman']),
  ('angels', ['Trout', 'Pujols']),
  ('yankees', ['Judge', 'Stanton']),
  ('red sox', ['Price', 'Betts'])
]
"""

print(list(team_groupings)[1][1][0])
# la clase list permite trabajar la vista del diccionario
# como si fuese una lista.
# el primer argumento es el índice de la fila,
# el segundo es el índice de la columna,
# y el tercero el índice del valor.
# si el elemento escogido es la key, entonces
# el último argumento indica el índice del caracter
# o rango de caracteres a seleccionar.