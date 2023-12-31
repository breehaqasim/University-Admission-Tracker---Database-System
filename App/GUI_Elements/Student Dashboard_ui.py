# Form implementation generated from reading ui file 'c:\Users\Tech Brand Store\Desktop\breeha db\Database Project\GUI_Elements\Student Dashboard.ui'
#
# Created by: PyQt6 UI code generator 6.5.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(580, 391)
        MainWindow.setStyleSheet("QMainWindow { \n"
"    border-image: url(GUI_Elements/bg image.png);\n"
"}\n"
"QLabel {\n"
"  color: #464d55;\n"
"  font-weight: 600;\n"
"}\n"
"QLabel#heading {\n"
"  color: #0f1925;\n"
"  font-size: 18px;\n"
"  margin-bottom: 10px;\n"
"}\n"
"\n"
"QLabel#subheading {\n"
"  color: #0f1925;\n"
"  font-size: 12px;\n"
"  font-weight: normal;\n"
"  margin-bottom: 10px;\n"
"}\n"
"QLineEdit {\n"
"  background: transparent;\n"
"  color: rgb(86, 86, 86);\n"
"  border-bottom: 1px solid rgb(86, 86, 86);\n"
"}\n"
"\n"
"QPushButton {\n"
"  background-color: #00557f;\n"
"  color: #0f1925;\n"
"  font-weight: 600;\n"
"  border-radius: 8px;\n"
"  border: 1px solid #00557f;\n"
"  padding: 5px 15px;\n"
"  margin-top: 10px;\n"
"  outline: 0px;\n"
"}\n"
"QPushButton:hover,\n"
"QPushButton:focus {\n"
"  background-color: #85E3D9;\n"
"  border: 3px solid #85E3D9;\n"
"}\n"
"")
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label_9 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(470, 0, 181, 181))
        self.label_9.setStyleSheet("image: url(GUI_Elements/2.png);")
        self.label_9.setText("")
        self.label_9.setObjectName("label_9")
        self.label = QtWidgets.QLabel(parent=self.centralwidget)
        self.label.setGeometry(QtCore.QRect(-50, -10, 371, 301))
        self.label.setStyleSheet("image: url(GUI_Elements/5.png);")
        self.label.setText("")
        self.label.setObjectName("label")
        self.frame_2 = QtWidgets.QFrame(parent=self.centralwidget)
        self.frame_2.setGeometry(QtCore.QRect(-10, -20, 601, 71))
        self.frame_2.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-radius: 8px;")
        self.frame_2.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_2.setObjectName("frame_2")
        self.label_8 = QtWidgets.QLabel(parent=self.frame_2)
        self.label_8.setGeometry(QtCore.QRect(10, 20, 61, 51))
        self.label_8.setStyleSheet("\n"
"image: url(GUI_Elements/DB Project.png);")
        self.label_8.setText("")
        self.label_8.setObjectName("label_8")
        self.pushButton = QtWidgets.QPushButton(parent=self.frame_2)
        self.pushButton.setGeometry(QtCore.QRect(200, 20, 121, 41))
        self.pushButton.setStyleSheet("QPushButton:hover,\n"
"QPushButton:focus {\n"
"    \n"
"  color: rgb(255, 255, 255);\n"
"  background-color: #85E3D9;\n"
"  border: 3px solid #85E3D9;\n"
"}")
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(parent=self.frame_2)
        self.pushButton_2.setGeometry(QtCore.QRect(330, 20, 141, 41))
        self.pushButton_2.setStyleSheet("QPushButton:hover,\n"
"QPushButton:focus {\n"
"    \n"
"  color: rgb(255, 255, 255);\n"
"  background-color: #85E3D9;\n"
"  border: 3px solid #85E3D9;\n"
"}")
        self.pushButton_2.setObjectName("pushButton_2")
        self.label_3 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(40, 130, 191, 41))
        self.label_3.setStyleSheet("\n"
"font: 75 24pt \"MS Shell Dlg 2\";\n"
"color: rgb(255, 255, 255);")
        self.label_3.setObjectName("label_3")
        self.label_10 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_10.setGeometry(QtCore.QRect(40, 170, 191, 41))
        self.label_10.setStyleSheet("\n"
"font: 75 24pt \"MS Shell Dlg 2\";\n"
"color: rgb(133, 227, 217);")
        self.label_10.setObjectName("label_10")
        self.label_11 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_11.setGeometry(QtCore.QRect(150, 170, 191, 41))
        self.label_11.setStyleSheet("\n"
"font: 75 24pt \"MS Shell Dlg 2\";\n"
"color: rgb(255, 255, 255);")
        self.label_11.setObjectName("label_11")
        self.label_12 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_12.setGeometry(QtCore.QRect(40, 210, 191, 41))
        self.label_12.setStyleSheet("\n"
"font: 75 24pt \"MS Shell Dlg 2\";\n"
"color: rgb(255, 255, 255);")
        self.label_12.setObjectName("label_12")
        self.label_13 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_13.setGeometry(QtCore.QRect(140, 50, 521, 421))
        self.label_13.setStyleSheet("image: url(GUI_Elements/graduation.png);")
        self.label_13.setText("")
        self.label_13.setObjectName("label_13")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 580, 18))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Student Dashboard"))
        self.pushButton.setText(_translate("MainWindow", "SEARCH UNIVERSITY"))
        self.pushButton_2.setText(_translate("MainWindow", "CONTACT COUNSELLORS"))
        self.label_3.setText(_translate("MainWindow", "Your Perfect "))
        self.label_10.setText(_translate("MainWindow", "University"))
        self.label_11.setText(_translate("MainWindow", "Is"))
        self.label_12.setText(_translate("MainWindow", "Waiting for You!"))
