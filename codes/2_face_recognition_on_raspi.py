#!/usr/bin/python3
# _*_ coding:UTF-8 _*_

import face_recognition
import picamera
import numpy as np
from collect_infos import *

camera=picamera.PiCamera()
person_name=input('enter your name please!')
main(camera,person_name)

camera.resolution = (320, 240)
output = np.empty((240, 320, 3), dtype=np.uint8)

#加载已知人名的图片
print("Loading known face image(s)")

image = face_recognition.load_image_file("%s.jpg"%person_name)
try:
	face_encoding = face_recognition.face_encodings(image)[0]
except:
	print('list index out of range')

#初始化一些参数
face_locations = []
face_encodings = []

while True:
    print("Capturing image.")
    # Grab a single frame of video from the RPi camera as a numpy array
    #从树莓派摄像头中抓取一帧图片，作为numpy的数组
    camera.capture(output, format="rgb")

    # Find all the faces and face encodings in the current frame of video
    #找出当前视频中的所有人脸和人脸编码
    face_locations = face_recognition.face_locations(output)
    print("Found {} faces in image.".format(len(face_locations)))
    face_encodings = face_recognition.face_encodings(output, face_locations)

    # Loop over each face found in the frame to see if it's someone we know.
    for face_encoding in face_encodings:
        # See if the face is a match for the known face(s)
        match = face_recognition.compare_faces([face_encoding], face_encoding)
        name = "<Unknown Person>"

        if match[0]:
            name =person_name 

        print("I see someone named {}!".format(person_name))
