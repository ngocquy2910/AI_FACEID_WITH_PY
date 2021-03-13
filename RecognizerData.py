import numpy as np 
import cv2
import sqlite3
import os	
from PIL import Image

#traning hinh anh va nhan dien 
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
recognizer = cv2.face.LBPHFaceRecognizer_create()
#lay models
recognizer.read('C:\\Users\\Nguyen Ngoc Quy\\CODE\\AI_FACEID\\recognizer\\trainningData.yml')
#get profile by id trong data
def getProfile(id):
 	conn = sqlite3.connect('C:\\Users\\Nguyen Ngoc Quy\\OneDrive\\Máy tính\\DB Browser for SQLite\\data.db')
 	query = 'SELECT * FROM PEOPLE WHERE ID=' +str(id)
 	curror = conn.execute(query)

 	profile = None
 	for row in curror:
 		profile = row
 	conn.close()
 	return profile
cap = cv2.VideoCapture(0)
fontface = cv2.FONT_HERSHEY_SIMPLEX

while(True):
	ret, fraem = cap.read()

	gray = cv2.cvtColor(fraem, cv2.COLOR_BGR2GRAY)

	faces = face_cascade.detectMultiScale(gray)

	for(x,y,w,h) in faces:
		cv2.rectangle(fraem, (x,y),(x+w,y+h), (0,255,0),2)

		#cat anh so sanh
		roi_gray = gray[y: y+h, x: x+w]

		#nhan dien
		id, confidence = recognizer.predict(roi_gray)
		# do chinh xac tren 50%
		if confidence < 50:
			profile = getProfile(id)
			if(profile != None):
				cv2.putText(fraem,""+str(profile[1]), (x+10,y+30+h), fontface, 1, (0,255,0),2)
		else:
			cv2.putText(fraem,"HACKER", (x+10,y+30+h), fontface, 1, (0,0,255),2)
	cv2.imshow('image',fraem)
	if(cv2.waitKey(1)== ord('q')):
		break;

 	

cap.release()
cv2.destroyAllWindows()