# Form implementation generated from reading ui file 'c:\Users\Tech Brand Store\Desktop\breeha db\Database Project\GUI_Elements\Admin Dashboard.ui'
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
        self.pushButton.setGeometry(QtCore.QRect(420, 20, 121, 41))
        self.pushButton.setStyleSheet("QPushButton:hover,\n"
"QPushButton:focus {\n"
"    \n"
"  color: rgb(255, 255, 255);\n"
"  background-color: #85E3D9;\n"
"  border: 3px solid #85E3D9;\n"
"}")
        self.pushButton.setObjectName("pushButton")
        self.frame = QtWidgets.QFrame(parent=self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(10, 70, 561, 271))
        self.frame.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-radius: 8px;")
        self.frame.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame.setObjectName("frame")
        self.label_3 = QtWidgets.QLabel(parent=self.frame)
        self.label_3.setGeometry(QtCore.QRect(20, 20, 171, 20))
        self.label_3.setStyleSheet("font: 75 16pt \"MS Shell Dlg 2\";\n"
"\n"
"color: rgb(86, 86, 86);")
        self.label_3.setObjectName("label_3")
        self.lineEdit = QtWidgets.QLineEdit(parent=self.frame)
        self.lineEdit.setEnabled(False)
        self.lineEdit.setGeometry(QtCore.QRect(120, 60, 121, 21))
        self.lineEdit.setStyleSheet("background:transparent;")
        self.lineEdit.setPlaceholderText("")
        self.lineEdit.setObjectName("lineEdit")
        self.label_4 = QtWidgets.QLabel(parent=self.frame)
        self.label_4.setGeometry(QtCore.QRect(20, 60, 101, 20))
        self.label_4.setStyleSheet("font: 75 8pt \"MS Shell Dlg 2\";\n"
"color: rgb(86, 86, 86);")
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(parent=self.frame)
        self.label_5.setGeometry(QtCore.QRect(20, 90, 111, 20))
        self.label_5.setStyleSheet("font: 75 8pt \"MS Shell Dlg 2\";\n"
"color: rgb(86, 86, 86);")
        self.label_5.setObjectName("label_5")
        self.lineEdit_5 = QtWidgets.QLineEdit(parent=self.frame)
        self.lineEdit_5.setEnabled(False)
        self.lineEdit_5.setGeometry(QtCore.QRect(120, 200, 121, 21))
        self.lineEdit_5.setStyleSheet("background:transparent;")
        self.lineEdit_5.setPlaceholderText("")
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.lineEdit_6 = QtWidgets.QLineEdit(parent=self.frame)
        self.lineEdit_6.setEnabled(False)
        self.lineEdit_6.setGeometry(QtCore.QRect(120, 230, 121, 21))
        self.lineEdit_6.setStyleSheet("background:transparent;")
        self.lineEdit_6.setPlaceholderText("")
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.label_7 = QtWidgets.QLabel(parent=self.frame)
        self.label_7.setGeometry(QtCore.QRect(20, 120, 81, 20))
        self.label_7.setStyleSheet("font: 75 8pt \"MS Shell Dlg 2\";\n"
"color: rgb(86, 86, 86);")
        self.label_7.setObjectName("label_7")
        self.lineEdit_7 = QtWidgets.QLineEdit(parent=self.frame)
        self.lineEdit_7.setEnabled(False)
        self.lineEdit_7.setGeometry(QtCore.QRect(350, 60, 151, 21))
        self.lineEdit_7.setStyleSheet("background:transparent;")
        self.lineEdit_7.setPlaceholderText("")
        self.lineEdit_7.setObjectName("lineEdit_7")
        self.label_10 = QtWidgets.QLabel(parent=self.frame)
        self.label_10.setGeometry(QtCore.QRect(20, 160, 121, 20))
        self.label_10.setStyleSheet("font: 75 8pt \"MS Shell Dlg 2\";\n"
"color: rgb(86, 86, 86);")
        self.label_10.setObjectName("label_10")
        self.label_11 = QtWidgets.QLabel(parent=self.frame)
        self.label_11.setGeometry(QtCore.QRect(20, 200, 81, 20))
        self.label_11.setStyleSheet("font: 75 8pt \"MS Shell Dlg 2\";\n"
"color: rgb(86, 86, 86);")
        self.label_11.setObjectName("label_11")
        self.lineEdit_12 = QtWidgets.QLineEdit(parent=self.frame)
        self.lineEdit_12.setEnabled(False)
        self.lineEdit_12.setGeometry(QtCore.QRect(180, 300, 101, 21))
        self.lineEdit_12.setStyleSheet("background:transparent;")
        self.lineEdit_12.setText("")
        self.lineEdit_12.setPlaceholderText("")
        self.lineEdit_12.setObjectName("lineEdit_12")
        self.label_16 = QtWidgets.QLabel(parent=self.frame)
        self.label_16.setGeometry(QtCore.QRect(30, 330, 121, 20))
        self.label_16.setStyleSheet("font: 75 8pt \"MS Shell Dlg 2\";\n"
"color: rgb(86, 86, 86);")
        self.label_16.setObjectName("label_16")
        self.lineEdit_13 = QtWidgets.QLineEdit(parent=self.frame)
        self.lineEdit_13.setEnabled(False)
        self.lineEdit_13.setGeometry(QtCore.QRect(180, 330, 101, 21))
        self.lineEdit_13.setStyleSheet("background:transparent;")
        self.lineEdit_13.setText("")
        self.lineEdit_13.setPlaceholderText("")
        self.lineEdit_13.setObjectName("lineEdit_13")
        self.lineEdit_14 = QtWidgets.QLineEdit(parent=self.frame)
        self.lineEdit_14.setEnabled(False)
        self.lineEdit_14.setGeometry(QtCore.QRect(180, 270, 101, 21))
        self.lineEdit_14.setStyleSheet("background:transparent;")
        self.lineEdit_14.setText("")
        self.lineEdit_14.setPlaceholderText("")
        self.lineEdit_14.setObjectName("lineEdit_14")
        self.lineEdit_2 = QtWidgets.QLineEdit(parent=self.frame)
        self.lineEdit_2.setEnabled(False)
        self.lineEdit_2.setGeometry(QtCore.QRect(120, 90, 121, 21))
        self.lineEdit_2.setStyleSheet("background:transparent;")
        self.lineEdit_2.setText("")
        self.lineEdit_2.setPlaceholderText("")
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.label_15 = QtWidgets.QLabel(parent=self.frame)
        self.label_15.setGeometry(QtCore.QRect(30, 300, 121, 20))
        self.label_15.setStyleSheet("font: 75 8pt \"MS Shell Dlg 2\";\n"
"color: rgb(86, 86, 86);")
        self.label_15.setObjectName("label_15")
        self.lineEdit_3 = QtWidgets.QLineEdit(parent=self.frame)
        self.lineEdit_3.setEnabled(False)
        self.lineEdit_3.setGeometry(QtCore.QRect(120, 120, 121, 21))
        self.lineEdit_3.setStyleSheet("background:transparent;")
        self.lineEdit_3.setPlaceholderText("")
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.lineEdit_4 = QtWidgets.QLineEdit(parent=self.frame)
        self.lineEdit_4.setEnabled(False)
        self.lineEdit_4.setGeometry(QtCore.QRect(120, 160, 121, 21))
        self.lineEdit_4.setStyleSheet("background:transparent;")
        self.lineEdit_4.setPlaceholderText("")
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.label_12 = QtWidgets.QLabel(parent=self.frame)
        self.label_12.setGeometry(QtCore.QRect(20, 230, 91, 20))
        self.label_12.setStyleSheet("font: 75 8pt \"MS Shell Dlg 2\";\n"
"color: rgb(86, 86, 86);")
        self.label_12.setObjectName("label_12")
        self.label_13 = QtWidgets.QLabel(parent=self.frame)
        self.label_13.setGeometry(QtCore.QRect(270, 70, 71, 20))
        self.label_13.setStyleSheet("font: 75 8pt \"MS Shell Dlg 2\";\n"
"color: rgb(86, 86, 86);")
        self.label_13.setObjectName("label_13")
        self.label_14 = QtWidgets.QLabel(parent=self.frame)
        self.label_14.setGeometry(QtCore.QRect(270, 100, 71, 20))
        self.label_14.setStyleSheet("font: 75 8pt \"MS Shell Dlg 2\";\n"
"color: rgb(86, 86, 86);")
        self.label_14.setObjectName("label_14")
        self.lineEdit_8 = QtWidgets.QLineEdit(parent=self.frame)
        self.lineEdit_8.setEnabled(False)
        self.lineEdit_8.setGeometry(QtCore.QRect(350, 100, 151, 21))
        self.lineEdit_8.setStyleSheet("background:transparent;")
        self.lineEdit_8.setText("")
        self.lineEdit_8.setPlaceholderText("")
        self.lineEdit_8.setObjectName("lineEdit_8")
        self.lineEdit_9 = QtWidgets.QLineEdit(parent=self.frame)
        self.lineEdit_9.setEnabled(False)
        self.lineEdit_9.setGeometry(QtCore.QRect(350, 140, 151, 21))
        self.lineEdit_9.setStyleSheet("background:transparent;")
        self.lineEdit_9.setText("")
        self.lineEdit_9.setPlaceholderText("")
        self.lineEdit_9.setObjectName("lineEdit_9")
        self.lineEdit_10 = QtWidgets.QLineEdit(parent=self.frame)
        self.lineEdit_10.setEnabled(False)
        self.lineEdit_10.setGeometry(QtCore.QRect(350, 180, 151, 21))
        self.lineEdit_10.setStyleSheet("background:transparent;")
        self.lineEdit_10.setText("")
        self.lineEdit_10.setPlaceholderText("")
        self.lineEdit_10.setObjectName("lineEdit_10")
        self.label_17 = QtWidgets.QLabel(parent=self.frame)
        self.label_17.setGeometry(QtCore.QRect(270, 140, 71, 20))
        self.label_17.setStyleSheet("font: 75 8pt \"MS Shell Dlg 2\";\n"
"color: rgb(86, 86, 86);")
        self.label_17.setObjectName("label_17")
        self.label_18 = QtWidgets.QLabel(parent=self.frame)
        self.label_18.setGeometry(QtCore.QRect(270, 180, 71, 20))
        self.label_18.setStyleSheet("font: 75 8pt \"MS Shell Dlg 2\";\n"
"color: rgb(86, 86, 86);")
        self.label_18.setObjectName("label_18")
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
        self.pushButton.setText(_translate("MainWindow", "EDIT NOW"))
        self.label_3.setText(_translate("MainWindow", "University Details"))
        self.lineEdit.setText(_translate("MainWindow", "Habib"))
        self.label_4.setText(_translate("MainWindow", "University Name"))
        self.label_5.setText(_translate("MainWindow", "Location"))
        self.lineEdit_5.setText(_translate("MainWindow", "1500"))
        self.lineEdit_6.setText(_translate("MainWindow", "100,000"))
        self.label_7.setText(_translate("MainWindow", "University Type"))
        self.lineEdit_7.setText(_translate("MainWindow", "BS Computer Science 4 Years"))
        self.label_10.setText(_translate("MainWindow", "Entry Test Type"))
        self.label_11.setText(_translate("MainWindow", "SAT Score Required"))
        self.label_16.setText(_translate("MainWindow", "Program 4"))
        self.label_15.setText(_translate("MainWindow", "Program 3"))
        self.lineEdit_3.setText(_translate("MainWindow", "Private"))
        self.lineEdit_4.setText(_translate("MainWindow", "SAT"))
        self.label_12.setText(_translate("MainWindow", "Average Annual Cost"))
        self.label_13.setText(_translate("MainWindow", "Program 1"))
        self.label_14.setText(_translate("MainWindow", "Program 2"))
        self.label_17.setText(_translate("MainWindow", "Program 3"))
        self.label_18.setText(_translate("MainWindow", "Program 4"))
