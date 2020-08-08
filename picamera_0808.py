import picamera
from time import sleep
import traceback
import cv2

if __name__ == '__main__':
	try:
		camera = picamera.PiCamera()
		camera.resolution = (320,240)
		camera.capture('/home/pi/photo/mission1.jpg')
		img = cv2.imread('/home/pi/photo/mission1.jpg')
		dst = cv2.resize(img, (img.shape[1]*2, img.shape[0]*2), interpolation=cv2.INTER_NEAREST)
		cv2.imwrite('/home/pi/photo/nearest1.jpg',dst)
		camera.resolution = (640,480)
		camera.capture('/home/pi/photo/mission2.jpg')
	except:
		print(traceback.format_exc())
