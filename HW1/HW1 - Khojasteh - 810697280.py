# -*- coding: utf-8 -*-
"""
Created on Thu Apr  6 21:17:11 2023

@author: Auspicious
"""

import numpy as np
import scipy

from scipy.optimize import minimize
from scipy.optimize import NonlinearConstraint
from scipy.optimize import BFGS

L = 2100
pi = 3.141592653589793
ro = 7800*(10^-9)

def f(x):
    return [pi*L*ro*[(x[0]/2)^2 - (x[1]/2)^2]]

from scipy.optimize import Bounds            
bounds = Bounds([0,0], [np.inf,np.inf])

from scipy.optimize import LinearConstraint
linear_constraint = LinearConstraint([1,-1],-np.inf, 1)

def con_f(x):
    return [1289692.1869 - x[0]^4 + x[1]^4, 11697.8883*x[0] - x[0]^4 + x[1]^4]

nonlinear_constraint = NonlinearConstraint(cons_f, -np.inf, -10, jac='2-point', hess=BFGS())

x0 = np.array([0.4,2.5])
res = minimize(f, x0, method='trust_constr', jac='2-point', hess=BFGS(),
               constraints=[linear_constraint, nonlinear_constraint],
               options={'verbose:1'}, bounds=bounds)

print(res.x)
