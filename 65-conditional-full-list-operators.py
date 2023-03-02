import os
os.system('cls')

# List of comparison operators
# == Equality
# != Inequality
# <> Inequality (deprecated)
# >  Greater than
# >= Greater than or equal to
# < Less than
# <= Less than or equal to

username = 'jonsnow'

if username == 'jonsnow':
  print('Welcome Jon')
else:
  print('You shall not pass!')

age = 25

if age <= 25:
  print(f"I'm sorry, you need to be at least 25 years old")


if username.lower() > 'jannitaca':
    print('Welcome Anna')
else:
    print('You shall not pass!')

list_1 =['uno', 'dos', 'tres']
list_2 =['dos', 'tres', 'uno', ]

if sorted(list_1) == sorted(list_2):
   print ('son iguales')
else:
   print('son distintas')