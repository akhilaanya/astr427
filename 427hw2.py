#Akhila Pisupati: ASTR 427 HW 2
#October 17, 2026

import scipy.integrate as integrate
import numpy as np
import matplotlib.pyplot as plt
import time

#Problem 1
#Euler method

#The derivative function takes, for some time and position, the derivative (of a derivative y, defined below) 
#This is fitting for a harmonic oscillator whose acceleration follows Hookes' law: F = ma = -kx so a is proportional to -x 
def derivative(t,y):
    dy_dt = -y 
    return dy_dt

#The Euler method function takes initial conditions wrapped in the initial_vector parameter, applies the derivative function for a fixed time step until the end of a time interval
def euler_method(initial_vector, derivative, h, end_of_time):
    t = 0.0
    try:
        ylist = [np.array(initial_vector, dtype = float)]#Create an array (for derivatives of y), initialize with initial conditions in a vector
        tlist = [0.0] #Initializing the time array
        t = 0.0  
    
        while t + h <= end_of_time: #while adding time steps before reaching the end of the time interval
            y_now = ylist[-1] #grabs the latest number in the array (for first iteration, is dy0_dt, packed into initial vector)

            if t + h > end_of_time: #if the end of the interval is reached or exceeded
                h = end_of_time - t #so that the last step gets to the end of the interval exactly and does not go over
            
            y_next = y_now + h*np.array(derivative(t, y_now)) #calculates the next step using the Euler method (in class)
            #further step = step + step size * derivative on that original step
            t = t + h #take a step h
            ylist.append(y_next) #add this next step to the list of steps as the latest one
            tlist.append(t)
 

        return np.array(tlist), np.array(ylist)

    except Exception as e:
        print("An error has occurred:", e)

#Runge-Kutta method (fourth order)
#For some initial conditions
def runge_kutta(tlist, ylist, y0, derivative, step, end_of_time):
    try:
        ylist = [np.array(y0, dtype = float)] #create an array with initial value of y (zeroth derivative)
        tlist = [0.0]
        t = 0.0

        while t < end_of_time: 
            y_now = ylist[-1] #current latest position without the step

            if t + step > end_of_time:
                step = end_of_time - t #so that the last step gets to the end of the interval

            #Defining derivatives k1-k4, according to the RK method 
            k1 = np.array(derivative(t, y_now))
            k2 = np.array(derivative(t + 0.5*step, y_now + 0.5*k1*step))
            k3 = np.array(derivative(t + 0.5*step, y_now + 0.5*k2*step))
            k4 = np.array(derivative(t + step, y_now + k3*step))

            y_next = y_now + (step/6) * (k1 + 2*k2 + 2*k3 + k4) #Applies the fourth-order Runge Kutta formula to find the next y after taking a step
            
            t = t + step
            tlist.append(t) #take a step
            
            ylist.append(y_next) #add this next y-step to the list of derivatives

        return np.array(tlist), np.array(ylist)
    
    except Exception as e:
        print("An error has occurred:", e)
        

#Leapfrog method

def leapfrog(xder, vder, first_x, first_v, step, end_of_time):
    try:
        xlist = [first_x] #creating an array of x's to step in, starting with first step
        vlist = [first_v] #same for v
        tlist = [0.0]
        t = 0.0
        
        while t < end_of_time: #first updating v, so going through xlist
            if t + step > end_of_time:
                step = end_of_time - t #so that the last step gets to the end of the interval 

            v_now = vlist[-1] #most recent velocity and position
            x_now = xlist[-1]


            t = t + step #update time
            tlist.append(t)

            v_half = np.array(v_now) + 0.5*step*np.array(vder(x_now)) #Leapfrog equation for v after a half time-step 
            
            x_next = np.array(x_now) + step*np.array(xder(v_half))
            xlist.append(x_next) #adding your full x step to the array
            
            v_next= np.array(v_half) + 0.5*step*np.array(vder(x_next))
            vlist.append(v_next) #adding your full v step to the array


        return np.array(xlist), np.array(vlist), np.array(tlist)

    except Exception as e:
        print("Here is the error that has occurred", e)

#Problem 2
initials = [1, 0] #at t = 0 for x and x'
step_sizes = [1, 0.3, 0.1, 0.03, 0.01] #given step sizes
time_end = 30 #end of the time interval
x_soln = np.cos(30) #solution at the end of the time interval

#Problem 2a
#RK method, finding the derivatives in the same manner as above
def der_harmonic(t, vector): #Calculating the derivative 
    try:
        x, vel_x = vector
        second_der_x = -x #rewriting DE given to make it solvable
        gradient = [vel_x, second_der_x] #saving the DE and the velocity (first derivative) as a list for easy access to the values in these indices 
        
        return gradient
    
    except Exception as e:
        print("error:", e)

#Finding the derivatives for the Leapfrog method in the same manner as above (problem 1)

def xder_harmonic(velocity): 
    return velocity

def vder_harmonic(position):
    try:
        lpf_x = position
        return -lpf_x
    
    except Exception as e:
        print("There was an error:", e)


for h in step_sizes: #for the set of steps instructed in the problem (1, .3, .1, ...), doing this integral calculation and plotting them. 
    t_list, y_list = runge_kutta(None, None, initials, der_harmonic, h, time_end) #RK method

    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))

    ax1.plot(t_list, y_list[:,0], color='purple', label=f'h = {h:.2f}')
    
    lpfx_list, lpfv_list, lpft_list = leapfrog(xder_harmonic, vder_harmonic, 1, 0, h, time_end) #Leapfrog method
    ax1.plot(lpft_list, lpfx_list, color='yellow')
    ax1.set_xlabel('time')
    ax1.legend()
    ax1.set_ylabel('x position')

    tlist_euler, ylist_euler = euler_method(initials, der_harmonic, h, time_end) #Euler method - plotted separately so that all positions are visible easily
    ax2.plot(tlist_euler, ylist_euler[:, 0], color = 'red', label=f'Euler h = {h:.2f}')
    ax2.set_xlabel('time')
    ax2.legend()
    ax2.set_ylabel('x position')
    
    plt.tight_layout()
    plt.show()
    

#Problem 2b
rk_errors = []

lpf_errors = []

euler_errors = [] #Generating a list of errors (initially empty, to be added to and then plotted for each of the 3 methods)

#Problem 2b
for h in step_sizes:
    t_list, y_list = runge_kutta(None, None, initials, der_harmonic, h, time_end)
    rk_errors.append(abs(y_list[-1, 0] - x_soln)) #numerical solution minus exact solution
    
    lpfx_list, lpfv_list, lpft_list = leapfrog(xder_harmonic, vder_harmonic, 1, 0, h, time_end) 
    lpf_errors.append(abs(lpfx_list[-1] - x_soln)) #repeated for Leapfrog and Euler (below) 

    tlist_euler, ylist_euler = euler_method(initials, der_harmonic, h, time_end)
    euler_errors.append(abs(ylist_euler[-1, 0] - x_soln))
    #finding the error as the absolute value of the difference between the calculated value and actual value (standard)


log_steps = np.log10(step_sizes) #finding the logs of the step sizes and errors calculated above to plot on the graph
log_errsrk = np.log10(rk_errors)
log_errslp = np.log10(lpf_errors)
log_errseu = np.log10(euler_errors)

plt.figure(figsize=(6, 6))
plt.plot(log_steps, log_errsrk, color='pink', label='RK Method')
plt.plot(log_steps, log_errslp, color='yellow', label='Leapfrog Method')
plt.plot(log_steps, log_errseu, color='red', label='Euler Method')
plt.xlabel('log(stepsize)')
plt.ylabel('log(|x_numerical(30) - x_exact(30)|)')
plt.legend()
plt.show()
        
#Problem 3
def der_orbit(t, vector):
    try:
        x, y, vel_x, vel_y = vector
        #defining your vector of position/velocity for x,y to pass into Problem 1 functions: can only pass one thing
        #basically expanding an array 

        potential = -(1 + x**2 + y**2)**(-0.5) #equation given for potential

        denom = (1 + x**2 + y**2)**(1.5)
        #just to make the math easy, separating derivatives given into -x/denom and -y/denom

        second_der_x = -x/denom
        second_der_y = -y/denom

        gradient_potential = [vel_x, vel_y, second_der_x, second_der_y] #elements needed, just saving them as an array

        return gradient_potential

    except Exception as e:
        print("There was an error :", e)

#Problem 3a - Runge Kutta!
initial_vector = [1.0, 0.0, 0.0, 0.3] #initial conditions given
step_sizes = np.arange(0.01, 1.1, 0.1) #taking increasing step sizes from 0.01 to 1 in increments of 0.1 at a time, making sure the calculation actually occurs for step size = 1 

for h in step_sizes:
    t_list, y_list = runge_kutta(None, None, initial_vector, der_orbit, h, 100.0) #calling RK for every 0.1 incremented increase of step size
    
    plt.figure(figsize=(6, 6))
    plt.plot(y_list[:,0], y_list[:,1], color='purple', label = f'h = {h:.3f}')
    plt.title(f'h = {h:.3f}')
    plt.xlabel('x position')
    plt.ylabel('y position') #plotting positions/orbits for each step size tested
    plt.show()

#Problem 3b - plotting energy
def finding_energy(t, vector):
    try:
        x = vector[:, 0]
        y = vector[:, 1] #creating a four vector of [x, y, vel_x, vel_y]
        vel_x = vector[:, 2]
        vel_y = vector[:, 3]
        potential = -(1 + x**2 + y**2)**(-0.5) #equation for potential given, function of x, y (indices 0 and 1)

        energy = ((vel_x)**(2) + (vel_y)**(2))/2 + potential #equation for energy given as a function of the elements of the vector

        return energy
    
    except Exception as e:
        print("There was an error", e)

for h in step_sizes:
    t_list, y_list = runge_kutta(None, None, initial_vector, der_orbit, h, 100.0)
    
    energy = finding_energy(t_list, y_list)

    plt.figure(figsize = (6,6))
    plt.plot(t_list, energy, color = 'blue') #calling the function to find the energy and plot it over time for each incremented step size
    plt.xlabel('time')
    plt.ylabel('energy')
    plt.show()

#Problem 3c - plotting energy again, fixed step sizes, now with both RK and Leapfrog methods
#Leapfrog
time_end = 100000 #given this and step size
stepsize = 0.4 #avoiding hardcoding

def xder_orbit(velocity): #to pass into Leapfrog
    lpfvel_x, lpfvel_y = velocity #creating a velocity vector 
    return velocity #just return 

def vder_orbit(position): #to pass into Leapfrog
    try:
        lpf_x, lpf_y = position #creating a position vector
        denom = (1.0 + lpf_x**2 + lpf_y**2)**(1.5) #making the writing shorter again by defining denominator separately
        
        return [-lpf_x/denom, -lpf_y/denom]
        #gives you second derivatives to integrate
    
    except Exception as e:
        print("Here's an error: ", e)

#Initial conditions
lpf_initx, lpf_inity = [1.0, 0.0] #initial conditions
lpf_initvx, lpf_initvy = [0.0, 0.3]

lpf_start = time.time() #timing how long it takes to do the Leapfrog integration 
lpfx_list, lpfv_list, lpft_list = leapfrog(xder_orbit, vder_orbit,
                                           [lpf_initx, lpf_inity], [lpf_initvx, lpf_initvy], stepsize, time_end)
lpf_end = time.time()
lpf_wallclock = lpf_end - lpf_start
print(f"The wall clock time for the Leapfrog method is {lpf_wallclock:.2f}")

lpf_potential = -(1 + (lpfx_list[:,0])**(2) + (lpfx_list[:,1])**(2))**(-0.5) #redefining potential and energy with Leapfrog-specific variables

lpf_energy = ((lpfv_list[:,0])**(2) + (lpfv_list[:,1])**(2))/2 + lpf_potential


#Runge-Kutta
rk_start = time.time() #doing the same as Leapfrog method above but for RK method
rkt_list, rky_list = runge_kutta(None, None, initial_vector, der_orbit, stepsize, time_end)
rk_end = time.time()
rk_wallclock = rk_end - rk_start
print(f"The wall clock time for the Runge-Kutta method is {rk_wallclock:.2f}")

rk_energy = finding_energy(rkt_list, rky_list)

plt.figure(figsize=(6, 6)) #actually plotting 
plt.plot(rkt_list, rk_energy, color='pink', label='RK Method')
plt.plot(lpft_list, lpf_energy, color='yellow', label='Leapfrog method')
plt.xlabel('time')
plt.ylabel('energy')
plt.legend()
plt.show()
