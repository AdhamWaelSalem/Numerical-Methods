import sympy
from sympy import *
from numpy import sin, cos, tan, cosh, tanh, sinh
from math import e
import matplotlib.pyplot as plt


def graph(f, root):
    f_xr = [calc(f, root)]
    xr = [root]
    x1 = []
    y1 = []
    y3 = []
    for n in range(-30, 30):
        x1.append(n)
        y1.append(calc(f, n))
        y3.append(int(0))

    plt.plot(x1, y1)
    plt.plot(x1, y3)
    plt.plot(xr[-1], f_xr[-1], 'r*')
    plt.xlabel('x - axis')
    plt.ylabel('y - axis')
    plt.title('Graph')
    plt.show()


def diff_f_at_point(f):
    f_dash = diff(f, symbols('x'))
    return f_dash.__str__()


def calc(f, value):
    x = float(value)
    return eval(f)


def bisection(f, xu, xl, iterations, tolerance):
    xl_list = []
    f_xl_list = []
    xu_list = []
    f_xu_list = []
    xr_list = []
    f_xr_list = []
    error_list = [None]
    message = ""
    n = 1
    # Validations
    if calc(f, xu) * calc(f, xl) > 0:  # not valid interval
        message = f"Bisection Method will fail to solve \nfor a root in this interval [{xl}, {xu}]"
    elif calc(f, xl) == 0:  # xl is root
        message = f"Xl : {xl} is the root"
    elif calc(f, xu) == 0:  # xu is root
        message = f"Xu : {xu} is the root"
    else:
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
            xr_list.append(xr_n)  # adding xr to its list
            if n > 1:
                error_list.append(abs((xr_list[-1] - xr_list[-2]) / xr_list[-1]))
                if error_list[-1] <= tolerance:
                    break
            if f_xr_n == 0:
                break
    data = {'Xu': xu_list, 'Xl': xl_list, 'Xr': xr_list, 'f(Xu)': f_xu_list, 'f(Xl)': f_xl_list, 'f(Xr)': f_xr_list,
            'Error': error_list}
    return data, n, xr_list, error_list, message


def newton_raphson(f, xi, iterations, tolerance):
    from sympy import Symbol, Derivative
    error = []
    xi_list = []
    xinew_list = []
    message = ""
    n = 1
    der = diff_f_at_point(f)
    conv = calc(der, xi)
    if abs(conv) == 0:
        message = f"Newton Raphson Method with f(x) = {f} and \nXi : {xi} will fail as it will diverge from root"
    else:
        for n in range(1, iterations + 1):
            fx = calc(f, xi)
            dfx = calc(der, xi)
            h = fx / dfx  # calculating second term of newton raphson equation
            temp = xi
            xi = xi - h  # calculating xi+1
            error.append(abs(h / xi))
            xi_list.append(temp)  # adding xi to its list
            xinew_list.append(xi)  # adding xi+1 to its list
            if error[-1] <= tolerance:  # exit condition if root value is accepted with respect to tolerance
                break
    data = {'Xi': xi_list, 'Xi+1': xinew_list, 'Error': error}
    return data, n, xinew_list, error, message  # return table
