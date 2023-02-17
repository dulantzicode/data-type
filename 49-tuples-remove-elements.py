import os
os.system('cls')

post = ('Python Basics', 'Intro guide to Python', 'Some cool python content', 'published')

# Removing elements from end
post = post[:-1]

# Removing elements from beginning
post = post[1:]

# Removing specific element (messy/not recommended)
post = list(post) # list(objeto) crea una nueva lista (si () entonces vacía)
post.remove('Intro guide to Python')
post = tuple(post) # tuple(objeto) crea una nueva tupla (si () entonces vacía)
# post = dict() # dict(iterable) crea un nuevo diccionario (si () entonces vacío)

print(post)