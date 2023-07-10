import numpy as np
import matplotlib.pyplot as plt

# PRIMERA ECUACIÓN
def f(x, y):
    return 7*(x**3) + 10*x*y + 1

def df(x, y):
    return 21*(x**2) + 10*y

#SEGUNDA ECUACIÓN
def g(x, y):
    return 8*(x**3) + 11*x+y + 1

def dg(x, y):
    return 24*(x**2) + 11*y 

#TERCERA ECUACIÓN 
def f2(x, y):
    return x**2+x*(y**3)+9

def df2(x, y):
    return 2*x+y**3

#CUARTA ECUACIÓN
def g2(x, y):
    return 3*(x**2)*y + y**3 + 4

def dg2(x, y):
    return 6*x*y 


x= np.linspace(-2, 2, 100)
y= np.linspace(-2, 2, 100)

x0=5
y0=5
itc=0
print("Para la primera situación en f(x) se tiene que: ")
for i in range(1, 11):
    x1 = x0 - (f(x0, y0)/df(x0, y0))
    x0= x1
    itc += 1
    print("Se realizaron ", itc, "iteraciones con aproximaciones de ", x0)


print("Para la primera situación en g(x) se tiene que: ")
x2=1
y2=1
itc=0
for i in range(1, 11):
    x1 = x2 - (g(x2, y2)/dg(x2, y2))
    x2 = x1
    itc += 1
    print("Se realizaron ", itc, "iteraciones con aproximaciones de ", x2)
    
    
print("Para la segunda situación en f(x) se tiene que: ")
x3=25
y3=-2
itc=0
for i in range(1, 11):
    x1 = x3 - (f2(x3, y3)/df2(x3, y3))
    x3= x1
    itc += 1
    print("Se realizaron ", itc, "iteraciones con aproximaciones de ", x3)
    
print("Para la segunda situación en g(x) se tiene que: ") 
x4=1
y4=-0.91
itc=0
for i in range(1, 11):
    x1 = x4 - (g2(x4, y4)/dg2(x4, y4))
    x4= x1
    itc += 1
    print("Se realizaron ", itc, "iteraciones con aproximaciones de ", x4)
    
    
# AZUL
fx= plt.plot(x, 7*(x**3) + 10*x*y + 1) 
# NARANJA
gx=plt.plot(x, 8*(x**3) + 11*x+y + 1)
# # VERDE
f2x= plt.plot(x, x**2+x*(y**3)+9)
# # ROJO
g2x= plt.plot(x, 3*(x**2)*y + y**3 + 4)

plt.grid()
plt.title("Primer problema: Newton Raphson")
plt.plot(-1.5, -0.09931430116285475,  "o")
plt.plot(-0.085, -0.06576819407008089, "o")
plt.plot(0, 9.661458333333332, "o")
plt.plot(-1, 1.090489858672758, "o")
plt.show()
