# Face-Detection
This program is written in python36 in jupyter notebook. Done by the openCV module. Can also run on terminal python36 in redhat.
This is also a Computer Vision project.

#face_detection.py
  import cv2 = to import cv2 module
  ret,photo=cap.read() = to read photo from camera
	faces=face_detect.detectMultiScale(photo) = it is a function which provides human face recognition
	photo=cv2.rectangle(photo,(x,y),(x2,y2),(0,255,0),4) = function to create a rectangle over face
  cv2.imshow("hi",photo) = to show a text on photo taken
		if cv2.waitKey(1)==13: = to wait until the signal "Enter key" to close
			break

  cv2.destroyAllWindows() = to destroy all windows opening as video is only random photos  
  cap.release() = to release the camera
