import os
os.system ("cls") 


name = 'Kristine'
product = 'Python elearning course'

email_content = f"""
Hi {name}

Thank you for purchasing {product}

Regards,

Sales Team
"""

print(email_content)


first_name = 'David'
last_name = 'Gomez'

def function(first_name, last_name):
    greeting = f'Hello, {first_name} {last_name}'
    #si necesito imprimir los corcehtes "{}" como parte 
    # de un texto (ej {corchetes})
    # entonces lo envuelvo con otros corechetes
    # ejemplo {{corchetes}}
    
    
    return greeting

print('---------')
print (function(first_name, last_name))