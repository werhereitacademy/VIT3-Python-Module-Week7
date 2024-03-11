from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import*
from PyQt6.QtWidgets import QWidget
from applications_ui import Ui_Form


class ApplicationsPage(QWidget):
    def __init__(self) -> None:
        super().__init__()
        self.applicationsform = Ui_Form()
        self.applicationsform.setupUi(self)
       