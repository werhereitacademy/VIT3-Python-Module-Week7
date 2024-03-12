from PyQt6.QtWidgets import QApplication
from login import LoginPage


if __name__ == '__main__':
    app = QApplication([])
    window = LoginPage()
    window.show()
    app.exec()
