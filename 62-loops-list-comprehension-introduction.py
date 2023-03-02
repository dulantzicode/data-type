import os
os.system('cls')


num_list = range(1, 11)
cubed_nums = []

for num in num_list:
  cubed_nums.append(num ** 3)

cubed_nums = [num ** 3 for num in num_list]

print(cubed_nums)

even_numbers = []

for num in num_list:
  if num % 2 == 0:
    even_numbers.append(num)

even_numbers = [num for num in num_list if num % 2 == 0]

print(even_numbers)


#ejercicio
def list_comprehension():
    numbers = (1,2,3,4,5,6)
    result =[num + 1 for num in numbers if (num+1) % 2 ==0]
    print (result)
   
    return result

list_comprehension()