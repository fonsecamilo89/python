print('Hello, world!')
print('What is your name?') # ask for their name

myName = str(input())

print('It is good to meet you, ' + myName)
print('The length of your name is: ' + str(len(myName)))
#len() recibe un string y cuenta el número de caracteres a contar

print('What is your age?') # ask for their age

myAge = int(input())

print(myAge)
print(type(myAge))

print('You will be ' + str(myAge + 1) + ' in a year.')
# Es necesario realizar casting de myAge con int(myAge) para poder sumarle 1.
# Posteriormente es necesario convertir la suma a string para poder mostrar el resultado