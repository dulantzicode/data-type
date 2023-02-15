import os
os.system('cls')

teams = {
  "astros" : ["Altuve", "Correa", "Bregman"],
  "angels":  ["Trout", "Pujols"],
  "yankees": ["Judge", "Stanton"],
  "red sox": ["Price", "Betts"],
}

del teams['angels']
# esta forma funciona cuando sabes seguro que 
# el item existe en el diccionario.


removed_team = teams.pop('mets', 'Team not found')
# esta forma es preferible cuando NO sabes seguro que 
# el item existe en el diccionario.
# El valor almacenado corresponde al valor, sin la key.



print(teams)
print(removed_team)