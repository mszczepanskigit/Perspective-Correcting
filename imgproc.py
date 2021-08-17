"""Contains functions to correct perspective of given image"""
import numpy as np


def perspective_projection(original, params):
    """
    Transforms a set of points to correct perspective.

    :param original: Tuple with sets of x and y coordinates.
    :param params: Set of parameters to determine transformation.

    :return: Tuple (xp, yp) where xp and yp are coordinates after transformation.
    """
    x, y = original
    A, B, C, D, E, F, G, H = params

    xp = (A*x+B*y+C)/(G*x+H*y+1)
    yp = (D*x+E*y+F)/(G*x+H*y+1)

    return xp, yp


def find_transformation(points, ref_points):
    """
    Allow to finding parameters to correct perspective.

    :param points: Given points from mouse clicks.
    :param ref_points: New coordinates for points

    :return: Parameters for perspective_projection() and correct_persp().
    """
    M = np.zeros((8, 8))
    v = np.zeros(8)

    for i in range(0, 4):
        x, y = ref_points[i]
        xp, yp = points[i]

        M[2*i, :] = np.array([x, y, 1, 0, 0, 0, -x*xp, -y*xp])
        M[2*i+1, :] = np.array([0, 0, 0, x, y, 1, -x*yp, -y*yp])

        v[2*i] = xp
        v[2*i+1] = yp

    params = np.linalg.solve(M, v)
    return params


def correct_persp(img, params, width, height):
    """
    Correcting perspective of given image. Need special params and new width and height.

    :param img: Given image from sys_arg[1].
    :param params: Parameters found in find_transformation().
    :param width: New width for the given area to correct perspective.
    :param height: New height for the given area to correct perspective.
    :return: Return new image which is grabbed area with corrected perspective.
    """
    rows = np.linspace(0, height-1, height)
    cols = np.linspace(0, width-1, width)

    x, y = np.meshgrid(cols, rows)
    x = x.astype(np.int32)
    y = y.astype(np.int32)

    xp, yp = perspective_projection((x, y), params)
    org_cols = np.floor(xp).astype(np.int32)
    org_rows = np.floor(yp).astype(np.int32)

    results = np.zeros((height, width, 3))
    results[y, x, :] = img[org_rows, org_cols, :]
    results = results.astype(np.uint8)

    return results
