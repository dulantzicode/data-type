import os
os.system('cls')

def heading_generator(text, heading_type):
    return f'<h{heading_type}>{text}</h{heading_type}>'



text_in = 'Hello world, again'
heading = '3'


print(heading_generator(text_in, heading))