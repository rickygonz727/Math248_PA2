"""Programming Assignment #2 - Finding Roots

Authors: Ricky Gonzales, Lauren Wiermanski, Elissa Anderson, James Love Jr, Brett Bono
Version: March 20th, 2024

Approximating Roots to Defeat Lex Luthor
"""

import functions as fn
import matplotlib.pyplot as plt


#%%Newtons Method for the three functions

nm1 = fn.newtons_method(fn.func1, fn.dfunc2, 1, 5)
nm2 = fn.newtons_method(fn.func2, fn.dfunc2, 3, 5)
nm3 = fn.newtons_method(fn.func3, fn.dfunc3, 4, 5)

func1_nm_x = nm1[0]
func2_nm_x = nm2[0]
func3_nm_x = nm3[0]

func1_nm_steps = nm1[1]
func2_nm_steps = nm2[1]
func3_nm_steps = nm3[1]


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
"""

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

#%% Fixed Point Method for the third function




#%% Bisection Method for all three functions

