#Definición del FizzBuzz
def fizzBuzz(n):
    i=1
    while i<=n: #Contador
        if(i % 3 == 0) and (i % 5 == 0):
            print ('FizzBuzz')
        elif i % 3 == 0:
            print ('Fizz')
        elif i % 5 == 0:
             print ('Buzz')
        else:
            print(i)
        i=i+1 #Aumentador
n = int(input("Ingrese el numero para empezar:")) #Ingresa número
fizzBuzz(n) #Invocación de la función