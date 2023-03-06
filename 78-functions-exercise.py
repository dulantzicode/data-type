import os
os.system('cls')


def FizzBuzz(max_range):
    max_range +=1
    for number in range(1, max_range):
        if number % 3 == 0 and number % 5 == 0:
            print ('FizzBuzz')
        elif number % 3 == 0:
            print ('Fizz')
        elif number % 5 == 0:
            print ('Buzz')
        else:
            print(number)



FizzBuzz(100)