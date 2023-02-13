heading = "Python: An Introduction: and Python: Advanced"

header, _, subheader, final = heading.partition(': ')

#utiliza ': ' (o lo que sea que haya) como punto de corte
#el '_' representa una variable que no se va a usar
#el punto de corte tambíen se considera parte de la división
#en este caso 'Python', ': ' y 'An Intr...: Advanced'
# solo coje el primer divisor.
# si hay más hay que iterar.
# porque solo devuelve tres elementos
 

print(header)
print(subheader)


first, second, third = heading.partition(': ')

print(first)
print(second)
print(third)


