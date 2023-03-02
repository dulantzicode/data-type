import os
os.system('cls')

legacy_customers = ['Alice', 'Bob']
new_customers = ['Tiffany', 'Kristine']

raw_db = [legacy_customers, new_customers]

print(raw_db)

for legacy_customer in legacy_customers:
  new_customers.append(legacy_customer)

print(new_customers)


#ejercicio
def loop_over_list():
    numbers = [1,2,3,4,5,6]
    result = []
    
    for number in numbers:
       result.append((number)+1)
    
    print (result)
    
    return result

loop_over_list()
