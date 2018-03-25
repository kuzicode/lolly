#总体框架#

1.信息采集阶段----拍照，并预览。照片满意就保存，不满意就舍弃。(将图片放到指定文件夹)

2.系统正式开始----从摄像头截取一张照片，与已存在人脸对比

	2.1 



实现时计划和遇到的困难：

###2018.3.22###

1.识别系统先用官方的例子，现在先完成第一点信息采集----写好了，具体得到树莓派上测试

2.看一下能不能用picamera实现，从摄像头中勾画出脸部，并识别出人名-----似乎找不到，我再试试Opencv能不能实现吧

3.先用picamera 测试下树莓派的摄像头拍照问题..休息下---the module picamera can work and i can take a picture after preview on wecam,goodjob.

4.but i get stuck in situation that i can not open the picture on command line,fortunately,i fix it after i installed the "imagemagick" package by run the command "sudo apt install imagemagick "

5.now i need to closed the image after i open it

###2018.3.24###

需要解决的问题是：
1.树莓派摄像头是排线摄像头，opencv库无法进入摄像头的问题
2.vncview登陆无法显示视频，所有只能用3.5寸的屏幕来显示，先安装驱动，教程链接(http://kookye.com/2017/01/18/install-3-5-hdmi-touch-screen-linux-driver-on-raspberry-pi/)
3.u盘无法在树莓派上使用的问题

###2018.3.25###
树莓派摄像头是排线摄像头，opencv库无法进入摄像头的问题
https://thinkrpi.wordpress.com/2013/05/22/opencv-and-camera-board-csi/

pip安装Opencv问题：
https://pypi.python.org/pypi/opencv-python

实时人脸识别：
https://www.hackster.io/mjrobot/real-time-face-recognition-an-end-to-end-project-a10826

安装Opencv3
https://www.pyimagesearch.com/2017/09/04/raspbian-stretch-install-opencv-3-python-on-your-raspberry-pi/





