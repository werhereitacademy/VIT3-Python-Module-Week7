import sys
import sqlite3
from PyQt6.QtWidgets import *
from tercih_admin_secimi import *



class LoginWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Giriş Sayfası")
        self.setGeometry(0, 0, 400, 200)
        self.center()
        self.username_input = QLineEdit()
        self.username_input.setStyleSheet("background-color: rgba(255, 228, 19, 50); color: blue;")
        #Kullanici adi girdigimiz yerin arka rengi,QLineEdit ile sadece yazi giriyoruz
        self.password_input = QLineEdit()
        self.password_input.setStyleSheet("background-color: rgba(255, 228, 19, 50); color: blue;")
        self.password_input.setEchoMode(QLineEdit.EchoMode.Password)
        #Echomode ile yazdigimiz yerin gozukmemesini istiyorum
        #Ben bir de sifreyi goster bolumu olsun istiyorum ne yazdigi sifreyi gorsun diye
        self.show_password_button = QPushButton("Şifreyi Göster", self)
        self.show_password_button.setObjectName("showpassword")
        self.show_password_button.clicked.connect(self.show_password_visibility)
        #show_password_visibility adinda yazdigim fonksiyonu cagiriyorum

        self.login_button = QPushButton("Giriş Yap", self)
        self.login_button.setObjectName("loginButton")
        self.login_button.clicked.connect(self.login)

        self.close_button = QPushButton("Kapat", self)
        self.close_button.setObjectName("closeButton")
        self.close_button.clicked.connect(self.close_application)

        self.status_label = QLabel()

        layout = QVBoxLayout()
        form_layout = QVBoxLayout()
        self.username_label = QLabel("Kullanıcı Adı:")
        self.username_label.setStyleSheet("color: blue;")

        form_layout.addWidget(self.username_label)
        form_layout.addWidget(self.username_input)

        self.password_label = QLabel("Şifre:")
        self.password_label.setStyleSheet("color: blue;")
        form_layout.addWidget(self.password_label)
        form_layout.addWidget(self.password_input)
        form_layout.addWidget(self.show_password_button)

        button_layout = QHBoxLayout()
        button_layout.addWidget(self.login_button)
        button_layout.addWidget(self.close_button)

        layout.addLayout(form_layout)
        layout.addLayout(button_layout)
        layout.addWidget(self.status_label)

        central_widget = QWidget()
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)

        self.connection = sqlite3.connect("users.db")
        self.cursor = self.connection.cursor()
        self.create_table()

        self.setStyleSheet(open("styles.qss").read())  # Stil dosyasını uygula
        self.username_input.returnPressed.connect(self.login)
        self.password_input.returnPressed.connect(self.login)
        #Bu şekilde, kullanıcı adı veya şifre giriş alanlarına odaklandıklarında Enter tuşuna bastıklarında login metodu otomatik olarak çağrılacaktır
    def create_table(self):
        self.cursor.execute("CREATE TABLE IF NOT EXISTS users (username TEXT, password TEXT)")

    def login(self):
        username = self.username_input.text()
        password = self.password_input.text()

        self.cursor.execute("SELECT * FROM users WHERE username=? AND password=?", (username, password))
        user = self.cursor.fetchone()

        if user:
            self.status_label.setText("Başarılı giriş!")
            self.selection_admin_window = WelcomeWindow()  # Tercihler penceresini oluştur
            self.selection_admin_window.show()  # Tercihler penceresini göster
            self.close()

        else:
            self.status_label.setText("Kullanıcı adı veya şifre hatalı")

    def close_application(self):
        self.connection.close()
        self.close()

    def show_password_visibility(self):
        if self.password_input.echoMode() == QLineEdit.EchoMode.Normal:
            self.password_input.setEchoMode(QLineEdit.EchoMode.Password)
            self.show_password_button.setText("Şifreyi Göster")
        else:
            self.password_input.setEchoMode(QLineEdit.EchoMode.Normal)
            self.show_password_button.setText("Şifreyi Gizle")

    def center(self):
        screen_geometry = QApplication.primaryScreen().geometry()  # Ekranın geometrisini al
        x = (screen_geometry.width() - self.width()) // 2  # Pencerenin x koordinatı
        y = (screen_geometry.height() - self.height()) // 2  # Pencerenin y koordinatı
        self.move(x, y)  # Pencereyi bu koordinatlara taşı

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = LoginWindow()
    window.show()
    sys.exit(app.exec())
#users.db icinde Sql kodunu yurut kisimina INSERT INTO users VALUES("Furkan Altay","1234") yazdim ve kullanici adi ekledim