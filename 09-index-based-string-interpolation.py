name = 'Kristine'
age = 12
product = 'Python eLearning course'
from_account = 'Jordan'

# con la función .format() se asigna un índice a las variables
#y así se pueden imprimir dentro de un string
#es un metodo en desuso
greeting = "Product Purchase: {2} - Hi {0}, you are listed as {1} years old. - {3}".format(name, age, product, 'Jordan')

#se obtiene el mismo resultado que con "f"
greeting2 = f"Product Purchase: {product} - Hi {name}, you are listed as {age} years old. - {from_account}"

print(greeting)
print(greeting2)