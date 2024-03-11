from PyQt6.QtWidgets import QApplication
from login import LoginPage

import gspread

credentials = 'key.json'
gc = gspread.service_account(filename=credentials)
spreadsheet = gc.open('Basvurular')
worksheet = spreadsheet.get_worksheet(0)
print(worksheet.get_all_values())

app = QApplication([])
window = LoginPage()
window.show()
app.exec()


    