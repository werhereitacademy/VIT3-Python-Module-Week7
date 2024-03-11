from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import*
from PyQt6.QtWidgets import QWidget
from mentor_menu_ui import Ui_Form

class MentorMenuPage(QWidget):
    def __init__(self) -> None:
        super().__init__()
        mentormenuform = Ui_Form()
        mentormenuform.setupUi(self)
