import face_recognition
import picamera
import numpy as np
from collect_infos import *

camera=picamera.PiCamera()
person_name=input('请输入你的名字')

collect_infos(camera,person_name)

camera.resolution = (320, 240)
output = np.empty((240, 320, 3), dtype=np.uint8)

#加载已知人名的图片
print("Loading known face image(s)")

image = face_recognition.load_image_file("%s.jpg"%person_name)
try:
    face_encoding = face_recognition.face_encodings(image)[0]

    #初始化一些参数
    face_locations = []
    face_encodings = []

    while True:
        print("Capturing image.")
        #从树莓派摄像头中抓取一帧图片，作为numpy的数组
        camera.capture(output, format="rgb")

        #找出当前帧数中的所有人脸位置和人脸编码
        face_locations = face_recognition.face_locations(output)
        print("Found {} faces in image.".format(len(face_locations)))
        face_encodings = face_recognition.face_encodings(output, face_locations)

        #遍历图片中每一张人脸，看是否为已知人脸
        for face_encoding in face_encodings:
            # See if the face is a match for the known face(s)
            match = face_recognition.compare_faces([face_encoding], face_encoding)
            name = "<Unknown Person>"

            if match[0]:
                name =person_name 

            print("I see someone named {}!".format(person_name))
except :
    print("take another picture and try it again")
