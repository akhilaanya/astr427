#Problem 1a

count = 0 #The initial iteration


epsilon = float(2.0**(count)) #F.P. representation omitting mantissa
diff = 1.0 - epsilon 

while diff != 1.0: #not sufficiently small epsilon
    try: 
        epsilon_before = epsilon
        count = count + 1 #redo iteration with a smaller epsilon (goes as 1/2**count, see above)
    
        epsilon = float(1.0/(2.0**(count))) #because you want epsilon to get smaller 
        diff = 1.0 - epsilon #calculates difference again

    except OverflowError:
        break

print("Here's the smallest epsilon s.t. result - epsilon is not ≠ 1.0!")
print(epsilon_before)


#Problem 1b - pretty much the same code just replace - with +
count = 0 #The initial iteration


epsilon = float(2.0**(count)) #F.P. representation omitting mantissa
sumtotal = 1.0 + epsilon 

while sumtotal != 1.0: #not sufficiently small epsilon
    try: 
        pre_epsilon = epsilon
        count = count + 1 #redo iteration with a smaller epsilon (goes as 1/2**count, see above)
    
        epsilon = float(1.0/(2.0**(count))) #because you want epsilon to get smaller 
        sumtotal = 1.0 + epsilon #calculates difference again

    except OverflowError:
        break

print("Here's the smallest epsilon s.t. result + epsilon is not ≠ 1.0!")
print(pre_epsilon)

#Problem 1c
count = 0

first_num = float(2.0**(count))

while first_num != float('inf'): #not close to infinity
    try: 
        numberminus1 = first_num #same logic as 1a/1b
        count = count + 1

        first_num = float(2.0**(count)) #because you want the number to get bigger (no 1/(2.0**(count)) )

    except OverflowError:
        break

print("Here's the maximum representable number!")
print(first_num)

#Problem 1d - same logic as 1c, just make the number exponentially smaller (include 1.0/(2.0**(count)) )
count = 0

first_num = float(1.0/(2.00**(count)))
while first_num != 0.0:
    try: 
        numberminus1 = first_num
        count = count + 1

        first_num = float(1.0/(2.00**(count)))

    except OverflowError:
        break

print("Here's the minimum representable positive number!")
print(first_num)

#Problem 2a
import numpy as np

class AkhilasArray: #Defining a method that will sum the array using np.float32 operation np.sum
    def __init__(self, data):
        self.array = np.array(data, dtype = np.float32)

    def sum_array(self):
        return np.sum(self.array, dtype = np.float32)

my_array = np.random.rand(20000000).astype(np.float32) #defining the array as float32 with 20 million elements

added_array = AkhilasArray(my_array) #calling the method on my array
total = added_array.sum_array() #finding the sum using the above function on my array
print("Here is the sum in the order produced by np.random.rand()!")
print(total)

#Problem 2b - the same method is used so I didn't define it again 
smallest_largest = np.sort(my_array) #default is smallest --> largest
array2 = AkhilasArray(smallest_largest) #called the method on my smallest to largest array
total2 = array2.sum_array() #summing the smallest--> largest array in the same manner as 2a)
print("Here is the sum after sorting from smallest to largest!")
print(total2)

#Problem 2c - also same method
largest_smallest = np.sort(my_array)[::-1] #now it's in descending largest --> smallest
array3 = AkhilasArray(largest_smallest)
total3 = array3.sum_array()
print("Here's the sum largest --> Smallest!")
print(total3)

#Problem 3
import matplotlib.pyplot as plt

x = np.linspace(1e-50, 1e-7, 50)
y = (1 - np.cos(x))/(x**2)
plt.plot(x,y)
plt.show()

#Problem 4a

def lin_interpolate(datafile, somepoint):
    data = np.loadtxt(datafile, delimiter = ',')
    x_data = data[:,0]
    y_data = data[:,1]

    x_diff = x_data[1] - x_data[0]

    floorx_diff = int(somepoint - x_data[0] // x_diff)

    x0, x1 = x_data[floorx_diff], x_data[floorx_diff + 1]
    y0, y1 = y_data[floorx_diff], y_data[floorx_diff + 1]

    y_interpol = y0 + ((somepoint - x0) * (y1 - y0)) / x_diff

    print(y_interpol)
    

#Problem 4b

point = 4.75
interpolate = lin_interpolate("427hw1_data.csv", point)
print("Here is the interpolation!")
print(interpolate)

#Problem 4c

