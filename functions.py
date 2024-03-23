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
