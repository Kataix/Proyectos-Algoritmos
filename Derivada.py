#Deberá realizar dos algoritmos. El primero, para calcular 
# la derivada numérica de una función dado un Δx. 
# El segundo, para calcular el Δx mediante el cual se consigue que el error entre la derivada explícita y la derivada numérica sea menor que un error ϵ.

def evaluar(x):
    z=eval(f)
    return z

dx = eval(input("Ingrese delta x :"))
x = eval(input("ingrese x: "))
f = input("Ingrese funcion: ")

derivada = (evaluar(x+dx)-evaluar(x))/dx
print (derivada )