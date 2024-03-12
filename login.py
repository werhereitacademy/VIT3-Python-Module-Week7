from PyQt6.QtWidgets import QMainWindow
from PyQt6 import QtCore
import gspread


from login_ui import Ui_MainWindow
from user_admin_preference import UserAdminPreferencePage
from user_preference import UserPreferencePage

credentials = 'key.json'
gc = gspread.service_account(filename=credentials)
spreadsheet_users = gc.open('Kullanicilar')
worksheet_users = spreadsheet_users.get_worksheet(0)
users = worksheet_users.get_all_values()
users.pop(0)


class LoginPage(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowFlags(QtCore.Qt.WindowType.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WidgetAttribute.WA_TranslucentBackground)
        self.loginForm = Ui_MainWindow()
        self.loginForm.setupUi(self)
        self.useradminwindow_open = UserAdminPreferencePage()
        self.userprewindow_open = UserPreferencePage()

        # Herhangi bir anda Enter tusuna basinca yetki kontrolu yapmak icin kodlar
        self.loginForm.lineEdit_password.returnPressed.connect(self.app_login)
        self.loginForm.lineEdit_password.returnPressed.connect(self.app_login)

        # 'pushButton_log_login' butonuna tiklandiginda yetki kontrolu yapmak icin kodlar
        self.loginForm.pushButton_login.clicked.connect(self.app_login)
        self.loginForm.pushButton_exit.clicked.connect(self.app_exit)

    def app_login(self):
        username = self.loginForm.lineEdit_username.text()
        password = self.loginForm.lineEdit_password.text()
        for user in users:
            if username == user[0] and password == user[1] and user[2] == 'admin':
                self.close()
                self.useradminwindow_open.show()
            elif username == user[0] and password == user[1] and user[2] == 'user':
                self.close()
                self.userprewindow_open.show()
            else:
                self.loginForm.label_fail.setText("\tYour email or password is incorrect.")
                self.loginForm.lineEdit_username.setText("")
                self.loginForm.lineEdit_password.setText("")

    def app_exit(self):
        self.close()
