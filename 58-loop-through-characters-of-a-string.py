import os
os.system('cls')


alphabet = 'abcdef'

for letter in alphabet:
  print(letter)


print(alphabet[1:3])

def loop_over_string():
    name = 'David'
    for letter in name:
            print (letter)
    return name

loop_over_string()