import math

loss = -20.25
product_cost = 89.99

print(abs(loss))

print(math.floor(product_cost))#redondea hacia abajo
print(math.ceil(product_cost))#redondea hacia arriba
#nota con números negativos funciona "al revés".
# -20,25  floor sería -21 y ceil -20

print(abs(math.floor(loss)))
print(round(product_cost)) #redondea al valor más cercano
                           # añadiendo al argumento
                           # ',' y un valor n
                           # redondea a esos decimales
print(math.sqrt(product_cost))
print(math.pow(5, 2))
print(5 ** 2)