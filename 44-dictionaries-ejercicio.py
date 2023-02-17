import os
os.system('cls')


ventas = {
    'Google': 15,
    'Facebook': 20,
    'Twitter': 8,
    'Offline': 10,
    'Otros': 25,
    }


longitud = (len(ventas))
ventas_groupings = ventas.items()

for i in range(longitud):
    print(list(ventas_groupings)[i][0] + ' ' +
         (list(ventas_groupings)[i][1])*'$')



