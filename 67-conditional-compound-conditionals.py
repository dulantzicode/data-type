import os
os.system('cls')

username = 'jonsnow'
email = 'jon@snow.com'
password = 'thenorth'

if username == 'jonsnow' and password == 'thenorth':
  print('Access permitted')
else:
  print('Not allowed')


if (username == 'jonsnow' or email == 'jon@snow.com') and password == 'thenorth':
  print('Access permitted')
else:
  print('Not allowed')


if username == 'jonsnow' or password == 'thenorth':
  print('Access permitted')
else:
  print('Not allowed')


logged_in = True
standard_user = False

if logged_in and not standard_user:
  print('You can access the admin dashboard')
else:
  print('You can only access the standard dashboard')


  #ejercicio
number =26
if number in range(1,101):
    print("Success!")
else:
    print("Failure...")




def compound_conditional(number):
    if number >= 1 and number <=100:
        print("Success!")
    else:
        print("Failure...")

compound_conditional(101)