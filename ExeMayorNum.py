# Encontrar el número menor de un conjunto de números e imprimir la comparación

larguest_so_far = -1 #inicio
print('Before,' , larguest_so_far)

a= int (input('ingrese el primer número: '))
b= int (input('ingrese el segundo número: '))
c= int (input('ingrese el tercer número: '))
d= int (input('ingrese el cuarto número: '))
e= int (input('ingrese el quinto número: '))
f= int (input('ingrese el sexto número: '))

for the_num in [a, b, c, d, e, f]: #Loop y cadena de numeros
    if the_num > larguest_so_far: #condicional (se puede cambiar para buscar el menor)
        larguest_so_far = the_num #Guardar el númeor calculado 
    print (larguest_so_far, the_num) # imprimir comparación

print('After', larguest_so_far) #mostrar el mayor
