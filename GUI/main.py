import sys,cv2,time,requests
from PyQt5 import QtGui
from PyQt5.QtWidgets import QApplication,QWidget,QLabel
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import QTimer,QBasicTimer,Qt

from set_user_1 import Ui_Form as Set_User
from open_camera_2 import Ui_Form as Open_Camera
from check_picture_3 import Ui_Form as Check_Picture
from face_recognition_4 import Ui_Form as Face_Recognition


USER_NAME='1'


class SetUser(QWidget,Set_User):
    def __init__(self,next_window):
        super().__init__()
        self.setupUi(self)
        self.slot_init()

        self.next_window=next_window

    #跳转到第二个摄像头界面
    def turn_to_camera(self):
        global USER_NAME
        USER_NAME=self.lineEdit.text()
        print(USER_NAME)
        self.close()
        self.next_window.show_window()


    def enter_again(self):
        USER_NAME=''
        self.lineEdit.clear()

    def slot_init(self):
        self.yes.clicked.connect(self.turn_to_camera)
        self.no.clicked.connect(self.enter_again)


class OpenCamera(QWidget,Open_Camera):
    def __init__(self,next_window=None):
        super().__init__()
        self.setupUi(self)
        self.slot_init()

        self.value=0
        # self.number_of_pic=1
        self.next_window=next_window


    def slot_init(self):
        self.cap=cv2.VideoCapture()
        self.timer_camera=QTimer()
        self.cap.open(0)


        self.timer_camera.timeout.connect(self.show_camera)
        self.timer_camera.timeout.connect(self.set_pbar_value)

    def show_window(self):
        self.show()			
        self.timer_camera.start(5)

    def closed_window(self):
        self.timer_camera.stop()
        self.cap.release()
        self.close()
        cv2.destroyAllWindows()

    def show_camera(self):
        flag, self.image = self.cap.read()

        show = cv2.resize(self.image, (640, 480))
        show = cv2.cvtColor(show, cv2.COLOR_BGR2RGB)
        showImage = QtGui.QImage(show.data, show.shape[1], show.shape[0], QtGui.QImage.Format_RGB888)
        self.label_show_camera.setPixmap(QtGui.QPixmap.fromImage(showImage))

    def set_pbar_value(self):
        self.value+=1
        self.pbar.setValue(self.value)

        cv2.imwrite('%s.jpg'%(USER_NAME),self.image)

        #进度条满100，跳转到下一个窗口
        if self.value==100:
            self.closed_window()
            if self.next_window:
                self.next_window.show_window()

class CheckPicture(QWidget,Check_Picture):
    def __init__(self):
        # self.nex_window=next_window
        self.last_window=OpenCamera()
        super().__init__()
        self.setupUi(self)

        self.slot_init()

    def slot_init(self):
        # self.set_picture()
        self.no.clicked.connect(lambda :self.show_last_window())
        self.yes.clicked.connect(lambda :self.closed_window())

    def closed_window(self):
        self.close()
    def show_window(self):
        self.show()
        self.set_picture()

    def set_picture(self):
        global USER_NAME
        pixmap=QPixmap('%s.jpg'%USER_NAME)
        self.user_picture.setPixmap(pixmap)

    def show_last_window(self):
        self.close()
        self.last_window.show_window()


    def show_next_window(self):
        self.close()
        self.nex_window.show_window()
class FaceRecognition(QWidget,Face_Recognition):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.slot_init()

        self.value=0

    def slot_init(self):
        self.cap=cv2.VideoCapture()
        self.timer_camera=QTimer()
        self.cap.open(0)

        self.timer_camera.timeout.connect(self.show_camera)
        self.face_compare()

    def keyPressEvent(self, e):
        if e.key() == Qt.Key_Escape:
            self.closed_window()

    def show_window(self):
        self.show()
        self.timer_camera.start(5)

    def closed_window(self):
        self.timer_camera.stop()
        self.cap.release()
        self.close()

    def show_camera(self):
        n=1
        flag, self.image = self.cap.read()

        show = cv2.resize(self.image, (640, 480))


        if n==5:
            cv2.imwrite('temp.jpg',self.image)
        show = cv2.cvtColor(show, cv2.COLOR_BGR2RGB)
        showImage = QtGui.QImage(show.data, show.shape[1], show.shape[0], QtGui.QImage.Format_RGB888)
        self.camera_label.setPixmap(QtGui.QPixmap.fromImage(showImage))

        n+=1


    def face_recognition(self,pic_1, pic_2):
        '''
        上传本地的两个图片，用于识别是否是同一个人(人脸识别)
        :pic_1,pic_2: local picture path
        :rtype:json
        '''
        url = 'https://api-cn.faceplusplus.com/facepp/v3/compare'

        data = {
            'api_key': 'ku-OGYH-G5ohgFtogUbox5rT0RHtNJK6',
            'api_secret': 'ZGmzUzNJPDUP-J4UDmr4JEnq89h6zxSI'}
        files = {'image_file1': open(pic_1, 'rb'), 'image_file2': open(pic_2, 'rb')}

        r = requests.post(url, data=data, files=files)
        # print(msg)
        if r.status_code == requests.codes.ok:
            # print(r.json()['confidence'])
            return r.json()['confidence']
        else:
            return 'something wrong and status_code is %s' % r.status_code

    # def face_compare(self):
    #     global USER_NAME
    #
    #     msg=self.face_recognition('%s.jpg'%USER_NAME,'temp.jpg')
    #     print(msg)
    #     self.label.setText(msg)



if __name__=='__main__':
    app=QApplication(sys.argv)

    w3=CheckPicture()
    # # w3.show()
    w2=OpenCamera(w3)
    w1=SetUser(w2)
    w1.show()
    # w4=FaceRecognition()
    # w4.show_window()
    # w4.label.setText('hello')

    sys.exit(app.exec_())