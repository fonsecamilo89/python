
# mensaje = "hola soy camilo"
# print(mensaje)
# print("su mensaje mide: " + str(len(mensaje)))




 # This program says hello and asks for my name.

print('Hello, world!')
print('What is your name?') # ask for their name

myName = input()

print('It is good to meet you, ' + myName)
print('The length of your name is: ' + str(len(myName)))
#len() recibe un string y cuenta el número de caracteres a contar

print('What is your age?') # ask for their age

myAge = input()

print(type(myAge))

print('You will be ' + str(int(myAge) + 1) + ' in a year.')
# Es necesario realizar casting de myAge con int(myAge) para poder sumarle 1.
# Posteriormente es necesario convertir la suma a string para poder mostrar el resultado