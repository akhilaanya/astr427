#Code snippets
#Random pieces of code I want to temporarily delete but still have 
def harmonic_oscillator(t, ylist, i):
    x = ylist[0] #Zeroth derivative w.r.t. time is position
    dx_dt = ylist[1] #1st derivative w.r.t. time is velocity
    d2x_dt2 = -x
    return -x
    
euler_integral = euler_method(50.0, 2.0, harmonic_oscillator, h=3)
print(f"Final position: {euler_integral[0]:.2f}")
print(f"Final velocity: {euler_integral[1]:.2f}")

my_t = [0, h]
y_solution = solution.y.reshape(2) #array of length 2 
y_solution = runge_kutta(my_t, y_solution)

print(y_solution)

def vel(v):
    return v

def acc(x):
    return -x 
        
solution = leapfrog(vel, acc, 50, 50, 3)
print(solution)

h = 3 #fixed time step 
def deriv_rk(t, y):
    try: 
        dy_dt = np.array([0.0, 0.0]) #Create an array (and initialize to 0)
        dy0_dt = y[1] #first derivative 
        dy1_dt = -y[0] #second derivative
        return [dy0_dt, dy1_dt] #grabs your coupled DEs

    except Exception as e:
        print("Something went wrong. Try again.")

def runge_kutta(tlist, y):
    try: 
        t0 = tlist[0]
        y_next = y[i + 1]
        y_now = y[i]

        tlist[i + 1] = t_next
        tlist[i] = t_now 
        for i in range(len(y) - 1): #grabs each index in y except the first one (?)
            dy_dt = (y_next - y_now)/(t_next - t_now)
            return dy_dt #calculates derivative

    except Exception as e:
        print("Something went wrong. try again.")

solution = integrate.RK45(deriv_rk, 0, [0.5, 12350], 2000, max_step = np.inf, rtol = 1.0,
                          atol = 1e6, vectorized = False,first_step = h)
#I ignored the **extraneous part because it was giving an error

k_now = klist[i]
            k_next = klist[i+1]
        
            k_now = deriv_rk(t, y_now)
            k_next = deriv_rk(t + 0.5*step, y_now + 0.5*k_now*step)
            klist = np.append(klist, k_next, axis = 0)

        y_next = y_now + (step/6) +  
            t = t + step
            
            y_next = y_now + step/6 * (k1 + 2*k2 + 2*k3 + k4)
            ylist = np.append(ylist, y_next, axis = 0)


def der_orbit(t, vector):
    try:
        x, y, v_x, v_y = vector
        potential = -(1 + x**2 + y**2)**(-0.5)
        
   
        denom = (1.0 + x**2 + y**2)**(1.5)
        
        gradient_potential = np.array([vx, vy, -x/denom, -y/denom])
            return gradient_potential
    except Exception as e:
        print("Error somewhere, sorry", e)
