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

