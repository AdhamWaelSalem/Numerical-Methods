import sys

import numpy
import functions
import table

def generateStraightLine(x1, y1, x2, y2):
    m = (y1 - y2) / (x1 - x2)
    c = y1 - m * x1
    return m, c


def falsePosition(fx, xl, xu, tolerance, iterations):
    fxl = [functions.calc(fx, xl[-1])]
    fxu = [functions.calc(fx, xu[-1])]
    # Validations will still add them or in input directly
    # if fxl[-1] * fxu[-1] > 0:  # not valid interval
    #     pass
    # if fxl[-1] == 0:  # xl is root
    #     pass
    # if fxu[-1] == 0:  # xu is root
    #     pass
    xr = []
    fxr = []
    error = [None]
    # To decrease iterations for steep functions make first iteration as bisection method (check with them)
    i = 0
    while i < iterations:
        m, c = generateStraightLine(xl[-1], fxl[-1], xu[-1], fxu[-1])
        xr.append(-c / m)
        fxr.append(functions.calc(fx, xr[-1]))
        if fxr[-1] == 0:
            break
        print(f"iteration = {i}")
        if i > 0:
            error.append(abs((xr[-1] - xr[-2]) / xr[-1]))
            print(
                f"xl:{xl[-1]} \t xu:{xu[-1]} \t fxl:{fxl[-1]}  \tfxu:{fxu[-1]} \t xr:{xr[-1]}  \t fxr:{fxr[-1]} \t error:{error[-1]}")
            if error[-1] <= tolerance:
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
    return i, fxl, fxu, xr, fxr, error


def fixedPoint(gx, x, tolerance, iterations):
    # check for convergence
    error = [None]
    i = 0
    while i < iterations:
        x.append(functions.calc(gx, x[-1]))
        error.append(abs((x[-1] - x[-2]) / x[-1]))
        if error[-1] <= tolerance:
            break
        i += 1
    return error


def Secant(fx, x0, x1, tolerance, iterations):
    error = [None]
    fx0 = []
    fx1 = []
    x2 = []
    i = 0
    while i < iterations:
        fx0.append(functions.calc(fx, x0[-1]))
        fx1.append(functions.calc(fx, x1[-1]))
        x2.append(x1[-1] - (fx1[-1] * (x0[-1] - x1[-1])) / (fx0[-1] - fx1[-1]))
        error.append(abs((x2[-1] - x1[-1]) / x2[-1]))
        print(f"iteration = {i}")
        print(
            f"Prior:{x0[-1]}\tCurrent:{x1[-1]}\tF(prior):{fx0[-1]}\tF(current):{fx1[-1]}\tFuture:{x2[-1]}\tError:{error[-1]}")
        if error[-1] <= tolerance:
            break
        x0.append(x1[-1])
        x1.append(x2[-1])
        i += 1
    return fx0, fx1, x2, error


def ModefiedSecant(fx, x, delta, tolerance, iterations):
    error = [None]
    y = []
    x_next = []
    i = 0
    while i < iterations:
        y.append(functions.calc(fx, x[-1]))
        x_next.append(x[-1] - (delta * x[-1] * y[-1]) / (functions.calc(fx, delta * x[-1] + x[-1]) - y[-1]))
        error.append(abs((x_next[-1] - x[-1]) / x_next[-1]))
        print(f"iteration = {i}")
        print(
            f"Current:{x[-1]}\tF(current):{y[-1]}\tFuture:{x_next[-1]}\tError:{error[-1]}")
        if error[-1] <= tolerance:
            break
        x.append(x_next[-1])
        i += 1
    return y, x_next, error


if __name__ == "__main__":
    # False Position
    xl = [0]
    xu = [2]
    fx = "x**4-2*x**3-4*x**2-4*x+4"
    tolerance = 0.00000001
    iterations = 100
    i, fxl, fxu, xr, fxr, error = falsePosition(fx, xl, xu, tolerance, iterations)

    # trying to draw table
    data = {
        'Iteration': range(i),
        'X_lower': xl,
        'X_upper': xu,
        'f(x_lower)': fxl,
        'f(x_upper)': fxu,
        'X_r': xr,
        'f(x_r)': fxr,
        'Error': error
    }

    # # Fixed Point
    # x = [2]
    # gx = "(2*x-1)/x"
    # error = fixedPoint(gx, x, tolerance, iterations)
    # print(numpy.column_stack((x, error)))
    #
    # # Secant
    # x_prior = [0]
    # x_current = [1]
    # x_successive, fx_prior, fx_current, error = Secant(fx, x_prior, x_current, tolerance, iterations)
    #
    # # Modified Secant
    # x = [1]
    # y, x_next, error = ModefiedSecant(fx, x, 0.01, tolerance, iterations)
