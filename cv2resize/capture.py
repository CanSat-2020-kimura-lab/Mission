import time
import picamera
import numpy as NumPy
import cv2
 
with picamera.PiCamera() as camera:
 camera.resolution = (320,240)
 camera.start_preview()
 time.sleep(2)
 camera.capture('test1.jpg')

 # 入力画像の読み込み
 img = cv2.imread("/home/pi/picamera/test1.jpg")

 # グレースケール変換
 #gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

 # 方法2
 dst = cv2.resize(
     img, (img.shape[1]*2, img.shape[0]*2), interpolation=cv2.INTER_NEAREST)

 # 結果を出力
 cv2.imwrite("/home/pi/picamera/nearest1.jpg", dst)


with picamera.PiCamera() as camera:
  camera.resolution = (640, 480)
  camera.start_preview()
  time.sleep(2)
  camera.capture('test2.jpg')
