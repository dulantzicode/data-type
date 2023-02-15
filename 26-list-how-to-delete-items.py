import os
os.system('cls')

users = ['Kristine', 'Tiffany', 'Jordan', 'Leann']

print(users)

users.remove('Jordan')

print(users)

popped_user = users.pop(1) #almacena en una variable el valor borrado
                          #(sin no hay índice, el último de la lista)

print(popped_user)
print(users)

del users[0]

print(users)