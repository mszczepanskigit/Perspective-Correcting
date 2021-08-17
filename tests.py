"""Contains some tests that I've done during coding"""

import imgproc
import numpy as np

x = np.array([-1, 1, 1, -1])
y = np.array([-1, -1, 1, 1])

params = [0.35, 0, 0, 0, 0.5, 0, -0.35, 0]

xp, yp = imgproc.perspective_projection((x, y), params)

ref_points = [(a, b) for a, b in zip(x, y)]
points = [(a, b) for a, b in zip(xp, yp)]

params = imgproc.find_transformation(points, ref_points)

v = np.zeros(3)

print(points)
print(ref_points)
print(params)
print(v)