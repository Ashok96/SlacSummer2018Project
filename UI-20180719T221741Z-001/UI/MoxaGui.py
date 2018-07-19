#!/usr/bin env python

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(916, 659)
        self.gridLayout = QtWidgets.QGridLayout(Form)
        self.gridLayout.setObjectName("gridLayout")
        self.pB_EXIT = QtWidgets.QPushButton(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pB_EXIT.sizePolicy().hasHeightForWidth())
        self.pB_EXIT.setSizePolicy(sizePolicy)
        self.pB_EXIT.setObjectName("pB_EXIT")
        self.gridLayout.addWidget(self.pB_EXIT, 0, 1, 1, 1)
        self.pB_BACKUP = QtWidgets.QPushButton(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pB_BACKUP.sizePolicy().hasHeightForWidth())
        self.pB_BACKUP.setSizePolicy(sizePolicy)
        self.pB_BACKUP.setObjectName("pB_BACKUP")
        self.gridLayout.addWidget(self.pB_BACKUP, 2, 1, 1, 1)
        self.pB_RESTORE = QtWidgets.QPushButton(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pB_RESTORE.sizePolicy().hasHeightForWidth())
        self.pB_RESTORE.setSizePolicy(sizePolicy)
        self.pB_RESTORE.setObjectName("pB_RESTORE")
        self.gridLayout.addWidget(self.pB_RESTORE, 2, 0, 1, 1)
        self.pB_SETUP = QtWidgets.QPushButton(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pB_SETUP.sizePolicy().hasHeightForWidth())
        self.pB_SETUP.setSizePolicy(sizePolicy)
        self.pB_SETUP.setObjectName("pB_SETUP")
        self.gridLayout.addWidget(self.pB_SETUP, 0, 0, 1, 1)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)
        self.showMaximized()

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.pB_EXIT.setText(_translate("Form", "EXIT"))
        self.pB_BACKUP.setText(_translate("Form", "BACKUP"))
        self.pB_RESTORE.setText(_translate("Form", "RESTORE"))
        self.pB_SETUP.setText(_translate("Form", "SETUP"))

