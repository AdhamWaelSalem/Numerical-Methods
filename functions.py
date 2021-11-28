import sympy
from sympy import *
from numpy import sin, cos, tan, cosh, tanh, sinh
from math import e


def calc(f, value):
    x = value
    return eval(f)


def bisection(f, xu, xl, iterations, xl_list, xu_list, f_xl_list, f_xu_list, xr_list, f_xr_list, tolerance):
    c = 0

    if calc(f, xu) * calc(f, xl) >= 0:
        return None  # bisection can not be used to get the root

    xu_n = xu  # xu_n is a temporary variable use to store new value of x upper
    xl_n = xl  # xl_n is a temporary variable use to store new value of x lower

    for n in range(1, iterations + 1):
        xu_list.append(xu_n)  # adding new value of x upper to its list
        f_xu_n = calc(f, xu_n)  # calculating f(x upper)
        f_xu_list.append(f_xu_n)  # adding new value of f(x upper) in its list

        xl_list.append(xl_n)  # adding new value of x lower to its list
        f_xl_n = calc(f, xl_n)  # calculating f(x lower)
        f_xl_list.append(f_xl_n)  # adding new value of f(x lower) in its list

        xr_n = (xu_n + xl_n) / 2  # calculating xr new value

        f_xr_n = calc(f, xr_n)  # calculating f(xr)
        f_xr_list.append(f_xr_n)  # adding f(xr) in its list

        if f_xu_n * f_xr_n < 0:  # if true : the value of x lower will be equal xr
            xu_n = xu_n
            xl_n = xr_n
        elif f_xl_n * f_xr_n < 0:  # if true : the value of x upper will be equal xr
            xu_n = xr_n
            xl_n = xl_n
        if c == 1 and (
                f_xr_n == 0 or abs(
            (xr_n - xr_list[-1]) / xr_n) <= tolerance):  # exit condition if calculated root is accepted with
            # respect to tolerance or exact solution
            xr_list.append(xr_n)  # adding xr to its list
            return xr_list[-1]
        xr_list.append(xr_n)  # adding xr to its list
        c = 1
    return xr_list[-1]


def newton_raphson(f, xv, iterations, tolerance, xi_list, xinew_list):
    x = sympy.Symbol('x')
    for n in range(1, iterations + 1):
        h = calc(f, xv) / calc(sympy.diff(f, x), xv)  # calculating second term of newton raphson
        xi_list.append(xv)  # adding xi to its list
        x = x - h  # calculating xi+1
        xinew_list.append(xv)  # adding xi+1 to its list
        if abs(h) <= tolerance:  # exit condition if root value is accepted with respect to tolerance
            return xv
    return xv  # returning resulted root after maximum  iterations have been done
