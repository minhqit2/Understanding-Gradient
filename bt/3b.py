from __future__ import division, print_function, unicode_literals
import math
import numpy as np 
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib.animation import FuncAnimation 

x0=4

def f(x):
    return (x**2+3*x-1)/(x+1)
def grad(x):
    return (x**2+2*x+4)/((x+1)**2)
# Khoi dong random 1 x o vi tri bat ki


def myGD1(x0, eta = 0.1):
    x = [x0]
    eta = 0.1
    for it in  range(100):
        x_new = x[-1] - eta*grad(x[-1])
        if abs(grad(x_new)) < 1e-3:
            break
        x.append(x_new)
    x=np.asarray(x)
    return(x,it)

def viz_alg_1d_2(x, cost, filename = 'nomomentum1d.gif'):
#     x = x.asarray()
    it = len(x)
    y = cost(x)
    xmin, xmax = np.min(x), np.max(x)
    ymin, ymax = np.min(y), np.max(y)
    xmin, xmax = -4, 6
    ymin, ymax = -12, 25
    x0 = np.linspace(xmin-1, xmax+1, 1000)
    y0 = cost(x0)
       
    fig, ax = plt.subplots(figsize=(4, 4))  
    
    def update(i):
        ani = plt.cla()
        plt.axis([-4 , 6, -13, 26])
        plt.plot(x0, y0)
        plt.axis([xmin, xmax, ymin, ymax])
        ani = plt.title('$f(x) = (x^2+3x-1)/(x+1); x_0 = 4; \eta = 0.1$')
        if i == 0:
            ani = plt.plot(x[i], y[i], 'ro', markersize = 7)
        else:
            ani = plt.plot(x[i-1], y[i-1], 'ok', markersize = 7)
            ani = plt.plot(x[i-1:i+1], y[i-1:i+1], 'k-')
            ani = plt.plot(x[i], y[i], 'ro', markersize = 7)
        label = 'GD without Momemtum: iter %d/%d' %(i, it)
        ax.set_xlabel(label)
        return ani, ax 
        
    anim = FuncAnimation(fig, update, frames=np.arange(0, it), interval=200)
    anim.save(filename, dpi = 100, writer = 'imagemagick')
    plt.show()
# x = np.asarray(x)
(x,eta) = myGD1(3, 0.1)
viz_alg_1d_2(x, f)