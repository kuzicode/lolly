import picamera

#create a PiCamera instance
camera=picamera.PiCamera()

#take a picture
camera.capture('image.jpg')

#start preview
camera.start_preview()

#stop preview
camera.stop_preview()