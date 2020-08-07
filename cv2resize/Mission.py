import sys
sys.path.append('/home/pi/git/kimuralab/Other')

import picamera
import time
import traceback
import Other

def measurement_nearest(func, **kwargs):
	val_n = func(kwargs["gray0"], kwargs["gray1"])
	return val_n

def measurement_linear(func, **kwargs):
	val_l = func(kwargs["gray0"], kwargs["gray2"])
	return val_l

def measurement_cubic(func, **kwargs):
	val_c = func(kwargs["gray0"], kwargs["gray3"])
	return val_c

def Mission(photo_path1,photo_path2):
	photo_path1 = ''
	photo_path2 = ''
	try:
		# --- Save photos in two resolution --- #
		camera = picamera.PiCamera()
		camera.resolution = (320,240)
		camera.capture(photo_path1)
		camera.resolution = (640,480)
		camera.capture(photo_path2)
		# --- Read two images --- #
		img1 = cv2.imread(photo_path1)
		img2 = cv2.imread(photo_path2)
		# --- hight resolution --- #
		dst1 = cv2.resize(img1, (img1.shape[1]*4, img1.shape[0]*4), interpolation=cv2.INTER_NEAREST)
		dst2 = cv2.resize(img1, (img1.shape[1]*4, img1.shape[0]*4), interpolation=cv2.INTER_LINEAR)
		dst3 = cv2.resize(img1, (img1.shape[1]*4, img1.shape[0]*4), interpolation=cv2.INTER_CUBIC)
		# --- Save high resolution images --- #
		filepath = ''
		filepath = Other.fileName('/home/pi/photo/nearest','jpg') # nearest
		cv2.imwrite(filepath, dst1)
		filepath = Other.fileName('/home/pi/photo/linear','jpg') # linear
		cv2.imwrite(filepath, dst2)
		filepath = Other.fileName('/home/pi/photo/cubic','jpg') # cubic
		cv2.imwrite(filepath, dst3)
		# --- Convert to grayscale --- #
		gray0 = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)
		gray1 = cv2.cvtColor(dst1, cv2.COLOR_BGR2GRAY)
		gray2 = cv2.cvtColor(dst2, cv2.COLOR_BGR2GRAY)
		gray3 = cv2.cvtColor(dst3, cv2.COLOR_BGR2GRAY)
		# --- Calculate ssim --- #
		print("ssim_n: " + str(measurement_nearest(compare_ssim, gray0 = gray0, gray1 = gray1)))
		print("ssim_l: " + str(measurement_linear(compare_ssim, gray0 = gray0, gray2 = gray2)))
		print("ssim_c: " + str(measurement_cubic(compare_ssim, gray0 = gray0, gray3 = gray3)))

	except picamera.exc.PiCameraMMALError:
		photo_path = 'Null'
		time.sleep(1)
	except:
		print(traceback.format_exc())
		time.sleep(0.1)
	return photo_path

if __name__ == '__main__':
	try:
		Mission('/home/pi/photo/mission1','/home/pi/photo/mission2')
	except:
		print(traceback.format_exc)
