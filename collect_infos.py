import time

def take_picture(camera,name):
        #'preview the webcam and take a picture after 2s'
	camera.start_preview()
	time.sleep(3)
	camera.capture(name)
	camera.stop_preview()

def satisfaction_of_image(path):
    #'preview the picture and quit'
    
    print('look at the picture and take a picture again if you are not satisfy') 
    from PIL import Image
    import subprocess
    
    p = subprocess.Popen(["display", path])
    time.sleep(3)
    p.kill()

def main(camera,name):
	name='%s.jpg'%name
	print('read to take a picture,pay attention please')
	time.sleep(3)
	take_picture(camera,name)

	while True:      
            satisfaction_of_image(name)
            i=input('是否对拍的图片感到满意,输入 y 进入下一步，或 n 进行重拍...y/n')
            if i=='n':
                    take_picture(camera,name)
            else:
                print('end')
                break


if __name__=="__main__":
    main()
