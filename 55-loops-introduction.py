import os
os.system('cls')


players = ['Altuve', 'Bregman', 'Correa', 'Gattis']
players = ('Altuve', 'Bregman', 'Correa', 'Gattis')

for player in players:
  print(player)

players = {
  '2b': 'Altuve',
  '3b': 'Bregman',
  'ss': 'Correa',
  'dh': 'Gattis'
}

for position, player in players.items():
  print('Position', position)
  print('Player', player)


# ejercicio
def loop_over_list():
    my_list = ['uno', 'dos', 'tres', 'cuatro', 'cinco']
    for item in my_list:
        print(item)
    return my_list

loop_over_list()