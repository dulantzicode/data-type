import os
os.system('cls')

post = ('Python Basics', 'Intro guide to Python', 'Some cool python content', 'published')

print(post[:2])
# rango estandar
# primer argumento es el índice de inicio
# segundo es el indice del final
# (recordar que se para justo antes de ese,
# por lo que también podría ser el número de items
# a recuperar)

print(post[1::2])
# rango extendido
# primer argumento el índice de inicio
# segundo argumento el índice de final
# tercer argumento el valor de salto
# igual que slice() con listas  

slice_obj = slice(1, (len(post)), 2)

print(post[slice_obj])