import os
os.system ("cls") 
# https://www.google.com/search?q=python+development+tutorial

uri = 'https://www.google.com/search?q='
tags = ['python', 'development', 'tutorial']
formatted_tags = '+'.join(tags)
query_uri = f'{uri}{formatted_tags}'

print(query_uri)
print()


lista = ['uno','dos','tres']
resultado = '= -cuatro'

operacion = '-'.join(lista)
operacion_completa = operacion + resultado
print(operacion_completa)
print(operacion, resultado)