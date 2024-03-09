import sys
from PyQt6.QtWidgets import *
from tercih_menu import *
from mentor_menuu import *

class WelcomeWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Hoş Geldiniz")
        self.setGeometry(200, 200, 400, 200)
        self.center()

        self.welcome_label = QLabel("                   Başarıyla giriş yaptınız!\n"
                                    "Lutfen devam etmek istediginiz islemi seciniz.")
        self.welcome_label.setObjectName("welcomeLabel")

        self.selection_window = QPushButton("Tercihler Sayfasi")
        self.selection_window.setObjectName("selectionwindowbuton")
        self.selection_window.clicked.connect(self.open_selection_window)

        self.admin_window = QPushButton("Admin Sayfasi")
        self.admin_window.setObjectName("Adminbuton")
        self.admin_window.clicked.connect(self.open_admin_window)  # Parantez kullanmıyoruz

        self.close_button = QPushButton("Kapat", self)
        self.close_button.setObjectName("closeButton2")
        self.close_button.clicked.connect(self.close_application)

        layout = QVBoxLayout()
        label_layout = QHBoxLayout()
        label_layout.addStretch()
        label_layout.addWidget(self.welcome_label)
        label_layout.addStretch()
        layout.addLayout(label_layout)

        button_layout = QHBoxLayout()
        button_layout.addWidget(self.admin_window)
        button_layout.addWidget(self.selection_window)
        button_layout.addWidget(self.close_button)
        layout.addStretch()
        layout.addLayout(button_layout)
        layout.addStretch()
        self.setLayout(layout)

        self.setStyleSheet(open("styles.qss").read())

    def open_selection_window(self):
        # Başvurular penceresini aç
        self.selection_window = SelectionWindow()  # Tercihler penceresini oluştur
        self.selection_window.show()  # Tercihler penceresini göster
        self.hide()

    def open_admin_window(self):
        # Admin penceresini aç
         pass

    def close_application(self):
        self.close()

    def center(self):
        screen_geometry = QApplication.primaryScreen().geometry()  # Ekranın geometrisini al
        x = (screen_geometry.width() - self.width()) // 2  # Pencerenin x koordinatı
        y = (screen_geometry.height() - self.height()) // 2  # Pencerenin y koordinatı
        self.move(x, y)  # Pencereyi bu koordinatlara taşı

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = WelcomeWindow()
    window.show()
    sys.exit(app.exec())
