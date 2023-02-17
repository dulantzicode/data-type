import os
os.system('cls')


post = ('Python Basics', 'Intro guide to python', 'Some cool python content')

print(id(post))
print(id(post))
# La función id() nos devuelve el número de identificación de un objeto.
# Este id es único y persistente para cada objeto.
# Sin embargo, aquí vemos que el id de 'post' es diferente después de la 
# reasignación, por lo que podemos constatar que se trata de un objeto
# diferente y que el primero ha sido eliminado.


post += ('published',)
#### IMPORTANTE: añadir una coma después del valor para que Python
# considere el valor como parte de una tupla y no como un string,
# porque, entonces, no podrá añadir el nuevo valor a la tupla.
# De hecho, lo que hacemos con esta instrucción es crear una nueva
# tupla con el mismo nombre que la anterior.

print(id(post))

title, sub_heading, content, status = post

print(title)
print(sub_heading)
print(content)
print(status)