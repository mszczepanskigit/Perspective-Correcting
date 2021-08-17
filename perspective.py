"""Main structure to correct perspective of grabbed area. For more info there is readme.txt file."""

import sys
import cv2
import imgproc

im_to_read = sys.argv[1]
im_to_write = sys.argv[2]
height_sys = int(sys.argv[3])
width_sys = int(sys.argv[4])
points = []

img = cv2.imread(im_to_read)
img_cpy = img.copy()

cv2.imshow("image", img_cpy)


def add_point(event, x, y, *args):
    """Adding point by mouse clicking."""
    if event == cv2.EVENT_LBUTTONDOWN:
        points.append((x, y))
        cv2.circle(img_cpy, (x, y), 3, [0, 255, 0], -1)

        if len(points) == 4:
            height = height_sys
            width = width_sys
            ref_points = [(0, 0), (width-1, 0), (width-1, height-1), (0, height-1)]
            params = imgproc.find_transformation(points, ref_points)
            rectified_img = imgproc.correct_persp(img, params, width, height)
            cv2.imshow("rectified image", rectified_img)
            cv2.imwrite(im_to_write, rectified_img)


cv2.setMouseCallback("image", add_point)

while True:
    cv2.imshow("image", img_cpy)
    key = cv2.waitKey(1)
    if key == ord("q"):
        break
