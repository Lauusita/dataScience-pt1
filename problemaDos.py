import numpy as np
import matplotlib.pyplot as plt
import random 

print("MÉTODO NEWTON-RAPHSON") 

def f(x):
    return 2*(x**3)+2*x

def df(x):
    return 6*(x**2)+2

x0 = 1
k=-1 # k representa el número de iteraciones la cual será un valor que incrementará
for i in range(1, 4):
    x1 = x0 -(f(x0)/df(x0)) # se aplica la ecuación
    x0 = x1
    k += 1
    print("Se realizaron ", k, "iteraciones con aproximaciones de ", x0)
  
m=[]    
m.append(x0) #se añaden los valores a un array
min = min(m)

x= np.linspace(-2, 2, 100)
p1=plt.plot(x, 2*(x**3)+2*x)
plt.plot(0, min, "o" )
plt.annotate("AZUL: Newton Raphson", xy=(-1.5, 20), color='blue')

print("MÉTODO BISECCIÓN")

def f(x):
    return 3*(x**3)-6*x 

# Se eligen dos puntos distintos de la ecuación, con tal de que al multiplicar los dos valores en función de f(x) éste dé como resultado negativo
a = random.uniform(5.0, 5.2)
b = random.uniform(5.0, 5.2)*-1
tol = 1
print("los valores tomados en el intervalo son ", a, "y", b)
# Se evalúa que la multiplicación de las funciones sea negativa
if f(a) * f(b) < 0:
    x1 = a
    x2 = b
    k=0 
    for i in range(3):
        while abs(x1-x2) > tol: # se coloca un ciclo while en el que se evalúa que el valor absoluto de la resta de los valores indicados a y b sea mayor a la tolerancia 
            x1 = x2
            x2 = (a+b)/2 
        if f(x2) *f(a)  < 0:
            b = x2
        if f(x2)*f(b) < 0:
            a = x2
        k+=1
        
print("Se realizaron ", k, "iteraciones con aproximaciones de ", x2)
        
if f(a) * f(b) > 0:
    print("La función no cambia de signo. El método de bisección no se pudo aplicar")
        

x= np.linspace(-2, 2, 100)
p2=plt.plot(x,3*(x**3)-6*x  )
plt.plot(0, x2, "o")
plt.annotate("VERDE: Bisección", xy=(-1.5, 15.5), color='green')


print("MÉTODO DE SECANTE")

def f(x):
    return (x**3) + 2*x -1

# Se eligen dos puntos distintos de la ecuación, con tal de que al multiplicar los dos valores en función de f(x) éste dé como resultado negativo

# xi = random.uniform(1.6, 1.7)
# xf = random.uniform(1.8, 1.9)*-1
xi = 1.672396036067921  
xf= -1.9336294365458186
k = 0
print("los valores tomados en el intervalo son ", xi, "y", xf)
# Se evalúa que la multiplicación de las funciones sea negativa

if f(xi)* f(xf) > 0:
    print("La función no cambia de signo. El método de secante no se pudo aplicar")
else:
    for i in range(3):
        x1 = xi
        x2 = xf - (f(xf)*(xi-xf)/f(xf)-f(xi))
        if f(x2) > 0 and f(xi)>0 : 
            xi = x2
        if f(x2) > 0 and f(xf)>0 > 0:
            xf = x2
            
        k += 1    
        print("Se realizaron ", k, "iteraciones con aproximaciones de ", x2)    
        
        # En éste método, a diferencia del de bisección, se evalúa que, tanto x2 o xf y xi evaluada en f(x) tengan el mismo signo
        
    
        
p = []
p.append(x2)
rd = random.choice(p)
plt.title("Segundo problema: métodos")
plt.annotate("MORADO: Secante", xy=(-1.5, 17.5), color='purple')
x= np.linspace(-2, 2, 100)
p3=plt.plot(x,x**3 + 2*x -1)
plt.plot(0.453, rd, "o")
plt.grid()
plt.show()