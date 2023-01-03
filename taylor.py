import sympy 
from sympy import * 
import numpy as np 
import matplotlib.pyplot as plt 

def derivar(func,x):
    func_derivada = diff(func, x)
    return func_derivada 

def evaluar(fc,x):
    y = eval(fc) 
    return y 

def graficar(intervX, intervY, interv_taylor):
    plt.plot(intervX, intervY,'r-', label ="Funcion Original")
    plt.plot(intervX, interv_taylor, 'b:' , label = "Funcion con estimacion Taylor =")
    plt.title("Grafica Teorema Taylor")
    plt.xlabel("x")
    plt.ylabel("f(x)")
    plt.grid(True)
    plt.legend()
    plt.show


    x = var('x')
    print ("Ingrese funcion a graficar: ")
    fc = eval(input("Funcion: "))
    xa = float(input("ingrese valor de xa: "))
    xb = float(input("ingrese valor de xb: ")) 
    delta = 0.01
    t = 1 

    intervalo_X = np.arange(xa,xb, delta)
    intervalo_Y = []
    intervalo_taylor = []

    der1 = derivar(fc , x)
    der2 = derivar(der1, x)


    for valor in intervalo_X: 
        valor = valor + delta 
        y = evaluar(str(fc) , valor)  
        intervalo_Y.append(y)
    
    for i in intervalo_X: 
        eTaylor = evaluar(fc, i) + evaluar(str(der1), i) * delta + 0.5*delta * (evaluar(str(der2), i+t*delta))*delta
        intervalo_taylor.append(eTaylor)

    graficar(intervalo_X , intervalo_Y , intervalo_taylor)