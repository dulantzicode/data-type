import os
os.system ("cls") 

tags = [
  'python',
  'development',
  'tutorials',
  'code',
  'programming',
  'computer science'
]

#tag_range = tags[1:-1:2] # El último valor indica que se tomen los elementos
                          # de n en n valores
                          # en este caso cada dos elementos

#tag_range = tags[::-1] # Esto invierte el valor del índice de cada elemento
                       # es decir crea una nueva lista pero empezando por
                       # el final (no confundir con .sort(reverse=True))
                       # si el valor negativo es mayor, entonces salta
                       # como en el caso anterior, pero desde atrás.
                       # no se puede indicar nada en el primer rango,
                       # pero sí en el intermedio (se para ahí).

#print(tag_range)
print(tags[:2:-1])
print(tags)

tags.sort(reverse=True)

print(tags)