# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'open_camera_2.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(640, 480)
        self.label_show_camera = QtWidgets.QLabel(Form)
        self.label_show_camera.setGeometry(QtCore.QRect(10, 19, 621, 361))
        self.label_show_camera.setText("")
        self.label_show_camera.setObjectName("label_show_camera")
        self.infos_label = QtWidgets.QLabel(Form)
        self.infos_label.setGeometry(QtCore.QRect(10, 380, 291, 51))
        self.infos_label.setObjectName("infos_label")
        self.pbar = QtWidgets.QProgressBar(Form)
        self.pbar.setGeometry(QtCore.QRect(10, 430, 621, 41))
        self.pbar.setProperty("value", 24)
        self.pbar.setObjectName("pbar")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.infos_label.setText(_translate("Form", "正在信息采集阶段，请稍等..."))

