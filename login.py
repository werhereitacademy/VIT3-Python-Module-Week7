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
        self.loginform = Ui_MainWindow()
        self.loginform.setupUi(self)
        self.useradminwindow_open = UserAdminPreferencePage()
        self.userprewindow_open = UserPreferencePage()

        # Herhangi bir anda Enter tusuna basinca yetki kontrolu yapmak icin kodlar
        self.loginform.lineEdit_log_password.returnPressed.connect(self.app_login)
        self.loginform.lineEdit_log_password.returnPressed.connect(self.app_login)

        # 'pushButton_log_login' butonuna tiklandiginda yetki kontrolu yapmak icin kodlar
        self.loginform.pushButton_log_login.clicked.connect(self.app_login)
        self.loginform.pushButton_log_exit.clicked.connect(self.app_exit)

    def app_login(self):
        username = self.loginform.lineEdit_log_username.text()
        password = self.loginform.lineEdit_log_password.text()
        for user in users:
            if username == user[0] and password == user[1] and user[2] == 'admin':
                self.close()
                self.useradminwindow_open.show()
            elif username == user[0] and password == user[1] and user[2] == 'user':
                self.close()
                self.userprewindow_open.show()
            else:
                self.loginform.label_log_fail.setText("\tYour email or password is incorrect.")
                self.loginform.lineEdit_log_username.setText("")
                self.loginform.lineEdit_log_password.setText("")

    def app_exit(self):
        self.close()
