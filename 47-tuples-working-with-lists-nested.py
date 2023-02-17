import os
os.system('cls')

post = ('Python Basics', 'Intro guide to Python', 'Some cool python content')

tags = ['python', 'coding', 'tutorial']
#tags = ('python', 'coding', 'tutorial')

post += (tags[0],)
post += (tags[1],)
post += (tags[2],)
post += (tags,)
# Se pueden anidar otras tuplas o listas dentro de una tupla

print(post)

print(post[-1][1])
print(post[-1])