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


def gfunc1(x):
    """This function defines the g(x) function for finding the fixed point of g(x) = x
    
    Inputs:
        x (float): An arbitrary value
        
    Returns:
        (1/2)*(np.log(2*(x**2)) + 1) (float): The g(x) function for func1
        
    """
    return (1/2)*(np.log(2*(x**2)+(1/2)) + 1)


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
    return (2*x*np.exp(-(x**2))) - np.sin(x)


def gfunc2_1(x):
    """This function defines one of the g(x) functions for finding the fixed point of func2. 
        Note: This function works for all x in [-10,10].
        Use this function for the 3.13 root.
        
    Inputs:
        x (flaot): An arbitrary value.
        
    Returns:
        np.arccos(np.exp(-(x**2))-1) (float): One of eight functions for g(x)
    
    """
    return np.arccos(np.exp(-(x**2))-1)


def gfunc2_2(x):
    """This function defines one of the g(x) functions for finding the fixed point of func2. 
        Note: This function works for all x in [-10,10].
        Use this function for the -3.13 root.
        
    Inputs:
        x (flaot): An arbitrary value.
        
    Returns:
        np.arcsin(np.sqrt(1-((np.exp(-(x**2))-1)**2))) (float): One of eight functions for g(x)
        
    """
    return np.arcsin(np.sqrt(1-((np.exp(-(x**2))-1)**2)))


def gfunc2_3(x):
    """This function defines one of the g(x) functions for finding the fixed point of func2. 
        Note: This function works for all x in [-10,0) U (0,10].
        Use this function for the 3pi root
                                                          
    Inputs:
        x (flaot): An arbitrary value.
        
    Returns:
        -(1/x)*np.log((np.sqrt(1-(np.sin(x)**2)))) (float): One of eight functions for g(x)

    """
    return -(1/x)*np.log((np.sqrt(1-(np.sin(x)**2))))


def gfunc2_4(x):
    """This function defines one of the g(x) functions for finding the fixed point of func2. 
        Note: This function works for all x in [-10, -5pi/2) U (-3pi/2, -pi/2) U (pi/2, 3pi/2) U (5pi/2, 10].
        Use this for the 3.15 root. 
                                                          
    Inputs: 
        x (float): An Arbitrary value
        
    Returns:
        np.sqrt(-np.log(np.cos(x)+1)) (float): One of eight functions for g(x)
        
    """
    return np.sqrt(-np.log(np.cos(x)+1))


def gfunc2_5(x):
    """This function defines one of the g(x) functions for finding the fixed point of func2. 
        Warning: This function only works for extremely specific values of x.
        Interval: x in (-9.5,-8.5) U (-6.8, -5.7) U (-3.6, -2.6) U (-0.9, 0.9) U (2.6, 3.6) U (5.7, 6.8) U (8.5, 9.5)
        This function will not be used after careful consideration. 
                                                          
    Inputs: 
        x (float): An Arbitrary value
        
    Returns:
        (1/2)*np.arcsin(2*np.sin(2*x)*(np.exp(-(x**2))-1)) (float): One of eight functions for g(x)
        
    """
    return (1/2)*np.arcsin(2*np.sin(2*x)*(np.exp(-(x**2))-1))


def gfunc2_6(x):
    """This function defines one of the g(x) functions for finding the fixed point of func2. 
        Note: This function works for all x in [-10, -0.8) U (0.8, 10].
        Use this function for the -3.15 root
                                                          
    Inputs: 
        x (float): An Arbitrary value
        
    Returns:
        np.arcsin((np.sin(2*x)/(2*(np.exp(-(x**2))-1)))) (float): One of eight functions for g(x)
        
    """
    return np.arcsin((np.sin(2*x)/(2*(np.exp(-(x**2))-1))))


def gfunc2_7(x):
    """This function defines one of the g(x) functions for finding the fixed point of func2. 
        Note: This function works for all x in [-10, -3.14) U (-3.14, 0) U (0, 3.14) U (3.14, 10].
        This function will not be used after careful consideration.
        
    Inputs: 
        x (float): An Arbitrary value
        
    Returns:
        -(1/x)*(np.log(np.cos(x)+1)) (float): One of eight functions for g(x)
        
    """
    return -(1/x)*(np.log(np.cos(x)+1))


def gfunc2_8(x):
    """This function defines one of the g(x) functions for finding the fixed point of func2. 
        Note: This function works for all x in [-10, -6) U (6, 10].
        Use this function for the -3pi root
                                                          
    Inputs: 
        x (float): An Arbitrary value
        
    Returns:
        np.arccos(np.exp(-(x**2))+1) (float): One of eight functions for g(x)
        
    """
    return np.arccos(np.exp(-(x**2))+1)


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


def gfunc3_1(x):
    """This function defines one of the possible g(x)'s for the third component to Lex's devious function.
        Interval: x between [-1.7, 1.6]
        Use this function to approximate the -0.510 root
        
    Inputs:
        x (float): An arbitrary value
        
    Returns:
        (1/8)*((x**5)-9*(x**4)-(x**3)+17*(x**2)-8) (float): One of the four g(x)'s
        
    """
    return (1/8)*((x**5)-9*(x**4)-(x**3)+17*(x**2)-8)


def gfunc3_2(x):
    """This function defines one of the possible g(x)'s for the third component to Lex's devious function.
        Interval: x between [-3, 8.5]
        Use this function to approximate the -1.38 root
        
    Inputs:
        x (float): An arbitrary value
        
    Returns:
        ((x**5)-9*(x**4)+17*(x**2)-8*x-8)**(1/3) (float): One of the four g(x)'s
        
    """
    return ((x**5)-9*(x**4)+17*(x**2)-8*x-8)**(1/3)


def gfunc3_3(x):
    """This function defines one of the possible g(x)'s for the third component to Lex's devious function.
        Interval: x between [-10, 10]
        Use this function to approximate the 8.91 root
        
    Inputs:
        x (float): An arbitrary value
        
    Returns:
        9*(x**4)+(x**3)-17*(x**2)+8*(x) +8)**(1/5) (float): One of the four g(x)'s
        
    """
    return (9*(x**4)+(x**3)-17*(x**2)+8*(x) +8)**(1/5)


def gfunc3_4(x):
    """This function defines one of the possible g(x)'s for the third component to Lex's devious function.
        Interval: x between (-2.79, -0.486] U [0.963, 9.778]
        This function will not be used after careful consideration. 
        
    Inputs:
        x (float): An arbitrary value
        
    Returns:
        ((1/9)*((x**5)-(x**3)+17*(x**2)-8*x-8))**(1/4) (float): One of the four g(x)'s
        
    """
    return ((1/9)*((x**5)-(x**3)+17*(x**2)-8*x-8))**(1/4)


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
    
    calculations = [x.tolist(),steps.tolist()] #Creates a list of both the x-values and the steps
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
        x[i+1] = x[i] - (func(x[i]) / dfunc(x[i]))
        steps[i+1] = i+1
        
    list_calcs = [x.tolist(),steps.tolist()]
    return list_calcs


def bisection_method():
    return
