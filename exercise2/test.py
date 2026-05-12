import numpy as np
import matplotlib.pyplot as plt
def my_func(a:int,b:int,c=0) -> int|str:
    """This is a simple function that 
    prints 'Hello, World!' to the console."""
    print("Hello, World!")
    return a+b+c # return is end of function, can use it to our advantage
    
var = my_func(1, 2, 3) # hover of function to see what it does, or use help(my_func) to see the docstring.
# print(help(my_func))
print(var)
var2 = my_func(c=1, b=2, a=3) # can use named arguments to change the order of the arguments
print(var2)

def fibonachhi(n:int) -> int:
    if n < 0:
        return "Input must be a non-negative integer"
    elif n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonachhi(n-1) + fibonachhi(n-2)
print(fibonachhi(10))
# x = np.asarray(range(40))
# print(x)
# y = np.asarray([fibonachhi(i) for i in x])
# plt.plot(x, y)
# plt.savefig('fibonachhi.png')

def fibonnaci_2(n:int) -> int:
    if n < 0:
        return "Input must be a non-negative integer"
    elif n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        a, b = 0, 1
        for _ in range(2, n + 1):
            a, b = b, a + b
        return b
print(fibonnaci_2(100))
# print(fibonachhi(100)) # takes longer
def factorial(n:int) -> int:
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result
print(factorial(5))

def factorial_recursive(n:int) -> int:
    if n < 0:
        return "Input must be a non-negative integer"
    elif n == 0 or n == 1:
        return 1
    else:
        return n * factorial_recursive(n - 1)
print(factorial_recursive(5))

# undefined number of arguments:
def sum_all(*args) -> int:
    print(args) # args is a tuple of all the arguments passed to the function
    return sum(args)
print(sum_all(1, 2, 3, 4, 5))

def print_kwargs(**kwargs) -> None:
    print(kwargs) # kwargs is a dictionary of all the keyword arguments passed to the function
    for key, value in kwargs.items():
        print(f"{key}: {value}")
print_kwargs(a=1, b=2, c=3)

def strange_function(a,b,c,/,d,e):
    return a+b+c+d+e
print(strange_function(1, 2, 3, d=4, e=5)) # the / means that the arguments before it must be positional, and the arguments after it keyword

# positional argument must not follow keyword argument, so this will give an error

a = 0
def func():
    a= 1
func()
print(a) # this will print 0, because the a inside the function is a local variable that is not accessible outside the function

def func2():
    global a # this tells the function to use the global variable a instead of creating a local variable
    a = 1
func2()
print(a) # this will print 1, because the a inside the function is now the global variable that is accessible outside the function

a=[1,2]
def func_3(a):
    a.append(3) # this will modify the original list, because lists are mutable
    return a
print(func_3(a)) # this will print [1, 2, 3]
print(a) # this will also print [1, 2, 3], because the original list was modified, TODO WITHOUT GLOBAL
# Reason: list not normal variable -> sends address of list to function, so when we modify the list inside the function, we are modifying the original list outside the function

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
# Erstellen der Figur und Achsen
fig, ax = plt.subplots()
xdata, ydata = [], []
ln, = ax.plot([], [], 'ro')
# Initialisierungsfunktion
def init():
   ax.set_xlim(0, 2 * np.pi)
   ax.set_ylim(-1, 1)
   return ln,
# Update-Funktion für jedes Frame
def update(frame):
   xdata.append(frame)
   ydata.append(np.sin(frame))
   ln.set_data(xdata, ydata)
   return ln,
# Animation erstellen
ani = FuncAnimation(fig, update, frames=np.linspace(0, 2 * np.pi, 128), init_func=init, blit=True)
plt.show()