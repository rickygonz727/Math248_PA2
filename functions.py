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


def func2(x):
    """This function defines the second component of Lex Luthors Devious Function.
    
    Inputs:
        x (float): An arbitrary value
        
    Returns:
        np.cos(x) - np.exp(-(x**2)) + 1 (float): The second component computed
        
    """
    return np.cos(x) - np.exp(-(x**2)) + 1


def func3(x):
    """This function defines the third component of Lex Luthors Devious Function.
    
    Inputs:
        x (float): An arbitrary value
        
    Returns:
        (x**5) - 9*(x**4) - (x**3) + 17*(x**2) - 8*x - 8 (float): The third component computed
        
    """
    return (x**5) - 9*(x**4) - (x**3) + 17*(x**2) - 8*x - 8


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


def logistic_func(func,a,x1,n):
    """Function to create lists of x-iterates and the number of steps.
    
    Inputs:
        func (function): The function that we are stepping through. 
        a (float): A value within the logistic function that can change
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
        x[k+1] = func(x[k]) #Replaces a value in the x-values list with what is calculated from the logistic function
        steps[k+1] = k+1 #Replaces a value in the steps list from the iterate in the for-loop
    
    calculations = [x,steps] #Creates a list of both the x-values and the steps
    return calculations #Returns the matrix

