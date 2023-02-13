import os

import math

"""
Tools:
- math library
- sorted function
- list slicing
- computations
"""

sale_prices = [
  100,
  83,
  220,
  40,
  100,
  400,
  10,
  1,
  3
]

sale_prices_sorted= sorted(sale_prices)

num_items = len(sale_prices)
center_value = num_items // 2
#center_value = math.floor(num_items / 2)

mediana = sale_prices_sorted [center_value:(center_value+1)]
mediana_int = int(mediana)

print (sale_prices_sorted)
print(num_items)
print(center_value)
print(mediana)