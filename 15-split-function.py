import os
os.system('cls')


tags = 'python,coding,programming,development'
# esto es un string

list_of_tags_one = tags.split(',')
# esto nos crea un lista 'list'o 'collection'
# (o array en otros lenguajes)

list_of_tags_two = tags.split(',')[0]
# esto nos crea un lista 'list'o 'collection'
# (o array en otros lenguajes) pero solo toma el índice indicado

list_of_tags_three = tags.split()
# si no se añaden argumentos lo que hace es convertir
# el string en una colección de un solo item

print(list_of_tags_one)
print(list_of_tags_two)
print(list_of_tags_three)

heading = "Python: An Introduction"

heading, subheading = heading.split(': ')

print(heading)
print(subheading)

