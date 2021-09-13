#video recording using ipwebcam

#keyrun

#importing urllib.request will get the content in the specific url
import urllib.request
import cv2
import numpy as np
#paste the image address url below
url=''
while True:
	imgresp=urllib.request.urlopen(url)
	imgN=np.array(bytearray(imgresp.read()),dtype=np.uint8)
	img=cv2.imdecode(imgN,-1) #decoding the image obtained from url
	cv2.imshow("test",img) #displaying the image 
	if ord("q")==cv2.waitKey(10): #if you press q it exits from the while loop hence video tab will be closed
		exit(0)
