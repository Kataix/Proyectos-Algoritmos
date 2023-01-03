import sympy   

def evaluar(x,funcion):
    z = eval(funcion)
    return z


def derivar(valor_x , f ): 
    x = sympy.symbols('x')
    f_derivada = sympy.diff(f,x)
    resultado_eval = evaluar(valor_x , str(f_derivada))
    return resultado_eval

def comprobar_condicion(x,dx, e):
    calculo = abs(derivar(x,f) - ( evaluar(x + dx, f) - evaluar(x,f)) / dx)
    print ("Valores evaluados: " , dx)
    if calculo > e :
        return True
    else: 
        return False

dx = eval(input("Ingrese valor de delta x: "))
x = eval(input ("Ingrese un valor para x: "))
e = eval(input ("Ingrese un valor para epsilon: "))
f = (input ("Ingrese funcion: "))

while ( comprobar_condicion(x,dx,e)):
    dx = dx/2
    

print ("El valor que debe tomar dx para que se cumpla la condición debe ser : " , dx)