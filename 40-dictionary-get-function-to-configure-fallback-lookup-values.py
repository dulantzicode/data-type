import os
os.system('cls')

teams = {
  "astros": ["Altuve", "Correa", "Bregman"],
  "angels": ["Trout", "Pujols"],
  "yankees": ["Judge", "Stanton"],
  "red sox": ['Price', 'Betts'],
}

featured_team = teams.get('yankees', 'No featured team')
# el segundo valor será el asignado en caso de que la clave
# buscada no exista en el diccionario.

print(featured_team)