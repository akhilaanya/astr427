#Problem 1a

count = 0 #The initial iteration

import numpy as np
import sys

epsilon = np.float32(2.0**(count)) #Floating point representation
diff = 1.0 - epsilon 

while diff != 1.0: #not a sufficiently small epsilon
    try: 
        epsilon_before = epsilon
        count = count + 1
        #redo iteration with a smaller epsilon (goes as 1/2**count, see above)
    
        epsilon = np.float32(1.0/(2.0**(count))) #because you want epsilon to get smaller
        diff = 1.0 - epsilon #calculates difference again

    except Exception as e: #Handles all possible value errors, type errors, etc. 
        break

print(f"Here's the smallest epsilon s.t. result - epsilon is not ≠ 1.0!: {epsilon_before}")

#Problem 1b - pretty much the same code just replace - with +
count = 0 #The initial iteration


epsilon = np.float32(2.0**(count)) #F.P. representation omitting mantissa
sumtotal = 1.0 + epsilon 

while sumtotal != 1.0: #not sufficiently small epsilon
    try: 
        pre_epsilon = epsilon
        count = count + 1 #redo iteration with a smaller epsilon (goes as 1/2**count, see above)
    
        epsilon = np.float32(1.0/(2.0**(count))) #because you want epsilon to get smaller 
        sumtotal = 1.0 + epsilon #calculates difference again

    except Exception as e:
        break

print(f"Here's the smallest epsilon s.t. result + epsilon is not ≠ 1.0!: {pre_epsilon}")

#Problem 1c
count = 0

number1 = np.float64(2.0**(count))

while number1 != float('inf'): #not close to infinity
    try: 
        numberminus1 = number1 #same logic as 1a/1b
        count = count + 1

        number1 = np.float64(2.0**(count)) #because you want the number to get bigger (no 1/(2.0**(count)) )

    except Exception as e:
        break

#And to find mantissa... you know it is 1.f so it can be between 1.0-2.0, so max is 2.0, same logic as 1a
mantissa = 2.0 - (2 * epsilon_before) #Spacing doubles (delta explanation from class)

maxnum = number1 * mantissa #floating point representation

print(f"Here's the maximum representable number!: {maxnum}")


#Problem 1d - same logic as 1c, just make the number exponentially smaller (include 1.0/(2.0**(count)) )
count = 0

first_num = np.float64(1.0)

while first_num / 2.0 > 0.0:
    try: 
        numberminus1 = first_num
        count = count + 1

        first_num = np.float64(first_num / 2.0)

    except Exception as e:
        print("underflow error")
        break

print(f"Here's the minimum representable positive (subnormal) number!: {first_num}")

#10 percent errors for 1a-1d - use sys.float_info() to get the hard-coded actual machine numbers
actual_epsilon = sys.float_info.epsilon
actual_subnormal = sys.float_info.min * sys.float_info.epsilon 
actual_max = sys.float_info.max 

minsub_epsilon = abs(pre_epsilon - actual_epsilon) / actual_epsilon * 100 #just calculating error
minadd_epsilon = abs(epsilon_before - actual_epsilon) / 2 * actual_epsilon * 100 #because this epsilon is double that of 1a
subnormal_error = abs(first_num - actual_subnormal) / actual_subnormal * 100
max_error = abs(maxnum - actual_max) / actual_max * 100 

print(f"Epsilon 1a error is {minsub_epsilon:.1f} percent")
print(f"Epsilon 1b error is {minadd_epsilon:.1f} percent")
print(f"Subnormal error is {subnormal_error:.1f} percent")
print(f"maximum number error is {max_error:.1f} percent")


#Problem 2a
import numpy as np

'''class AkhilasArray: #Defining a method that will sum the array using np.float32 operation np.sum
    def __init__(self, data):
        self.array = np.array(data, dtype = np.float32)'''

my_array = np.random.rand(20000000).astype(np.float32) #defining the array as float32 with 20 million elements

def sum_array(my_array):
    total = 0
    for element in my_array:
        total += element

    return total

added_array = sum_array(my_array) #finding the sum using the above function on my array
print("Here is the sum in the order produced by np.random.rand()!:", added_array)

#Problem 2b - the same method is used so I didn't define it again 
smallest_largest = np.sort(my_array) #default is smallest --> largest
array2 = sum_array(smallest_largest) #summing the smallest--> largest array in the same manner as 2a)
print("Here is the sum after sorting from smallest to largest!", array2)

#Problem 2c - also same method
largest_smallest = np.sort(my_array)[::-1] #now it's in descending largest --> smallest
array3 = sum_array(largest_smallest)
print("Here's the sum largest --> Smallest!", array3)


np_array = np.ndarray.sum(my_array)
print("The numpy way for the standard random array produces a summation of", np_array)

np_array2 = np.ndarray.sum(smallest_largest)
print("The numpy way for the smallest--> largest random array produces a summation of", np_array2)

np_array3 = np.ndarray.sum(largest_smallest)
print("The numpy way for the standard random array produces a summation of", np_array3)

#Problem 3
#Numerically, lim_x-->0[(1 - cos(x))/(x**2)] = 1/2 using L'Hopital's rule 
import matplotlib.pyplot as plt

x = np.linspace(1e-14, 1e-6, 1000)
plt.xscale('log')
y = (1 - np.cos(x))/(x**2)
plt.plot(x,y)
plt.show()

#Problem 4a

def lin_interpolate(datafile, somepoint):
    data = np.loadtxt(datafile, delimiter = ',', skiprows = 1)
    x_data = data[:,0] #grabbing the rows
    y_data = data[:,1]

    x_diff = x_data[1] - x_data[0]

    floorx_diff = int((somepoint - x_data[0]) // x_diff) #removes any decimal places to get the difference as an integer index to pass into the x0, x1 = x_data[] line

    floorx_diff = max(0, min(floorx_diff, len(x_data) - 4)) #keeps the index in a boundary only across the length of the array

    x0, x1 = x_data[floorx_diff], x_data[floorx_diff + 1] #defining the x, y points
    y0, y1 = y_data[floorx_diff], y_data[floorx_diff + 1]

    linear = ((somepoint - x0) * (y1 - y0)) / x_diff #linear Lagrange interpolation using the equations from class

    y_interpol = y0 + linear

    return y_interpol
    

#Problem 4b

point = 4.75
lin_inter = lin_interpolate("/Users/pisupati/Documents/astr427/427hw1_data.csv", point)
print("Here is the linear interpolation!", lin_inter)

#Problem 4c
def quad_interpolate(datafile, somepoint): #same logic as 4a except you now have 3 parameters 
    data = np.loadtxt(datafile, delimiter = ',', skiprows = 1)
    x_data = data[:,0]
    y_data = data[:,1]

    x_diff = x_data[1] - x_data[0]

    floorx_diff = int((somepoint - x_data[0]) // x_diff)

    floorx_diff = max(0, min(floorx_diff, len(x_data) - 4))

    x0, x1, x2 = x_data[floorx_diff], x_data[floorx_diff + 1], x_data[floorx_diff + 2]
    y0, y1, y2 = y_data[floorx_diff], y_data[floorx_diff + 1], y_data[floorx_diff + 2]

    
    quad0 = ((somepoint - x1) * (somepoint - x2)) / ((x0 - x1) * (x0 - x2))
    quad1 = ((somepoint - x0) * (somepoint - x2)) / ((x1 - x0) * (x1 - x2))
    quad2 = ((somepoint - x0) * (somepoint - x1)) / ((x2 - x0) * (x2 - x1))

    y_interpol = (y0 * quad0) + (y1 * quad1) + (y2 * quad2)

    return y_interpol

def fourth_order(datafile, somepoint): #now you have 5 parameters for a 4th order polynomial (including your constant term)
    data = np.loadtxt(datafile, delimiter = ',', skiprows = 1)
    x_data = data[:,0]
    y_data = data[:,1]

    x_diff = x_data[1] - x_data[0]

    floorx_diff = int((somepoint - x_data[0]) // x_diff)

    floorx_diff = max(0, min(floorx_diff, len(x_data) - 5)) 

    x0, x1, x2, x3, x4 = x_data[floorx_diff], x_data[floorx_diff + 1], x_data[floorx_diff + 2], x_data[floorx_diff + 3], x_data[floorx_diff + 4]
    y0, y1, y2, y3, y4 = y_data[floorx_diff], y_data[floorx_diff + 1], y_data[floorx_diff + 2], y_data[floorx_diff + 3], y_data[floorx_diff + 4]

    four_order0 = ((somepoint - x1) * (somepoint - x2) * (somepoint - x3) * (somepoint - x4)) / ((x0 - x1) * (x0 - x2) * (x0 - x3) * (x0 - x4))
    four_order1 = ((somepoint - x0) * (somepoint - x2) * (somepoint - x3) * (somepoint - x4)) / ((x1 - x0) * (x1 - x2) * (x1 - x3) * (x1 - x4))
    four_order2 = ((somepoint - x0) * (somepoint - x1) * (somepoint - x3) * (somepoint - x4)) / ((x2 - x0) * (x2 - x1) * (x2 - x3) * (x2 - x4))
    four_order3 = ((somepoint - x0) * (somepoint - x1) * (somepoint - x2) * (somepoint - x4)) / ((x3 - x0) * (x3 - x1) * (x3 - x2) * (x3 - x4))
    four_order4 = ((somepoint - x0) * (somepoint - x1) * (somepoint - x2) * (somepoint - x3)) / ((x4 - x0) * (x4 - x1) * (x4 - x2) * (x4 - x3))

    y_interpol = (y0 * four_order0) + (y1 * four_order1) + (y2 * four_order2) + (y3 * four_order3) + (y4 * four_order4)

    return y_interpol
    
x_vals = np.linspace(1, 5, 100)
y_lin = []
y_quad = []
y_fourthorder = []

for x in x_vals:
    lin_vals = lin_interpolate("/Users/pisupati/Documents/astr427/427hw1_data.csv", x)
    y_lin.append(lin_vals)

    quad_vals = quad_interpolate("/Users/pisupati/Documents/astr427/427hw1_data.csv", x)
    y_quad.append(quad_vals)

    fourthorder_vals = fourth_order("/Users/pisupati/Documents/astr427/427hw1_data.csv", x)
    y_fourthorder.append(fourthorder_vals)

point = 4.75

data = np.loadtxt("/Users/pisupati/Documents/astr427/427hw1_data.csv", delimiter = ',', skiprows = 1)

quad_inter = quad_interpolate("/Users/pisupati/Documents/astr427/427hw1_data.csv", point)
print(f"Here is the quadratic interpolation!", quad_inter)

fourthorder_inter = fourth_order("/Users/pisupati/Documents/astr427/427hw1_data.csv", point)
print(f"Here is the 4th order interpolation!", fourthorder_inter)

plt.figure(figsize=(6, 4))
plt.plot(x_vals, y_lin, label='linear', color='orange', linestyle='--', linewidth=2)
plt.title('Linear interpolation')
plt.xlabel('x')
plt.ylabel('y')
plt.show()

plt.figure(figsize=(6, 4))
plt.plot(x_vals, y_quad, label='Quadratic', color='purple', linestyle='-.', linewidth=2)
plt.title('Quadratic interpolation')
plt.xlabel('x')
plt.ylabel('y')
plt.show()

plt.figure(figsize=(6, 4))
plt.plot(x_vals, y_fourthorder, label='4th order', color='green', linestyle='-', linewidth=2)
plt.title('4th Order innterpolation')
plt.xlabel('x')
plt.ylabel('y')
plt.show()

#Problem 4d
y = 100/ ((4.75)**2)
lin_ratio = y / lin_inter
quad_ratio = y / quad_inter
fourthorder_ratio = y/fourthorder_inter
print(f"ratio of function calculation to linear interpolation result: {lin_ratio:.3f}")
print(f"ratio of function calculation to quadratic interpolation result: {quad_ratio:.3f}")
print(f"ratio of function calculation to fourth order interpolation result: {fourthorder_ratio:.3f}")
