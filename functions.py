"""Programming Assignment #2 - Necessary Functions

Authors: Ricky Gonzales, Lauren Wiermanski, Elissa Anderson, James Love Jr, Brett Bono
Version: March 20th, 2024

Approximating Roots to Defeat Lex Luthor
"""


import numpy as np


def func1(x):
    """This function defines the first component of Lex Luthors Devious Function.
    
    Inputs:
        x (float): An arbitrary value
        
    Returns:
        np.exp(2*x -1) - 2*(x**2) - (1/2) (float): The first component computed
        
    """
    return np.exp(2*x -1) - 2*(x**2) - (1/2)


def dfunc1(x):
    """This function defines the derivative of the first component of Lex Luthors Devious Function
    
    Inputs:
        x (float): An arbitrary value
        
    Returns:
        (4*x*(np.exp(2*x-1)) - 4*x - (2*(np.exp(2*x-1)))) (float): The derivative function
    
    """
    return (4*x*(np.exp(2*x-1)) - 4*x - (2*(np.exp(2*x-1))))


def func2(x):
    """This function defines the second component of Lex Luthors Devious Function.
    
    Inputs:
        x (float): An arbitrary value
        
    Returns:
        np.cos(x) - np.exp(-(x**2)) + 1 (float): The second component computed
        
    """
    return np.cos(x) - np.exp(-(x**2)) + 1


def dfunc2(x):
    """This function defines the derivative of the second component of Lex Luthors Devious Function.
    
    Inputs:
        x (float): An arbitraty value
        
    Returns:
        (2*(x**3)*np.exp(-(x**2))) - np.sin(x) (float): The derivative function
        
    """
    return (2*(x**3)*np.exp(-(x**2))) - np.sin(x)


def func3(x):
    """This function defines the third component of Lex Luthors Devious Function.
    
    Inputs:
        x (float): An arbitrary value
        
    Returns:
        (x**5) - 9*(x**4) - (x**3) + 17*(x**2) - 8*x - 8 (float): The third component computed
        
    """
    return (x**5) - 9*(x**4) - (x**3) + 17*(x**2) - 8*x - 8


def dfunc3(x):
    """This function defines the derivative of the third component of Lex Luthors Devious function.
    
    Inpurs:
        x (flaot): An arbitrary value
        
    Returns:
        5*(x**4) - 36*(x**3) - 3*(x**2) + 34*x - 8 (float): The derivative function
    
    """
    return 5*(x**4) - 36*(x**3) - 3*(x**2) + 34*x - 8


def lex_func(a, b, c):
    """This function defines the combination of all of the three functions
    
    Inputs:
        a (float): An arbitrary value
        b (float): An arbitrary value
        c (float): An arbitrary value

        
    Returns:
        a * b * c (float): The combined computation
        
    """
    return a * b * c


def fixed_point_func(func,x1,n):
    """Function to create lists of x-iterates and the number of steps.
    
    Inputs:
        func (function): The function that we are stepping through. 
        x1 (float): The initial condition of the logisitc function
        n (int): The step size for iteration.
        
    Returns:
        calculations (list): A list of two lists, which consists of the list of x-values and a list of steps. 
    
    """
    x = np.zeros(n+1) #Creates zero list for x-values
    steps = np.zeros(n+1) #Creates zero list for steps
    
    x[1] = x1 #Appends the initial condition to the x-list
    steps[1] = 1 #Appends the first step to the steps list
    
    for k in range(1,n): #Begins loop to construct each of the lists
        x[k+1] = func(x[k]) #Replaces a value in the x-values list with what is calculated from the function
        steps[k+1] = k+1 #Replaces a value in the steps list from the iterate in the for-loop
    
    calculations = [x,steps] #Creates a list of both the x-values and the steps
    return calculations #Returns the list


def newtons_method(func, dfunc, xn, limit):
    """This function defines Newtons Method for converging to the root of a function.
    
    Inputs:
        func (function): The function that we are stepping through
        dfunc (function): The functions derivative
        xn (float): Initial x-value
        limit (int): Tolerance number for when Newtons method should stop
        
    Returns:
        x (list): A list of the x-values calculated from stepping through the function.
        
    """
    x = np.zeros(limit+1)
    steps = np.zeros(limit+1)
    
    x[1] = xn
    steps[1] = 1
    
    for i in range(1,limit):
        x[i+1] = x[1] - (func(xn) / dfunc(xn))
        steps[i+1] = i+1
        
    list_calcs = [x.tolist(),steps.tolist()]
    return list_calcs
    