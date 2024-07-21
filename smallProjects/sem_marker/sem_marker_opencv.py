import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread("test.jpg")
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# OTSU: find a optimal threshold automatically
ret, binary_image = cv2.threshold(gray, 150, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)
h, w = np.shape(binary_image)

# exact the middle line
middle_line_index = w // 2
middle_line = binary_image[middle_line_index, :]
offset = middle_line_index + 5
line2 = binary_image[offset, :]


# locate the start point and end point of fiber in the selected line
def find_points(line):
    start_point = []
    end_point = []
    index = 0
    count = 1
    while index < len(line) - 1:
        if line[index] == 255 and line[index + 1] == 255:
            count += 1
            index += 1
        else:
            if count >= 10:
                start_point.append(index - count + 1)
                end_point.append(index)
                count = 1
                index += 1
            else:
                count = 1
                index += 1
    return start_point, end_point


def calc_vp(x1, y1, x2, y2, x0, y0):
    """:arg x1,y1,x2,y2 are used to calculate line Ax + By + C = 0
    x0, y0 is used to calculate the coordinate of the vertical point
    """
    A = y2 - y1
    B = x1 - x2
    C = x2 * y1 - x1 * y2

    x_vp = (B * B * x0 - A * B * y - A * C) / (A * A + B * B)
    y_vp = (A * A * y0 - A * B * x - B * C) / (A * A + B * B)

    return x_vp, y_vp


s1, e1 = find_points(middle_line)
s2, e2 = find_points(line2)
print(s1)
print(e1)
print(s2)
print(e2)

if len(s1) == len(s2):
    for i in range(len(s1)):
        y1 = s1[i]
        x1 = middle_line_index
        y2 = s2[i]
        x2 = offset
        y0 = e1[i]
        x0 = middle_line_index
        x_vp, y_vp = calc_vp(x1, y1, x2, y2, x0, y0)
        cv2.line(img, (x_vp, y_vp), (x0, y0), color=(0, 0, 255), thickness=1)

for i in range(len(s1)):
    cv2.line(img, (middle_line_index, s1[i]), (middle_line_index, e1[i]), color=(0, 0, 255), thickness=1)

for i in range(len(s2)):
    cv2.line(img, (offset, s2[i]), (offset, e2[i]), color=(0, 0, 255), thickness=1)

cv2.imshow("", img)
cv2.waitKey(0)
