from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import *
from PyQt6.QtWidgets import QWidget
from interviews_ui import Ui_Form

class InterviewsPage(QWidget):
    def __init__(self) -> None:
        super().__init__()
        self.interviewsform = Ui_Form()
        self.interviewsform.setupUi(self)
    