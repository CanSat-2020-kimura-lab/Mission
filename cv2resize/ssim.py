from skimage.measure import compare_ssim
import cv2
import time

img1 = cv2.imread("C:/Users/Hasse/Desktop/12small.jpg")
img2 = cv2.imread("C:/Users/Hasse/Desktop/12big.jpg")

#NEAREST
dst1 = cv2.resize(img1, (img1.shape[1]*4, img1.shape[0]*4), interpolation=cv2.INTER_NEAREST)
#LINEAR
dst2 = cv2.resize(img1, (img1.shape[1]*4, img1.shape[0]*4), interpolation=cv2.INTER_LINEAR)
#CUBIC
dst3 = cv2.resize(img1, (img1.shape[1]*4, img1.shape[0]*4), interpolation=cv2.INTER_CUBIC)

cv2.imwrite("C:/Users/Hasse/Desktop/nearest15.jpg", dst1)
cv2.imwrite("C:/Users/Hasse/Desktop/linear15.jpg", dst2)
cv2.imwrite("C:/Users/Hasse/Desktop/cubic15.jpg", dst3)

cv2.imshow("nearest", dst1)
cv2.imshow("linear", dst2)
cv2.imshow("cubic", dst3)
cv2.waitKey(0)
cv2.destroyAllWindows()

gray0 = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)
gray1 = cv2.cvtColor(dst1, cv2.COLOR_BGR2GRAY)
gray2 = cv2.cvtColor(dst2, cv2.COLOR_BGR2GRAY)
gray3 = cv2.cvtColor(dst3, cv2.COLOR_BGR2GRAY)

def measurement_nearest(func, **kwargs):
	start = time.time()
	val = func(kwargs["gray0"], kwargs["gray1"])
	end = time.time()
	return val, end-start

def measurement_linear(func, **kwargs):
	start = time.time()
	val = func(kwargs["gray0"], kwargs["gray2"])
	end = time.time()
	return val, end-start

def measurement_cubic(func, **kwargs):
	start = time.time()
	val = func(kwargs["gray0"], kwargs["gray3"])
	end = time.time()
	return val, end-start

print("ssim_n: %f, time_n: %lf[sec]" % measurement_nearest(compare_ssim, gray0 = gray0, gray1 = gray1))

print("ssim_l: %f, time_l: %lf[sec]" % measurement_linear(compare_ssim, gray0 = gray0, gray2 = gray2))

print("ssim_c: %f, time_c: %lf[sec]" % measurement_cubic(compare_ssim, gray0 = gray0, gray3 = gray3))
