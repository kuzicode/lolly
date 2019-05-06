### lolly
简单的人脸识别程序 from https://github.com/ageitgey/face_recognition  
raspberrypi + dlib + python3     

### Progress
1.信息采集阶段: 拍照并预览。照片满意就保存，不满意就舍弃。(将图片放到指定文件夹)  
2.系统工作开始: 从摄像头截取一张image，与本地存储已存在人脸image对比，返回对比相似度结果  

### Ready
[Raspberrypi linux环境搭建过程](https://github.com/kumataahh/lolly/blob/master/installations_guide.md)  


### Run 
  $ python3 face_recognition_on_raspi.py    
