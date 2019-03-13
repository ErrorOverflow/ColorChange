import cv2 as cv
import numpy as np
import operator

params = {
    'red': 0,
    'orange': 11
}


def color_change(img, img_hsv, color):
    # solve h
    for x in range(img.shape[1]):
        for y in range(img.shape[0]):
            r = img[x, y][0]
            g = img[x, y][1]
            b = img[x, y][2]
            max = np.max(img[x, y])
            min = np.min(img[x, y])
            if max == min:
                h = 0
            elif np.argmax(img[x, y]) == 0 and g >= b:
                h = 60 * (g - b) / (max - min)
            elif np.argmax(img[x, y]) == 0 and g < b:
                h = 60 * (g - b) / (max - min) + 360
            elif np.argmax(img[x, y]) == 1:
                h = 60 * (b - r) / (max - min) + 120
            else:
                h = 60 * (r - g) / (max - min) + 240
            if max == 0:
                s = 0
            else:
                s = 1 - min / max
            v = max
            h = params.get(color)
            img_hsv[x, y] = [h, s, v]
    cv.imshow('res', img_hsv)
    cv.waitKey(0)
    return 0


if __name__ == '__main__':
    img = cv.imread('image/img.jpg')
    img_hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)
    color_change(img, img_hsv, 'red')
