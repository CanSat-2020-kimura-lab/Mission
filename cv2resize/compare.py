from skimage.measure import compare_ssim
import cv2
import time

def measurement(func, **kwargs):
    start = time.time()
    val = func(kwargs["img1"], kwargs["img2"])
    end = time.time()
    return val, end-start

img1 = cv2.imread("photo2.jpg", cv2.IMREAD_GRAYSCALE)
img2 = cv2.imread("nearest1.jpg", cv2.IMREAD_GRAYSCALE)
print("ssim: %f, time: %lf[sec]" % measurement(compare_ssim, img1=img1, img2=img2))
