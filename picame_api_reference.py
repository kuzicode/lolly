import picamera



def capturing_to_file():

	#capturing to a file
	from time import sleep
	from picamera import PiCamera

	camera = PiCamera()
	camera.resolution = (1024, 768)
	camera.start_preview()
	# Camera warm-up time
	sleep(2)
	camera.capture('foo.jpg')

def capturing_timelapse():
	from time import sleep
	from picamera import PiCamera

	camera = PiCamera()
	camera.start_preview()
	sleep(2)
	for filename in camera.capture_continuous('img{counter:03d}.jpg'):
	    print('Captured %s' % filename)
	    sleep(300) # wait 5 minutes


def capturing_in_low_light():
	from picamera import PiCamera
	from time import sleep
	from fractions import Fraction

	# Force sensor mode 3 (the long exposure mode), set
	# the framerate to 1/6fps, the shutter speed to 6s,
	# and ISO to 800 (for maximum gain)
	camera = PiCamera(
	    resolution=(1280, 720),
	    framerate=Fraction(1, 6),
	    sensor_mode=3)
	camera.shutter_speed = 6000000
	camera.iso = 800
	# Give the camera a good long time to set gains and
	# measure AWB (you may wish to use fixed AWB instead)
	sleep(30)
	camera.exposure_mode = 'off'
	# Finally, capture an image with a 6s exposure. Due
	# to mode switching on the still port, this will take
	# longer than 6 seconds
	camera.capture('dark.jpg')	
	
def open_close_image():
    from PIL import Image
    import subprocess
    
    p = subprocess.Popen(["display", "jack.jpg"])
    i=input("Give a name for image:")
    p.kill()

open_close_image()
