#El algoritmo programado que calcule el gradiente numérico de la función, dada la función fX, el vector de variables X y el vector de pasos ΔX.
#La forma en que se puede calcular el gradiente de la función f(x,y)=x2+y2+pxy utilizando wxMaxima o Maple

f = "x**2 + y**2"
x = [2,3,4,5,6]
deltax = [0.02 , 0.04 , 0.06 , 0.08, 0.10]
y = [1,3,5,6,7]
deltay = [0.01, 0.5, 0.07, 0.09, 0.11]

def evalua_fx(func, x , y):
    derivadax = eval(func)
    #print (derivadax)
    return derivadax

def evalua_fy(func, y , x):
    derivaday = eval(func)
    return derivaday


def derivar(x, deltax , y , deltay):
    dX = (evalua_fx(str(f), x + deltax , y) - evalua_fx(str(f) , x , y)) /deltax
    dY = (evalua_fy(str(f), y + deltay , x) - evalua_fy(str(f) , y , x)) /deltay
    return (dX , dY)

for i in range(len(x)):
    print (derivar(x[i], deltax[i], y[i], deltay[i]))