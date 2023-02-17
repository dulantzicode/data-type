import os
os.system('cls')


# List: []
# Dictionary: {}
# Tuple: ()

# Tuple: immutable, eso implica ciertas restricciones, aunque sí se pueden actualizar.
# List: mutable

post = ('Python Basics', 'Intro guide to python', 'Some cool python content')
# al ser inmutable no se puede ordenar con el método var.sort()
# pero sí se puede crear una nueva lista con la función sorted(var)

post_sorted = sorted(post)
print(post_sorted)
# Tuple unpacking
title, sub_heading, content = post

# Equivalent to Tuple unpacking
# title = post[0]
# sub_heading = post[1]
# content = post[2]
# También se puede acceder a los valores del objeto tupla a través de
# sus índices.

print(post)
print(title)
print(sub_heading)
print(content)