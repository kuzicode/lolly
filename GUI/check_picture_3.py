# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'check_picture_3.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(640, 480)
        self.user_picture = QtWidgets.QLabel(Form)
        self.user_picture.setGeometry(QtCore.QRect(10, 9, 621, 301))
        self.user_picture.setText("")
        self.user_picture.setObjectName("user_picture")
        self.horizontalLayoutWidget = QtWidgets.QWidget(Form)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(180, 410, 261, 61))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.no = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.no.setMinimumSize(QtCore.QSize(0, 28))
        self.no.setObjectName("no")
        self.horizontalLayout.addWidget(self.no, 0, QtCore.Qt.AlignVCenter)
        self.yes = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.yes.setObjectName("yes")
        self.horizontalLayout.addWidget(self.yes)
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(10, 370, 281, 41))
        self.label_2.setObjectName("label_2")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.no.setText(_translate("Form", "重拍"))
        self.yes.setText(_translate("Form", "确认"))
        self.label_2.setText(_translate("Form", "<html><head/><body><p><span style=\" font-size:12pt;\">请核对照片，重拍或者点击确认进入下一步</span></p></body></html>"))

