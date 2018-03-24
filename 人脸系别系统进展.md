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

5.now i need to shutdown the image after i open it



