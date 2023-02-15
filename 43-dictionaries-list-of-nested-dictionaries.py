import os
os.system('cls')

teams = [
  {
    'astros': {
      '2B': 'Altuve',
      'SS': 'Correa',
      '3B': 'Bregman',
    }
  },
  {
    'angels': {
      'OF': 'Trout',
      'DH': 'Pujols',
    }
  }
]

# print(teams[0])

angels = teams[1].get('angels', 'Team not found')
# get() consigue los valores, no la clave.

print(list(angels.values()))