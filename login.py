from PyQt6.QtWidgets import*
from login_bak import Ui_MainWindow
from user_admin_preference import UserAdminPreferencePage
from user_preference import UserPreferencePage
from PyQt6.QtWidgets import QMainWindow
from PyQt6 import uic, QtCore

class LoginPage(QMainWindow):
    def __init__(self) :
        super().__init__()
        self.setWindowFlags(QtCore.Qt.WindowType.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WidgetAttribute.WA_TranslucentBackground)
        self.loginform = Ui_MainWindow()
        self.loginform.setupUi(self)
        self.useradminwindow_open = UserAdminPreferencePage()
        self.userprewindow_open = UserPreferencePage()
        self.loginform.pushButton_log_login.clicked.connect(self.log_in)
        self.loginform.pushButton_log_exit.clicked.connect(self.log_exit)
        


    def log_exit(self):
        self.close()

    def log_in(self):
        username = self.loginform.lineEdit_log_username.text()   
        password = self.loginform.lineEdit_log_password.text()  
        if username == "a" and password == "1":
            self.close()
            self.useradminwindow_open.show()
        elif username == "u" and password == "2":
            self.close()
            self.userprewindow_open.show() 
        else:
            self.loginform.label_log_fail.setText("\tYour email or password is incorrect.")
            self.loginform.lineEdit_log_username.setText("")
            self.loginform.lineEdit_log_password.setText("")
            


            
        
    

                   
                



            
        
        

            
        
                
