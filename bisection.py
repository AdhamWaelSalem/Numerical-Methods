from sympy import *


def bisection(f, xu, xl, N, xl_list, xu_list, f_xl_list, f_xu_list, xr_list, f_xr_list, tolerance):
    if f(xu) * f(xl) >= 0:
        return None  # bisection can not be used to get the root

    xu_n = xu  # xu_n is a temporary variable use to store new value of x upper
    xl_n = xl  # xl_n is a temporary variable use to store new value of x lower

    for n in range(1, N + 1):
        xu_list.append(xu_n)  # adding new value of x upper to its list
        f_xu_n = f(xu_n)  # calculating f(x upper)
        f_xu_list.append(f_xu_n)  # adding new value of f(x upper) in its list

        xl_list.append(xl_n)  # adding new value of x lower to its list
        f_xl_n = f(xl_n)  # calculating f(x lower)
        f_xl_list.append(f_xl_n)  # adding new value of f(x lower) in its list

        xr_n = (xu_n + xl_n) / 2  # calculating xr new value
        xr_list.append(xr_n)  # adding xr to its list
        f_xr_n = f(xr_n)  # calculating f(xr)
        f_xr_list.append(f_xr_n)  # adding f(xr) in its list

        if f_xu_n * f_xr_n < 0:  # if true : the value of x lower will be equal xr
            xu_n = xu_n
            xl_n = xr_n
        elif f_xl_n * f_xr_n < 0:  # if true : the value of x upper will be equal xr
            xu_n = xr_n
            xl_n = xl_n
        elif f_xr_n == 0 or xr_n - xr_list[-1] <= tolerance:  # exit condition if calculated root is accepted with
            # respect to tolerance or exact solution
            print("Found solution.")
            return n
        else:
            print("Bisection method fails.")
            return None
    return n


def newton_raphson(f, x, N, tolerance, xi_list, xinew_list):
    for n in range(1, N + 1):
        h = f(x) / (Derivative(f, x)).doit()  # calculating second term of newton raphson
        xi_list.append(x)                     # adding xi to its list
        x = x - h                             # calculating xi+1
        xinew_list.append(x)                  # adding xi+1 to its list
        if abs(h) <= tolerance:               # exit condition if root value is accepted with respect to tolerance
            return x
    return x                                  # returning resulted root after maximum  iterations have been done


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')
