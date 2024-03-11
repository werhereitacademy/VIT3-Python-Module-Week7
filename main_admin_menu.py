from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import*
from PyQt6.QtWidgets import QWidget
from main_admin_menu_ui import Ui_Form

class MainAdminMenuPage(QWidget):
    def __init__(self) -> None:
        super().__init__()
        mainadminmenuform = Ui_Form()
        mainadminmenuform.setupUi(self)