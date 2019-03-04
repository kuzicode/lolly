import face_recognition
import picamera
import numpy as np
from collect_infos import *

camera = picamera.PiCamera()
person_name = input('Please input your name: ')

collect_infos(camera, person_name)

camera.resolution = (320, 240)
output = np.empty((240, 320, 3), dtype = np.uint8)

# Loading known face
print("Loading known face image(s)")

image = face_recognition.load_image_file("%s.jpg" % person_name)
try:
    face_encoding = face_recognition.face_encodings(image)[0]
    # parameters init
    face_locations = []
    face_encodings = []

    while True:
        print("Capturing image.")
        # get frame data from raspi camera as numpy array
        camera.capture(output, format="rgb")

        # Find all face positions and face codes in the current frame number
        face_locations = face_recognition.face_locations(output)
        print("Found {} faces in image.".format(len(face_locations)))
        face_encodings = face_recognition.face_encodings(output, face_locations)

        # Range every face from frame picture，find known face
        for face_encoding in face_encodings:
            # See if the face is a match for the known face(s)
            match = face_recognition.compare_faces([face_encoding], face_encoding)
            name = "<Unknown Person>"

            if match[0]:
                name =person_name 

            print("I see someone named {}!".format(person_name))
except :
    print("take another picture and try it again")
