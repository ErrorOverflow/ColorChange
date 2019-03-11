import cv2 as cv
import numpy as np


def his_match(src, dst):
    res = np.zeros_like(dst)
    # cdf 为累计分布
    cdf_src = np.zeros((3, 256))
    cdf_dst = np.zeros((3, 256))
    cdf_res = np.zeros((3, 256))
    kw = dict(bins=256, range=(0, 256), normed=True)
    for ch in range(3):
        his_src, _ = np.histogram(src[:, :, ch], **kw)
        hist_dst, _ = np.histogram(dst[:, :, ch], **kw)
        cdf_src[ch] = np.cumsum(his_src)
        cdf_dst[ch] = np.cumsum(hist_dst)
        index = np.searchsorted(cdf_src[ch], cdf_dst[ch], side='left')
        np.clip(index, 0, 255, out=index)
        res[:, :, ch] = index[dst[:, :, ch]]
        his_res, _ = np.histogram(res[:, :, ch], **kw)
        cdf_res[ch] = np.cumsum(his_res)
    return res, (cdf_src, cdf_dst, cdf_res)


src = cv.imread('C:/Users/WML/PycharmProjects/ColorChange/image/image000001.jpg')
# src = cv.imread('flower.jpg')
# src = cv.imread('summer.jpg')
dst = cv.imread('C:/Users/WML/PycharmProjects/ColorChange/image/orange.jpg')
# dst = cv.imread('greentree.jpg')


# src = cv.imread('autumn.jpg')
# dst = cv.imread('greentree.jpg')

cv.imshow('src', src)
cv.imshow('dst', dst)
res, cdfs = his_match(src, dst)
cv.imshow('res', res)

print(cdfs[0].shape)
cv.waitKey(0)
