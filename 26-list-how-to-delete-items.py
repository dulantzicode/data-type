users = ['Kristine', 'Tiffany', 'Jordan', 'Leann']

print(users)

users.remove('Jordan')

print(users)

popped_user = users.pop() #almacena en una variable el valor borrado
                          #(el último de la lista)

print(popped_user)
print(users)

del users[0]

print(users)