#总体框架#

1.信息采集阶段----拍照，并预览。照片满意就保存，不满意就舍弃。(将图片放到指定文件夹)

2.系统正式开始----从摄像头截取一张照片，与已存在人脸对比


实现时计划和遇到的困难：

###2018.3.22###  

1.识别系统先用官方的例子，现在先完成第一点信息采集----写好了，具体得到树莓派上测试  
2.看一下能不能用picamera实现，从摄像头中勾画出脸部，并识别出人名-----似乎找不到，我再试试Opencv能不能实现吧  
3.先用picamera 测试下树莓派的摄像头拍照问题..休息下---the module picamera can work and i can take a picture after preview on wecam,goodjob.  
4.but i get stuck in situation that i can not open the picture on command line,fortunately,i fix it after i installed the "imagemagick" package by run the command "sudo apt install imagemagick "  
5.now i need to closed the image after i open it  

###2018.3.24###  

需要解决的问题是：  

1.树莓派摄像头是排线摄像头，opencv库无法进为入摄像头的问题  
2.vncview登陆无法显示视频，所有只能用3.5寸的屏幕来显示，先安装驱动，教程链接(http://kookye.com/2017/01/18/install-3-5-hdmi-touch-
screen-linux-driver-on-raspberry-pi/)  
3.u盘无法在树莓派上使用的问题  


###2018.3.27###  

想要设计一个图形用户界面，python中有一些图形界面的库，如pyQt、wxpython.  
如果想设计一个优秀的图形界面得用pyQt,但是想先用wxpython设计出一个简单的来用用  

问题：  
1.要解决图形界面中显示视频流的问题。  

https://www.jianshu.com/p/8f4ee3de02e6  


###2018.3.28###  

要做的事：
1.了解GUI生成器    ----已初步了解GUI生成器的工作流程
2.熟悉wxpython库
3.初步了解Opencv库


###2019.3.3###  
Rebuild拍照和对比识别代码，处理在linux下vim的编辑问题

