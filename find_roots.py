"""Programming Assignment #2 - Finding Roots

Authors: Ricky Gonzales, Lauren Wiermanski, Elissa Anderson, James Love Jr, Brett Bono
Version: March 20th, 2024

Approximating Roots to Defeat Lex Luthor
"""

import functions as fn
import matplotlib.pyplot as plt


#%%Newtons Method for the three functions

def lex_nm():
    """This function works as the main function for finding roots with Newtons Method.
    
    Inputs:
        None
    
    Returns:
        roots (list): A list of all 10 roots to Lex Luthors Devious Function
        
    """
    roots = [] #This creates an empty list to store the roots
    
    nm1 = fn.newtons_method(fn.func1, fn.dfunc1, 0.5, 5) #This calculates the singular root for the first function
    
    #These next 6 lines of code calculate all 6 roots of the second function that lies between -10 and 10
    #Desmos was used to help pick the initial x-values
    nm2_1 = fn.newtons_method(fn.func2, fn.dfunc2, 3.13, 7) 
    nm2_2 = fn.newtons_method(fn.func2, fn.dfunc2, -3.13, 7)
    nm2_3 = fn.newtons_method(fn.func2, fn.dfunc2, 3.151, 7) 
    nm2_4 = fn.newtons_method(fn.func2, fn.dfunc2, -3.151, 7)
    nm2_5 = fn.newtons_method(fn.func2, fn.dfunc2, 9.4, 25)
    nm2_6 = fn.newtons_method(fn.func2, fn.dfunc2, -9.4, 25)
    
    #The next three lines calculate the three real roots of the third function, also with help from desmos
    nm3_1 = fn.newtons_method(fn.func3, fn.dfunc3, -0.5, 6) 
    nm3_2 = fn.newtons_method(fn.func3, fn.dfunc3, -1.5, 10) 
    nm3_3 = fn.newtons_method(fn.func3, fn.dfunc3, 9, 6) 
    
    #This next chunk of code assigns variables to the x-value lists from the Newtons Method iterations
    func1_nm_x1 = nm1[0]
    func2_nm_x1 = nm2_1[0]
    func2_nm_x2 = nm2_2[0]
    func2_nm_x3 = nm2_3[0]
    func2_nm_x4 = nm2_4[0]
    func2_nm_x5 = nm2_5[0]
    func2_nm_x6 = nm2_6[0]
    func3_nm_x1 = nm3_1[0]
    func3_nm_x2 = nm3_2[0]
    func3_nm_x3 = nm3_3[0]
    
    #After the x-values list variable were assigned for all 10 roots, we then obtain the actual root by appending the final
    #value of the x-values function and appending it to our empty roots list
    func_nm_x1 = func1_nm_x1[-1]
    roots.append(func_nm_x1)
    func_nm_x2 = func2_nm_x1[-1]
    roots.append(func_nm_x2)
    func_nm_x3 = func2_nm_x2[-1]
    roots.append(func_nm_x3)
    func_nm_x4 = func2_nm_x3[-1]
    roots.append(func_nm_x4)
    func_nm_x5 = func2_nm_x4[-1]
    roots.append(func_nm_x5)
    func_nm_x6 = func2_nm_x5[-1]
    roots.append(func_nm_x6)
    func_nm_x7 = func2_nm_x6[-1]
    roots.append(func_nm_x7)
    func_nm_x8 = func3_nm_x1[-1]
    roots.append(func_nm_x8)
    func_nm_x9 = func3_nm_x2[-1]
    roots.append(func_nm_x9)
    func_nm_x10 = func3_nm_x3[-1]
    roots.append(func_nm_x10)
    
    roots.sort()
    #After all of the values are appended, we then print to the user all 10 roots as well as the degree of accuracy, which
    #thanks to Newtons Method, is extremely high
    print(f"\nThe roots of Lex Luthors Function are: \n\n{func_nm_x1}\n{func_nm_x2}\n{func_nm_x3}")
    print(f"{func_nm_x4}\n{func_nm_x5}\n{func_nm_x6}\n{func_nm_x7}\n{func_nm_x8}\n{func_nm_x9}\n{func_nm_x10}\n")
    print("With 14-15 decimal places of accuracy.")
    
    #We then return the list from the function call
    return roots


#%% Fixed point method for the First function





#%% Fixed Point method for the second function
"""
This part of the code needs to be reconsidered, forgot that there should be the g(x) = x part in order to do this stepping process
Since this is function 2, that means theres two options for what we can do

Either g(x) = np.sqrt(-np.log(np.cos(x) + 1))
or
g(x) = np.arccos(np.exp(-(x**2)) - 1)

which would give g(x) = x to find the root of the second function

So a new function, func2_fp, needs to be defined in the functions.py file

I tested the functions in maxima and option two is the one that works with the conditions for a fixed point algorithm
So, g(x) = np.arccos(np.exp(-(x**2)) - 1)


func2_fp_lists = fn.fixed_point_func1(fn.func2, 1, 35)

func2_fp_x = func2_fp_lists[0]
func2_fp_steps = func2_fp_lists[1]

plt.figure(2)
plt.figure(figsize=(7,5))
plt.scatter(func2_fp_steps, func2_fp_x, label='Iterates')
plt.title("Stepping through Function 2")
plt.xlabel("X-Axis")
plt.ylabel("Steps")
plt.legend()
plt.grid()
plt.show()
"""
#%% Fixed Point Method for the third function




#%% Bisection Method for all three functions

