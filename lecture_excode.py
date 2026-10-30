import numpy as np
import scipy.integrate as integ

def f(t,y):
    B = 1.0
    C = 1.0
    D = 1.0
    Omega = 5.0
    dydt = np.array([0.0,0.0]) #create array, initialize to 0
    dydt[0] = y[1]
    dydt[1] = -B*y[1] - C*y[0] + D*np.cos(Omega*t)

    return dydt

y_0 = np.array([1.0, 0.0]) #stationary, displaced from 0 

t_eval = np.arange(0.0, 10.0, 0.1) #for plotting purposes

soln = integ.solve_ivp(f, (0.0, 10.), y_0, t_eval = t_eval) 
