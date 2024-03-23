"""Programming Assignment #2 - Finding Roots

Authors: Ricky Gonzales, Lauren Wiermanski, Elissa Anderson, James Love Jr, Brett Bono
Version: March 20th, 2024

Approximating Roots to Defeat Lex Luthor
"""

import numpy as np
import matplotlib.pyplot as plt
import functions as fn

#Newtons Method for All three functions

func1_nm_lists = fn.newtons_method(fn.func1, fn.dfunc2, 1, 5)
func2_nm_lists = fn.newtons_method(fn.func2, fn.dfunc2, 1, 5)
func3_nm_lists = fn.newtons_method(fn.func3, fn.dfunc3, 1, 5)

func1_nm_x = func1_nm_lists[0]
func2_nm_x = func2_nm_lists[0]
func3_nm_x = func3_nm_lists[0]

func1_nm_steps = func1_nm_lists[1]
func2_nm_steps = func2_nm_lists[1]
func3_nm_steps = func3_nm_lists[1]

plt.figure(1)
plt.scatter(func1_nm_x, func1_nm_steps, label='Steps')
plt.xlabel("X-Axis")
plt.ylabel("Steps")
plt.title("Newtons Method for the First Component")
plt.legend()
plt.grid()
plt.show()

plt.figure(2)
plt.scatter(func2_nm_x, func2_nm_steps, label='Steps')
plt.xlabel("X-Axis")
plt.ylabel("Steps")
plt.title("Newtons Method for the Second Component")
plt.legend()
plt.grid()
plt.show()

plt.figure(3)
plt.scatter(func3_nm_x, func3_nm_steps, label='Steps')
plt.xlabel("X-Axis")
plt.ylabel("Steps")
plt.title("Newtons Method for the Third Component")
plt.legend()
plt.grid()
plt.show()