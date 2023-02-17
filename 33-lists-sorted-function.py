import os
os.system("cls")

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

sorted_list = sorted(sale_prices, reverse=True)
# sorted_list = sorted(sale_prices[0::2], reverse=True) 
# también se puede indicacar un rango

print(sorted_list)