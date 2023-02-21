import os
os.system('cls')

positions = ['2b', '3b', 'ss', 'dh']
players = ['Altuve', 'Bregman', 'Correa', 'Gattis']

scoreboard = zip(positions, players)
# la función zip() crea un objeto zip que hay que convertir para poder usar.

print(list(scoreboard))
print(scoreboard)

scoreboard = list(zip(positions, players))

print(scoreboard)
print(tuple(scoreboard))
