from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1121, 627)
        MainWindow.setStyleSheet("background-color: white;")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.app_name = QtWidgets.QLabel(self.centralwidget)
        self.app_name.setGeometry(QtCore.QRect(0, 0, 1121, 81))
        self.app_name.setStyleSheet("font-size: 24px;\n"
"font-weight: 700;\n"
"")
        self.app_name.setAlignment(QtCore.Qt.AlignCenter)
        self.app_name.setObjectName("app_name")
        self.infor_group = QtWidgets.QWidget(self.centralwidget)
        self.infor_group.setGeometry(QtCore.QRect(310, 330, 501, 161))
        self.infor_group.setObjectName("infor_group")
        self.time_label = QtWidgets.QLabel(self.infor_group)
        self.time_label.setGeometry(QtCore.QRect(10, 110, 201, 41))
        self.time_label.setStyleSheet("\n"
"    background-color: white;\n"
"    font-size: 18px;\n"
"    font-weight: 600;\n"
"")
        self.time_label.setObjectName("time_label")
        self.id_label = QtWidgets.QLabel(self.infor_group)
        self.id_label.setGeometry(QtCore.QRect(10, 60, 201, 41))
        self.id_label.setStyleSheet("\n"
"    background-color: white;\n"
"    font-size: 18px;\n"
"    font-weight: 600;\n"
"")
        self.id_label.setObjectName("id_label")
        self.name_label = QtWidgets.QLabel(self.infor_group)
        self.name_label.setGeometry(QtCore.QRect(10, 10, 201, 41))
        self.name_label.setStyleSheet("background-color: white;\n"
"font-size: 18px;\n"
"font-weight: 600;\n"
"")
        self.name_label.setObjectName("name_label")
        self.name = QtWidgets.QLabel(self.infor_group)
        self.name.setGeometry(QtCore.QRect(210, 10, 281, 41))
        self.name.setStyleSheet("background-color: white;\n"
"font-size: 18px;\n"
"font-weight: 600;\n"
"")
        self.name.setObjectName("name")
        self.id = QtWidgets.QLabel(self.infor_group)
        self.id.setGeometry(QtCore.QRect(210, 60, 281, 41))
        self.id.setStyleSheet("    background-color: white;\n"
"    font-size: 18px;\n"
"    font-weight: 600;\n"
"")
        self.id.setObjectName("id")
        self.time = QtWidgets.QLabel(self.infor_group)
        self.time.setGeometry(QtCore.QRect(210, 110, 281, 41))
        self.time.setStyleSheet("\n"
"    background-color: white;\n"
"    font-size: 18px;\n"
"    font-weight: 600;\n"
"")
        self.time.setObjectName("time")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(470, 90, 181, 171))
        self.label.setStyleSheet("background-color: white;\n"
"border-raduis: 50px;    \n"
"")
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap(".\\assets\\design\\../media/finger_print.png"))
        self.label.setScaledContents(True)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setWordWrap(False)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(420, 270, 281, 21))
        self.label_2.setStyleSheet("color: red;")
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.infor_group.raise_()
        self.app_name.raise_()
        self.label.raise_()
        self.label_2.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.menuBar = QtWidgets.QMenuBar(MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 1121, 26))
        self.menuBar.setObjectName("menuBar")
        self.menu_setting = QtWidgets.QMenu(self.menuBar)
        self.menu_setting.setObjectName("menu_setting")
        self.menu_gsp = QtWidgets.QMenu(self.menu_setting)
        self.menu_gsp.setObjectName("menu_gsp")
        self.help = QtWidgets.QMenu(self.menuBar)
        self.help.setObjectName("help")
        self.menu_tools = QtWidgets.QMenu(self.menuBar)
        self.menu_tools.setTearOffEnabled(False)
        self.menu_tools.setObjectName("menu_tools")
        MainWindow.setMenuBar(self.menuBar)
        self.menu_com_port = QtWidgets.QAction(MainWindow)
        self.menu_com_port.setObjectName("menu_com_port")
        self.menu_auth_key = QtWidgets.QAction(MainWindow)
        self.menu_auth_key.setObjectName("menu_auth_key")
        self.menu_email = QtWidgets.QAction(MainWindow)
        self.menu_email.setObjectName("menu_email")
        self.menu_exit = QtWidgets.QAction(MainWindow)
        self.menu_exit.setCheckable(False)
        self.menu_exit.setObjectName("menu_exit")
        self.actionB_o_l_i = QtWidgets.QAction(MainWindow)
        self.actionB_o_l_i.setObjectName("actionB_o_l_i")
        self.actionLi_n_h = QtWidgets.QAction(MainWindow)
        self.actionLi_n_h.setObjectName("actionLi_n_h")
        self.menu_tutorial = QtWidgets.QAction(MainWindow)
        self.menu_tutorial.setObjectName("menu_tutorial")
        self.menu_bug = QtWidgets.QAction(MainWindow)
        self.menu_bug.setObjectName("menu_bug")
        self.menu_contact = QtWidgets.QAction(MainWindow)
        self.menu_contact.setObjectName("menu_contact")
        self.menu_gsp.addAction(self.menu_auth_key)
        self.menu_gsp.addAction(self.menu_email)
        self.menu_setting.addAction(self.menu_com_port)
        self.menu_setting.addAction(self.menu_gsp.menuAction())
        self.help.addAction(self.menu_tutorial)
        self.help.addAction(self.menu_bug)
        self.help.addAction(self.menu_contact)
        self.menu_tools.addAction(self.menu_exit)
        self.menuBar.addAction(self.menu_tools.menuAction())
        self.menuBar.addAction(self.menu_setting.menuAction())
        self.menuBar.addAction(self.help.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.app_name.setText(_translate("MainWindow", "HỆ THỐNG ĐIỂM DANH BẰNG VÂN TAY"))
        self.time_label.setText(_translate("MainWindow", "Thời gian điểm danh"))
        self.id_label.setText(_translate("MainWindow", "Mã sinh viên"))
        self.name_label.setText(_translate("MainWindow", "Họ và tên"))
        self.name.setText(_translate("MainWindow", ": Nguyễn Quỳnh Anh Nhung"))
        self.id.setText(_translate("MainWindow", ": B22DCCN888"))
        self.time.setText(_translate("MainWindow", ": 14:24:13"))
        self.label_2.setText(_translate("MainWindow", "Vui lòng đặt ngón tay vào cảm biến!"))
        self.menu_setting.setTitle(_translate("MainWindow", "Cài đặt"))
        self.menu_gsp.setTitle(_translate("MainWindow", "Thiết lập Google Sheet"))
        self.help.setTitle(_translate("MainWindow", "Trợ giúp"))
        self.menu_tools.setTitle(_translate("MainWindow", "Công cụ"))
        self.menu_com_port.setText(_translate("MainWindow", "Cổng kết nối (COM)"))
        self.menu_auth_key.setText(_translate("MainWindow", "Authentication key"))
        self.menu_email.setText(_translate("MainWindow", "Email"))
        self.menu_exit.setText(_translate("MainWindow", "Thoát"))
        self.actionB_o_l_i.setText(_translate("MainWindow", "Báo lỗi"))
        self.actionLi_n_h.setText(_translate("MainWindow", "Liên hệ"))
        self.menu_tutorial.setText(_translate("MainWindow", "Hướng dẫn sử dụng"))
        self.menu_bug.setText(_translate("MainWindow", "Báo lỗi"))
        self.menu_contact.setText(_translate("MainWindow", "Liên hệ"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
