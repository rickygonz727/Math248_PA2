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
        roots (list): A sorted list of all 10 roots from smallest to largest to Lex Luthors Devious Function
        
    """
    roots = [] #This creates an empty list to store the roots
    
    nm1 = fn.newtons_method(fn.func1, fn.dfunc1, 0.5, 5) #This calculates the singular root for the first function
    
    #These next 6 lines of code calculate all 6 roots of the second function that lies between -10 and 10
    #Desmos was used to help pick the initial x-values
    nm2_1 = fn.newtons_method(fn.func2, fn.dfunc2, 3, 15) 
    nm2_2 = fn.newtons_method(fn.func2, fn.dfunc2, -3, 15)
    nm2_3 = fn.newtons_method(fn.func2, fn.dfunc2, 3.2, 15) 
    nm2_4 = fn.newtons_method(fn.func2, fn.dfunc2, -3.2, 15)
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

func1_fpm = fn.fixed_point_func(fn.gfunc1, -0.5, 7)

func1_fp_x = func1_fpm[0]


#%% Fixed Point method for the second function

func2_fpm_1 = fn.fixed_point_func(fn.gfunc2_1, 3, 50)
func2_fpm_2 = fn.fixed_point_func(fn.gfunc2_2, -3, 50) #Fix
func2_fpm_3 = fn.fixed_point_func(fn.gfunc2_3, 9.4, 50) #Fix
func2_fpm_4 = fn.fixed_point_func(fn.gfunc2_4, 3.2, 50) #Find a different function for +3.15
func2_fpm_5 = fn.fixed_point_func(fn.gfunc2_6, -3.2, 50) #Reconsider
func2_fpm_6 = fn.fixed_point_func(fn.gfunc2_8, -9.4, 50) #Reconsider

func2_fp_x1 = func2_fpm_1[0]
func2_fp_x2 = func2_fpm_2[0]
func2_fp_x3 = func2_fpm_3[0]
func2_fp_x4 = func2_fpm_4[0]
func2_fp_x5 = func2_fpm_5[0]
func2_fp_x6 = func2_fpm_6[0]


#%% Fixed Point Method for the third function

func3_fpm_1 = fn.fixed_point_func(fn.gfunc3_1, -0.5, 50) #Fix
func3_fpm_2 = fn.fixed_point_func(fn.gfunc3_2, -1.38, 50) #Reconsider
func3_fpm_3 = fn.fixed_point_func(fn.gfunc3_3, 8.5, 50) 

func3_fp_x1 = func3_fpm_1[0]
func3_fp_x2 = func3_fpm_1[0]
func3_fp_x3 = func3_fpm_3[0]


#%% Bisection Method for all three functions

