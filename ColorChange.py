import cv2 as cv
import numpy as np
import operator

params = {
    'red': [240, 15, 15],
    'yellow': [255, 255, 0],
    'green': [0, 255, 0],
    'blue': [0, 0, 255],
    'gray': [128, 128, 128],
    'white': [255, 255, 255],
    'black': [0, 0, 0]
}


def color_change(img, pixel, color):
    r = np.average(img[70:90, 60:90][0])
    g = np.average(img[70:90, 60:90][1])
    b = np.average(img[70:90, 60:90][2])
    for x in range(70, 90):
        for y in range(60, 90):
            if operator.eq(img[x, y], [255, 255, 255]):
                img[x, y][0] = (params.get(color)[0] + img[x, y][0] - r)
                img[x, y][1] = (params.get(color)[1] + img[x, y][1] - g)
                img[x, y][2] = (params.get(color)[2] + img[x, y][2] - b)
    cv.imshow("wee", img)
    cv.waitKey(0)
    return 0


if __name__ == '__main__':
    img = cv.imread('image/img000001.png')
    gray_img = cv.imread('image/img000001.png', 0)
    pixel = [[1 for __ in range(img.shape[0])] for _ in range(img.shape[1])]
    cv.imshow("gray", gray_img)

    color_change(img, pixel, 'red')
