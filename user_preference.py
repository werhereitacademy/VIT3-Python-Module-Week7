from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QWidget
from user_preference_ui import Ui_Form
from applications import ApplicationsPage
from interviews import InterviewsPage
from mentor_menu import MentorMenuPage




class UserPreferencePage(QWidget):
    def __init__(self) -> None:
        super().__init__()
        self.userpreform = Ui_Form()
        self.userpreform.setupUi(self)
        self.applicationswindow_open = ApplicationsPage()
        self.interviewswindow_open = InterviewsPage() 
        self.mentormenu_open = MentorMenuPage()
        
        self.userpreform.pushButton_user_pre_applications.clicked.connect(self.app_in)
        self.userpreform.pushButton_user_pre_interviews.clicked.connect(self.inter_in)
        self.userpreform.pushButton_user_pre_exit.clicked.connect(self.exit_in)
        self.userpreform.pushButton_user_pre_main_menu.clicked.connect(self.menu_in)
        self.userpreform.pushButton_user_pre_mentor_meeting.clicked.connect(self.mentor_in)

    def app_in(self):
        self.close()
        self.applicationswindow_open.show()

    def inter_in(self):
        self.close()
        self.interviewswindow_open.show()

    def exit_in(self):
        self.close()

    def menu_in(self):pass
        

    def mentor_in(self):
        self.close()
        self.mentormenu_open.show()
        
