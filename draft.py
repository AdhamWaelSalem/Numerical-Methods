import sys

import numpy
import functions


def generateStraightLine(x1, y1, x2, y2):
    m = (y1 - y2) / (x1 - x2)
    c = y1 - m * x1
    return m, c


def falsePosition(fx, xlValue, xuValue, tolerance, iterations):
    xl = [xlValue]
    xu = [xuValue]
    fxl = [functions.calc(fx, xl[-1])]
    fxu = [functions.calc(fx, xu[-1])]
    xr = []
    fxr = []
    error = [None]
    i = 0
    message = ""
    # Validations
    if fxl[-1] * fxu[-1] > 0:  # not valid interval
        message = f"False Position Method will fail to solve \nfor a root in this interval [{xlValue}, {xuValue}]"
    elif fxl[-1] == 0:  # xl is root
        message = f"Xl : {xlValue} is the root"
        xr.append(xl[-1])
        fxr.append(0)
    elif fxu[-1] == 0:  # xu is root
        message = f"Xu : {xuValue} is the root"
        xr.append(xu[-1])
        fxr.append(0)
    else:
        while i < iterations:
            m, c = generateStraightLine(xl[-1], fxl[-1], xu[-1], fxu[-1])
            xr.append(-c / m)
            fxr.append(functions.calc(fx, xr[-1]))
            if i > 0:
                error.append(abs((xr[-1] - xr[-2]) / xr[-1]))
                if error[-1] <= tolerance:
                    break
            if fxr[-1] == 0:
                break
            if fxr[-1] * fxl[-1] < 0:
                xu.append(xr[-1])
                xl.append(xl[-1])
            else:
                xl.append(xr[-1])
                xu.append(xu[-1])
            fxl.append(functions.calc(fx, xl[-1]))
            fxu.append(functions.calc(fx, xu[-1]))
            i += 1
    data = {'Xu': xu, 'Xl': xl, 'Xr': xr, 'f(Xu)': fxu, 'f(Xl)': fxl, 'f(Xr)': fxr,
            'Error': error}
    return data, i + 1, xr, error, message


def fixedPoint(gx, x, tolerance, iterations):
    message = ""
    error = []
    xold = [x]
    xnew = []
    i = 0
    dgx = functions.diff_f_at_point(gx)
    conv = functions.calc(dgx, x)
    if abs(conv) >= 1:
        message = f"Fixed Point Method with g(x) = {gx} \nwill fail as it will diverge from root"
    else:
        while i < iterations:
            xnew.append(functions.calc(gx, xold[-1]))
            error.append(abs((xnew[-1] - xold[-1]) / xnew[-1]))
            if error[-1] <= tolerance:
                break
            xold.append(xnew[-1])
            i += 1
    data = {'Xold': xold, 'Xnew': xnew, 'Error': error}
    return data, i, xnew, error, message


def Secant(fx, xl, xu, tolerance, iterations):
    error = []
    x0 = [xl]
    x1 = [xu]
    fx0 = []
    fx1 = []
    x2 = []
    message = ""
    i = 0
    if functions.calc(fx, x0[-1]) == functions.calc(fx, x1[-1]):
        message = f"Secant Method with X(i-1) : {x0} and X(i) : {x1}\n will fail as it will diverge from root"
    else:
        while i < iterations:
            fx0.append(functions.calc(fx, x0[-1]))
            fx1.append(functions.calc(fx, x1[-1]))
            x2.append(x1[-1] - (fx1[-1] * (x0[-1] - x1[-1])) / (fx0[-1] - fx1[-1]))
            error.append(abs((x2[-1] - x1[-1]) / x2[-1]))
            if error[-1] <= tolerance:
                break
            x0.append(x1[-1])
            x1.append(x2[-1])
            i += 1
    data = {'Xi-1': x0, 'Xi': x1, 'f(Xi-1)': fx0, 'f(Xi)': fx1, 'Xi+1': x2, 'Error': error}
    return data, i + 1, x2, error, message


def ModefiedSecant(fx, xValue, delta, tolerance, iterations):
    x = [xValue]
    error = []
    y = []
    x_next = []
    i = 0
    message = ""
    der = functions.diff_f_at_point(fx)
    conv = functions.calc(der, xValue)
    if abs(conv) == 0:
        message = f"Modified Secant Method with f(x) = {fx} and Xi : {xValue}\n will fail as it will diverge from root"
    else:
        while i < iterations:
            y.append(functions.calc(fx, x[-1]))
            x_next.append(x[-1] - (delta * x[-1] * y[-1]) / (functions.calc(fx, delta * x[-1] + x[-1]) - y[-1]))
            if x_next[-1] != 0:
                error.append(abs((x_next[-1] - x[-1]) / x_next[-1]))
            else:
                if functions.calc(fx, x_next[-1]) == 0:
                    error.append(0)
                    break
                error.append(abs((x_next[-1] - x[-1])))
            if error[-1] <= tolerance:
                break
            x.append(x_next[-1])
            i += 1
    data = {'X': x, 'f(X)': y, 'Xnext': x_next, 'Error': error}
    return data, i + 1, x_next, error, message
