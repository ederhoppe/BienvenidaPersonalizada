# 2. Escribe un programa que le pida primero su nombre al usuario, 
# posteriormente su apellido, crea una variable de nombre completo 
# concatenando el nombre y el apellido y muestra en pantalla un 
# mensaje de bienvenida utilizando la variabla con el nombre completo.

print('Bienvenido, ¿Quieres concatenar tu nombre y apellido?')
first_name = input('Ingresa tu nombre: ')
print('Tu nombre es: ',first_name)
last_name = input('Ingresa tu apellido: ')
print('Tu apellido es: ', last_name)
full_name = first_name + last_name
print('Bienvenido', full_name)