# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'PianyuanAboutUs.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets



class Ui_WindowAboutUs(object):
    def setupUi(self, WindowAboutUs):
        WindowAboutUs.setObjectName("WindowAboutUs")
        WindowAboutUs.resize(253, 178)
        self.centralwidget = QtWidgets.QWidget(WindowAboutUs)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(50, 30, 121, 51))
        self.label.setObjectName("label")
        WindowAboutUs.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(WindowAboutUs)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 253, 18))
        self.menubar.setObjectName("menubar")
        WindowAboutUs.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(WindowAboutUs)
        self.statusbar.setObjectName("statusbar")
        WindowAboutUs.setStatusBar(self.statusbar)

        self.retranslateUi(WindowAboutUs)
        QtCore.QMetaObject.connectSlotsByName(WindowAboutUs)

    def retranslateUi(self, WindowAboutUs):
        _translate = QtCore.QCoreApplication.translate
        WindowAboutUs.setWindowTitle(_translate("WindowAboutUs", "关于我们"))
        self.label.setText(_translate("WindowAboutUs", "这里可以写点个人信息"))
