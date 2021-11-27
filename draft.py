from numpy import *
from numpy.dual import lstsq


def generateStraightLine():
    points = [(1, 5), (3, 4)]
    x_coords, y_coords = zip(*points)
    A = vstack([x_coords, ones(len(x_coords))]).T
    m, c = lstsq(A, y_coords, None)[0]
    return "{m}x + {c}".format(m=m, c=c)


if __name__ == "__main__":
    print(generateStraightLine())
    print("Draft Work")
