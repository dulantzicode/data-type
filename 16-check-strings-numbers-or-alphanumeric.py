api_data = '5'
greeting = 'Hi there'

print(api_data.isalpha())
print(greeting.isalpha()) #solo funciona si todos los
# caracteres son letras, y el ' ' no lo es.

# normalente es preferible este.
print(api_data.isnumeric())
print(greeting.isnumeric())