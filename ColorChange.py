import cv2 as cv
import numpy as np

params = {
    'blue': 0,
    'yellow': 180
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
            if max == 0:
                s = 0
            else:
                s = 1 - min / max
            v = max
            h = 180
            hi = int(h / 60) % 6
            f = h / 60 - hi
            p = v * (1 - s)
            q = v * (1 - f * s)
            t = v * (1 - (1 - f) * s)
            if hi == 0:
                img[x, y] = [v, t, p]
            elif hi == 1:
                img[x, y] = [q, v, p]
            elif hi == 2:
                img[x, y] = [p, v, t]
            elif hi == 3:
                img[x, y] = [p, q, v]
            elif hi == 4:
                img[x, y] = [t, p, v]
            elif hi == 5:
                img[x, y] = [v, p, q]
    cv.imshow('res', img)
    cv.imwrite('yellow.jpg', img, None)
    cv.waitKey(0)
    return 0


if __name__ == '__main__':
    img = cv.imread('image/img.jpg')
    img_hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)
    color_change(img, img_hsv, 'orange')
