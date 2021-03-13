import cv2
import numpy as np 
import sqlite3
import os

def insert0rUpdate(id, name):
	conn = sqlite3.connect('C:\\Users\\Nguyen Ngoc Quy\\OneDrive\\Máy tính\\DB Browser for SQLite\\data.db')

	query = "SELECT * FROM PEOPLE WHERE ID=" + str(id)

	cusror = conn.execute(query)

	isRecordExist = 0

	for row in cusror:
		isRecordExist = 1
	if (isRecordExist == 0):
		query = "INSERT INTO PEOPLE(ID, NAME) VALUES("+str(id)+",'"+ str(name)+"')"
	else:
		query = "UPDATE PEOPLE SET NAME='" + str(name)+"' WHERE ID="+ str(id)
	conn.execute(query)
	conn.commit()
	conn.close()

#load lib
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
#truy cap vao camera
cap = cv2.VideoCapture(0)
#input data id name
id = input("Enter Your ID: ")
name = input("Enter Your Name: ")
insert0rUpdate(id,name)
#chi so index
sampleNum = 0
#laydata from camera

while(True):
	ret, frame = cap.read()
	# convert anh thanh trang den
	gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
	# CONNECT ANH VOI FACE ID
	faces = face_cascade.detectMultiScale(gray, 1.3 ,5)
	for(x,y,w,h) in faces:
		cv2.rectangle(frame, (x,y), (x+w,y+h), (0,255,0),2)
		if not os.path.exists('dataSet'):
			os.makedirs('dataSet')
		sampleNum +=1

		#ghi anh moi 
		cv2.imwrite('dataSet/Users.'+str(id)+'.'+str(sampleNum)+'.jpg', gray[y: y+h,x: x+w]) #toa do tinh tien
	#show anh
	cv2.imshow('frame',frame)
	cv2.waitKey(1)

	if sampleNum > 500:
		break;



	

cap.release()
cv2.destroyAllWindows()

