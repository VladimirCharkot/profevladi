# -*- coding: utf-8 -*-
"""
Created on Mon Dec 11 00:31:36 2017

@author: usuario
"""

def param_test(the_arg_f, arg):
    if not type(the_arg_f) == type(lambda x: x):
        f = lambda x: the_arg_f
    else:
        f = the_arg_f
    return f(arg)

# supongamos que arg va de 0 a 10
def comp(x):
    return param_test(lambda d: d/10, x)