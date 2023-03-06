import os
os.system('cls')

sentence = 'The quick brown fox jumped over the lazy Dog'
word = 'dog'

if word.lower() in sentence.lower():
  print('The word is in the sentence')
else:
  print('The word is not in the sentence')


nums = [1, 2, 3, 4]

if 3 in nums:
  print('The number was found')
else:
  print('The number was not found')


if 3 | 4 in nums:
  print('The numbers were found')
else:
  print('The numbers were not found')


#ejercicio

def value_in_string():
    sentence = 'Python is the best!'
    
    if 'Python' in sentence: 
      print('The word Python is in the sentence')
    else:
      print('The word is not in the sentence')



value_in_string()




