import time

def take_picture(camera,name):
        #'preview the webcam and take a picture after 2s'
	camera.start_preview()
	time.sleep(3)
	camera.capture(name)
	camera.stop_preview()


def satisfaction_of_image(path):
    #'preview the picture and quit'
    print('Please check the photos you took to check if you are satisfied.') 
    from PIL import Image
    import subprocess
    
    p = subprocess.Popen(["display", path])
    time.sleep(3)
    p.kill()


def collect_infos(camera, name):
	name = '%s.jpg' % name
	print('Take a photo after 3 seconds ...')
	time.sleep(3)
	take_picture(camera, name)

	while True:      
            satisfaction_of_image(name)
            i=input('Satisfied with the picture taken, enter "y" to the next step, or "n" to retake ...y/n ')
            if i=='n':
                    take_picture(camera, name)
            else:
                print('Done, end of photo.')
                break


if __name__=="__main__":
    collect_infos()
