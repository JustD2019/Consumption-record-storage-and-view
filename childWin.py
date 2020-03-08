# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'childWin.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(637, 303)
        self.type_input1 = QtWidgets.QLineEdit(Dialog)
        self.type_input1.setGeometry(QtCore.QRect(60, 70, 81, 31))
        self.type_input1.setFocusPolicy(QtCore.Qt.NoFocus)
        self.type_input1.setObjectName("type_input1")
        self.type_input3 = QtWidgets.QLineEdit(Dialog)
        self.type_input3.setGeometry(QtCore.QRect(60, 150, 421, 31))
        self.type_input3.setObjectName("type_input3")
        self.type_input2 = QtWidgets.QLineEdit(Dialog)
        self.type_input2.setGeometry(QtCore.QRect(170, 70, 81, 31))
        self.type_input2.setFocusPolicy(QtCore.Qt.NoFocus)
        self.type_input2.setObjectName("type_input2")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(60, 30, 171, 31))
        font = QtGui.QFont()
        font.setFamily("方正粗黑宋简体")
        font.setPointSize(14)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_5 = QtWidgets.QLabel(Dialog)
        self.label_5.setGeometry(QtCore.QRect(60, 110, 441, 31))
        font = QtGui.QFont()
        font.setFamily("方正粗黑宋简体")
        font.setPointSize(14)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.widget = QtWidgets.QWidget(Dialog)
        self.widget.setGeometry(QtCore.QRect(60, 200, 238, 36))
        self.widget.setObjectName("widget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(50)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.save_type_btn = QtWidgets.QPushButton(self.widget)
        font = QtGui.QFont()
        font.setFamily("方正粗黑宋简体")
        font.setPointSize(12)
        self.save_type_btn.setFont(font)
        self.save_type_btn.setObjectName("save_type_btn")
        self.horizontalLayout.addWidget(self.save_type_btn)
        self.clear_btn = QtWidgets.QPushButton(self.widget)
        font = QtGui.QFont()
        font.setFamily("方正粗黑宋简体")
        font.setPointSize(12)
        self.clear_btn.setFont(font)
        self.clear_btn.setObjectName("clear_btn")
        self.horizontalLayout.addWidget(self.clear_btn)
        self.horizontalLayout.setStretch(0, 1)
        self.horizontalLayout.setStretch(1, 1)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "自定义列名"))
        self.type_input1.setText(_translate("Dialog", "消费日期"))
        self.type_input2.setText(_translate("Dialog", "消费总额"))
        self.label.setText(_translate("Dialog", "前两列固定名"))
        self.label_5.setText(_translate("Dialog", "请输入您需要定义的列名，以空格分隔！"))
        self.save_type_btn.setText(_translate("Dialog", "存储"))
        self.clear_btn.setText(_translate("Dialog", "清空"))
