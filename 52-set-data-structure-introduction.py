import os
os.system('cls')

# Uniqueness
# this means that an element is present only once
# cada elemento presente siempre será único.
tags = {
  'python',
  'coding',
  'tutorials',
  'coding'
}

print(tags)

# Nope 
# el contenido de un objeto set no se puede indexar como una lista.
# print(tags[0])

# pero si se puede comprobar la existencia o no de un valor
query_one = 'python' in tags
query_two = 'ruby' in tags

print(query_one)
print(query_two)