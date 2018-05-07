#!/usr/bin/python3
# _*_ coding:UTF-8 _*_

import face_recognition

picture_of_me=face_recognition.load_image_file("jack.jpg")
my_face_encoding=face_recognition.face_encodings(picture_of_me)[0]

unknow_picture=face_recognition.load_image_file("unknow.jpg")
unknow_face_encoding=face_recognition.face_encodings(unknow_picture)[0]

results=face 
