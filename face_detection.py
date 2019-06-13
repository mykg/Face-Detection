import cv2
face_detect=cv2.CascadeClassifier("haarcascade_frontalface_default.xml") #to make the program intelligent

cap=cv2.VideoCapture(0) #capture photo
#ret,photo=cap.read() #read photo

while True:
	ret,photo=cap.read()
	faces=face_detect.detectMultiScale(photo)
	if faces is not():
		x=faces[0][0] #x axis
		y=faces[0][1] #y axis
		x2=faces[0][2]+x
		y2=faces[0][3]+y

		photo=cv2.rectangle(photo,(x,y),(x2,y2),(0,255,0),4) #function to create a rectangle
		
		#crop=photo[y-20:y+height+20,x-20:x+width+20]
		#print(crop.shape)

		cv2.imshow("hi",photo)
		if cv2.waitKey(1)==13:
			break

cv2.destroyAllWindows()
len(faces) # to count the number of faces detected
cap.release()
