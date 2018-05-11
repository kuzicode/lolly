import time

def take_picture(camera,name):
        #'preview the webcam and take a picture after 2s'
	camera.start_preview()
	time.sleep(3)
	camera.capture(name)
	camera.stop_preview()

def satisfaction_of_image(path):
    #'preview the picture and quit'
    
    print('请查看你拍的照片，核对是否满意') 
    from PIL import Image
    import subprocess
    
    p = subprocess.Popen(["display", path])
    time.sleep(3)
    p.kill()

def collect_infos(camera,name):
	name='%s.jpg'%name
	print('即将在3秒后进行拍照，请注意')
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
    collect_infos()
