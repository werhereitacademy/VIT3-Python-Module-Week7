import sys
from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QHBoxLayout, QVBoxLayout
from PyQt6.QtGui import QPixmap
from PyQt6.QtCore import Qt



class SelectionWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Hoş Geldiniz")
        self.setGeometry(400, 600, 600, 200)
        self.center()

        self.image_label = QLabel()
        pixmap = QPixmap("logo-1.png")
        self.image_label.setPixmap(pixmap)
        self.image_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.applications_window = QPushButton("Başvurular")
        self.applications_window.setObjectName("Applicationsbuton")
        self.applications_window.clicked.connect(self.open_applications_window)

        self.mentor_meeting = QPushButton("Mentor Görüşmesi")
        self.mentor_meeting.setObjectName("MentorMeetingbuton")
        self.mentor_meeting.clicked.connect(self.open_mentor_window)

        self.interviews = QPushButton("Mülakatlar")
        self.interviews.setObjectName("Interviewsbuton")
        self.interviews.clicked.connect(self.open_interviews_window)

        self.close_button = QPushButton("Kapat", self)
        self.close_button.setObjectName("closeButton2")
        self.close_button.clicked.connect(self.close_application)

        layout1 = QHBoxLayout()
        layout1.addStretch()
        layout1.addWidget(self.image_label)
        layout1.addStretch()

        layout = QVBoxLayout()
        layout.addLayout(layout1)
        layout.addWidget(self.applications_window)
        layout.addWidget(self.mentor_meeting)
        layout.addWidget(self.interviews)
        layout.addWidget(self.close_button)
        self.setLayout(layout)

        self.setStyleSheet(open("styles.qss").read())

    def open_applications_window(self):
        self.hide()
        from basvurular_2_beyza import ApplicationsWindow
        self.app_window = ApplicationsWindow()
        self.app_window.show()

    def open_mentor_window(self):
        self.hide()
        from mentor_menuu import MentorGorusmesiSayfasiWindow
        self.mentor_window = MentorGorusmesiSayfasiWindow()
        self.mentor_window.show()

    def open_interviews_window(self):
        self.hide()
        from Mulakatlar_sayfasi_murat import MulakatlarSayfasi
        self.mulakatlar_sayfasi = MulakatlarSayfasi()
        self.mulakatlar_sayfasi.show()  # MulakatlarSayfasi penceresini göster

    def close_application(self):
        self.close()

    def center(self):
        screen_geometry = QApplication.primaryScreen().geometry()
        x = (screen_geometry.width() - self.width()) // 2
        y = (screen_geometry.height() - self.height()) // 2
        self.move(x, y)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = SelectionWindow()
    window.show()
    sys.exit(app.exec())
