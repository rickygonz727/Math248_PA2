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
    """This function defines a g(x) function for finding the fixed point of g(x) = x
        This function has been tested as a valid fixed point algorithm.  
    
    Inputs:
        x (float): An arbitrary value
        
    Returns:
        (1/2)*(np.log(2*(x**2)) + 1) (float): One of three functions for g(x)
        
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
    """This function defines a g(x) function that works for iterating through function #2.
        This can only work for the roots more near the origin.
        
    Inputs:
        x (float): An arbitrary value
        
    Returns:
        np.arccos(np.exp(-(x**2))-1) (float): One of 6 g(x) functions.
        
    """
    return np.arccos(np.exp(-(x**2))-1)


def gfunc2_2(x):
    """This function defines a g(x) function that works for iterating through function #2.
        This can work for any of the roots. 
        
    Inputs:
        x (float): An arbitrary value
        
    Returns:
        np.arcsin((np.sin(2*x)/(2*(np.exp(-(x**2))+1)))) (float): One of 6 g(x) functions.
        
    """
    return np.arcsin((np.sin(2*x)/(2*(np.exp(-(x**2))+1))))


def gfunc2_3(x):
    """This function defines a g(x) function that works for iterating through function #2.
        This can only work for +3.15 and +3pi. 
        x in [4.6, 3.14] U [3pi, 10]
        
    Inputs:
        x (float): An arbitrary value
        
    Returns:
        np.sqrt(np.log(1-((np.exp(x**2)*np.cos(x))))) (float): One of 6 g(x) functions.
        
    """
    return np.sqrt(np.log(1-(np.exp(x**2)*np.cos(x))))


def gfunc2_4(x):
    """This function defines a g(x) function that works for iterating through function #2.
        This can only work for -3.15, -3pi, +3.15, and +3pi
        x in [-10,-3pi] U [-4.6, -3.14] U [3.14,4.6] U [3pi, 10]
        
    Inputs:
        x (float): An arbitrary value
        
    Returns:
        (1/x)*np.log(1-(np.exp(x**2)*np.cos(x))) (float): One of 6 g(x) functions.
        
    """
    return (1/x)*np.log(1-(np.exp(x**2)*np.cos(x)))


def gfunc2_5(x):
    """This function defines a g(x) function that works for iterating through function #2.
        This can only work for +3.13 and +3pi.
        x in [1.7,3.14] U [7.8, 3pi]
        
    Inputs:
        x (float): An arbitrary value
        
    Returns:
        np.sqrt(np.log((1-np.exp(x**2))/np.cos(x))) (float): One of 6 g(x) functions.
        
    """
    return np.sqrt(np.log((1-np.exp(x**2))/np.cos(x)))


def gfunc2_6(x):
    """This function defines a g(x) function that works for iterating through function #2.
        This can only work for +/- 3.13 and +/- 3pi.
        x in [-3pi, -7.9] U [-3.14, -1.8] U [1.8, 3.14] U [7.9, 3pi]
        
    Inputs:
        x (float): An arbitrary value
        
    Returns:
        (1/x)*np.log((1-np.exp(x^2))/np.cos(x)) (float): One of 6 g(x) functions.
        
    """
    return (1/x)*np.log((1-np.exp(x**2))/np.cos(x))


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
        Interval: x between [-3, 8.5]
        
    Inputs:
        x (float): An arbitrary value
        
    Returns:
        ((x**5)-9*(x**4)+17*(x**2)-8*x-8)**(1/3) (float): One of the g(x)'s
        
    """
    return ((x**5)-9*(x**4)+17*(x**2)-8*x-8)**(1/3)


def gfunc3_2(x):
    """This function defines one of the possible g(x)'s for the third component to Lex's devious function.
        Interval: x between [-10, 10]
        
    Inputs:
        x (float): An arbitrary value
        
    Returns:
        9*(x**4)+(x**3)-17*(x**2)+8*(x) +8)**(1/5) (float): One of the g(x)'s
        
    """
    return (9*(x**4)+(x**3)-17*(x**2)+8*(x) +8)**(1/5)


def gfunc3_3(x):
    """This function defines one of the possible g(x)'s for the third component to Lex's devious function.
        Interval: x between (-2.79, -0.486] U [0.963, 9.778]
        
    Inputs:
        x (float): An arbitrary value
        
    Returns:
        ((1/9)*((x**5)-(x**3)+17*(x**2)-8*x-8))**(1/4) (float): One of the g(x)'s
        
    """
    return ((1/9)*((x**5)-(x**3)+17*(x**2)-8*x-8))**(1/4)


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


def plot_fixed_point(x,steps,num):
    """This function plots fixed point methods.
    
    Input:
        x (list): The list of x-values calcualted from the method
        steps (list): The list of steps taken during the method
        num (int): The number of the respective root we're plotting
        
    Returns:
        None
        
    """
    import matplotlib.pyplot as plt
    
    title = "Fixed Point Function Plot for root #" + str(num)
    plt.figure(figsize=(7,5))
    plt.scatter(steps, x)
    plt.title(title)
    plt.xlabel("x-Axis")
    plt.ylabel("Iterations")
    plt.grid()
    plt.show()
    
    
def newtons_method(func,dfunc, x0, tol=10E-14):
    """This function defines Newtons Method for converging to the root of a function.
    
    Inputs:
        func (function): The function that we are stepping through
        dfunc (function): The functions derivative
        x0 (float): Initial x-value
        tol (int): Tolerance number for how accurate we want Newtons Method to be (14 decimal places).
        
    Returns:
        list_calcs (list): A list of the x-values, error, and final k value of the iterations. 
        
    """
    limit = 1000
    x = np.zeros(limit + 1)
    error = np.zeros(limit + 1)
    
    error[1] = 10
    x[1] = x0
    k = 1
    
    while error[k] > tol and k < limit:
        x[k+1] = x[k] - (func(x[k]) / dfunc(x[k]))
        
        k += 1
        error[k] = abs(x[k] - x[k-1])
    
    list_calcs = [x, error, k]
    return list_calcs
    

def bisection_method(func, a, b, tol1=10E-14, tol2=10E-14):
    """This function defines the Bisection Method for converging to the root of a function
    
    Inputs:
        func (Function): The function that we are stepping through
        a (int): First part of interval [a,b]
        b (int): Second part of interval [a,b]
        tol1 (float): The first tolerance number, set to 10E-14
        tol2 (flaot): The second tolerance number to ensure nothing blows up, set to 10E-14
        
    Returns: 
        limit_calcs (list): A list of the c-values and the final iteration value.
        
    """
    limit = 1 + int(np.ceil(np.log((b-a)/tol1)/np.log(2)))
    
    c = np.zeros(limit + 1)
    error = np.zeros(limit + 1)
    
    error[1] = 10
    k = 1
    
    c[1] = (a+b) /2
    fa = func(a)
    fc = func(c[1])
    
    while error[k] > tol1 and k < limit and abs(fc) > tol2:
        if fa*fc < 0:
            b = c[k]
        else:
            a = c[k]
            fa = func(a)
            
        c[k + 1] = (a+b) / 2
        fc = func(c[k + 1])
        error[k + 1] = abs(c[k+1] - c[k])
        k += 1
        
    limit_calcs = [c,k]
    return limit_calcs
