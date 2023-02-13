sentence = 'The quick brown fox jumped over the lazy dog.'

query = sentence.find('fox')
query_two = sentence.index('over')

print(query)
print(query_two)

query = 'bear' in sentence #devuelve False o True (no existe o sí existe)

print(query)

# en caso de que la subcadena no exista, .find() devuelve -1
#pero .index() da error.
sentence = 'The quick brown fox jumped over the lazy dog.'

query = sentence.find('oops')
query_two = sentence.index('oops')

print(query)
print(query_two)