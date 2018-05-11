# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'face_recognition_4.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, face_recognition):
        face_recognition.setObjectName("face_recognition")
        face_recognition.resize(640, 480)
        self.camera_label = QtWidgets.QLabel(face_recognition)
        self.camera_label.setGeometry(QtCore.QRect(10, 9, 621, 271))
        self.camera_label.setObjectName("camera_label")
        self.label = QtWidgets.QLabel(face_recognition)
        self.label.setGeometry(QtCore.QRect(10, 324, 331, 71))
        self.label.setObjectName("label")

        self.retranslateUi(face_recognition)
        QtCore.QMetaObject.connectSlotsByName(face_recognition)

    def retranslateUi(self, face_recognition):
        _translate = QtCore.QCoreApplication.translate
        face_recognition.setWindowTitle(_translate("face_recognition", "Form"))
        self.camera_label.setText(_translate("face_recognition", "<html><head/><body><p><br/></p></body></html>"))
        self.label.setText(_translate("face_recognition", "<html><head/><body><p><span style=\" font-size:11pt; font-weight:600;\">正在核对人脸，请稍候....</span></p></body></html>"))

