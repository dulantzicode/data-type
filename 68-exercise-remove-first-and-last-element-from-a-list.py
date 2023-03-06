import os
os.system('cls')

#mi respuesta
html = ['<h1>', 'My content', '</h1>']


def remove_first_and_last(list_to_clean):
    del(list_to_clean[0])
    del(list_to_clean[-1])
    return

remove_first_and_last(html)
print(html)


#respuesta del profe
def remove_first_and_last(list_to_clean):
  _, *content, _ = list_to_clean
  return content

# agregar un * antes de una variable indica que esa variable se lleva todos los 
# valores de la lista que no estén asignados a otras variables. 


html = ['<h1>', 'My content', '</h1>']

print(remove_first_and_last(html))

other_content_to_clean = ['', 'My content', 'Something else', '/']

print(remove_first_and_last(other_content_to_clean))


#ampliación del ejercicio
def remove_first_and_last(list_to_clean):
  if len(list_to_clean) <3:
      print ('Sorry, the list must have 3 elements al least')
      content = []
  else:
      _, *content, _ = list_to_clean
  return content


html = ['<h1>', 'My content', 'dos', 'tres']

cleaned_list = (remove_first_and_last(html))
print (cleaned_list)