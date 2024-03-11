from PyQt6.QtWidgets import*
from user_admin_preference_ui import Ui_Form
from applications import ApplicationsPage
from interviews import InterviewsPage
from mentor_menu import MentorMenuPage
from main_admin_menu import MainAdminMenuPage
from user_preference import UserPreferencePage

class UserAdminPreferencePage(QWidget):
    def __init__(self) :
        super().__init__()
        self.useradminform = Ui_Form()
        self.useradminform.setupUi(self)
        self.applicationswindow_open = ApplicationsPage()
        self.interviewswindow_open = InterviewsPage() 
        self.mentormenu_open = MentorMenuPage()
        self.mainadminmenu_open = MainAdminMenuPage()
        self.useradminform.pushButton_user_admin_applications.clicked.connect(self.app_in)
        self.useradminform.pushButton_user_admin_interviews.clicked.connect(self.inter_in)
        self.useradminform.pushButton_user_admin_exit.clicked.connect(self.exit_in)
        self.useradminform.pushButton_user_admin_main_menu.clicked.connect(self.menu_in)
        self.useradminform.pushButton_user_admin_mentor_meeting.clicked.connect(self.mentor_in)
        self.useradminform.pushButton_user_admin_menu.clicked.connect(self.adminmenu_in)

    def app_in(self):
        UserPreferencePage.app_in(self)

    def inter_in(self):
        UserPreferencePage.inter_in(self)

    def exit_in(self):
        UserPreferencePage.exit_in(self)
        
    def menu_in(self):pass


    def mentor_in(self):
        UserPreferencePage.mentor_in(self)

    def adminmenu_in(self):
        self.close()
        self.mainadminmenu_open.show()    