import sys
import json
from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtWidgets import QMessageBox


class Ui_MentorGorusmesiSayfasi(object):
    def setupUi(self, MentorGorusmesiSayfasi):
        MentorGorusmesiSayfasi.setObjectName("MentorGorusmesiSayfasi")
        MentorGorusmesiSayfasi.resize(883, 481)
        self.verticalLayoutWidget = QtWidgets.QWidget(MentorGorusmesiSayfasi)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(70, 30, 761, 431))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Minimum,
                                           QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem)
        self.label_mentormenu = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_mentormenu.setFont(font)
        self.label_mentormenu.setObjectName("label_mentormenu")
        self.horizontalLayout_6.addWidget(self.label_mentormenu)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Minimum,
                                            QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem1)
        self.verticalLayout_2.addLayout(self.horizontalLayout_6)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pushButton_tumgorusmeler = QtWidgets.QPushButton(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_tumgorusmeler.setFont(font)
        self.pushButton_tumgorusmeler.setIconSize(QtCore.QSize(16, 16))
        self.pushButton_tumgorusmeler.setObjectName("pushButton_tumgorusmeler")
        self.horizontalLayout.addWidget(self.pushButton_tumgorusmeler)
        spacerItem2 = QtWidgets.QSpacerItem(30, 20, QtWidgets.QSizePolicy.Policy.Expanding,
                                            QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout.addItem(spacerItem2)
        self.pushButton_ara = QtWidgets.QPushButton(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_ara.setFont(font)
        self.pushButton_ara.setObjectName("pushButton_ara")
        self.horizontalLayout.addWidget(self.pushButton_ara)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Maximum,
                                            QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout.addItem(spacerItem3)
        self.lineEdit_aranacakmetin = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setStrikeOut(False)
        self.lineEdit_aranacakmetin.setFont(font)
        self.lineEdit_aranacakmetin.setPlaceholderText("Adaya ait ad soyad:")
        self.horizontalLayout.addWidget(self.lineEdit_aranacakmetin)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding,
                                            QtWidgets.QSizePolicy.Policy.Minimum)
        self.verticalLayout_2.addItem(spacerItem4)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding,
                                            QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem5)
        self.comboBox = QtWidgets.QComboBox(self.verticalLayoutWidget)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.horizontalLayout_5.addWidget(self.comboBox)
        self.verticalLayout_2.addLayout(self.horizontalLayout_5)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.pushButton_tercihler = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.pushButton_tercihler.setObjectName("pushButton_tercihler")
        self.horizontalLayout_2.addWidget(self.pushButton_tercihler)
        self.pushButton_exit = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.pushButton_exit.setObjectName("pushButton_exit")
        self.horizontalLayout_2.addWidget(self.pushButton_exit)
        spacerItem6 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding,
                                            QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem6)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        self.tableWidget = QtWidgets.QTableWidget(self.verticalLayoutWidget)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(6)
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(5, item)
        self.verticalLayout_2.addWidget(self.tableWidget)

        self.retranslateUi(MentorGorusmesiSayfasi)
        QtCore.QMetaObject.connectSlotsByName(MentorGorusmesiSayfasi)

    def retranslateUi(self, MentorGorusmesiSayfasi):
        _translate = QtCore.QCoreApplication.translate
        MentorGorusmesiSayfasi.setWindowTitle(_translate("MentorGorusmesiSayfasi", "Form"))
        self.label_mentormenu.setText(_translate("MentorGorusmesiSayfasi", "MENTOR MENU"))
        self.pushButton_tumgorusmeler.setText(_translate("MentorGorusmesiSayfasi", "TUM GORUSMELER"))
        self.pushButton_ara.setText(_translate("MentorGorusmesiSayfasi", "ARA"))
        self.comboBox.setItemText(0,
                                  _translate("MentorGorusmesiSayfasi", "VIT Projesinin tamamina katilmasi uygun olur"))
        self.comboBox.setItemText(1, _translate("MentorGorusmesiSayfasi",
                                                "Bir sonraki VIT Projesube Katilmasi Daha Uygun Olur."))
        self.comboBox.setItemText(2, _translate("MentorGorusmesiSayfasi", "Diger"))
        self.pushButton_tercihler.setText(_translate("MentorGorusmesiSayfasi", "TERCIHLER"))
        self.pushButton_exit.setText(_translate("MentorGorusmesiSayfasi", "EXIT"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MentorGorusmesiSayfasi", "Gorusme Tarihi"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MentorGorusmesiSayfasi", "Ad Soyad"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("MentorGorusmesiSayfasi", "Mentor"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("MentorGorusmesiSayfasi", "IT BIlgisi"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("MentorGorusmesiSayfasi", "Yogunluk"))
        item = self.tableWidget.horizontalHeaderItem(5)
        item.setText(_translate("MentorGorusmesiSayfasi", "Yorumlar"))


class MentorGorusmesiSayfasiWindow(QtWidgets.QWidget, Ui_MentorGorusmesiSayfasi):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.pushButton_ara.clicked.connect(self.search_data)
        self.comboBox.currentIndexChanged.connect(self.filter_data)
        self.pushButton_tumgorusmeler.clicked.connect(self.show_all_data)
        self.pushButton_tercihler.clicked.connect(self.open_selection_window)
        self.pushButton_exit.clicked.connect(self.close_application)
        self.load_data()
        self.center()

    def load_data(self):
        with open("mentor_menu.json", "r") as file:
            data = json.load(file)
            for row, gorusme in enumerate(data["mentor_gorusmeleri"]):
                self.tableWidget.insertRow(row)
                self.tableWidget.setItem(row, 0, QtWidgets.QTableWidgetItem(gorusme["gorusme_tarihi"]))
                self.tableWidget.setItem(row, 1, QtWidgets.QTableWidgetItem(gorusme["ad_soyad"]))
                self.tableWidget.setItem(row, 2, QtWidgets.QTableWidgetItem(gorusme["mentor"]))
                self.tableWidget.setItem(row, 3, QtWidgets.QTableWidgetItem(gorusme["it_bilgisi"]))
                self.tableWidget.setItem(row, 4, QtWidgets.QTableWidgetItem(gorusme["yogunluk"]))
                self.tableWidget.setItem(row, 5, QtWidgets.QTableWidgetItem(gorusme["yorumlar"]))

    def search_data(self):
        search_text = self.lineEdit_aranacakmetin.text().lower()
        if search_text:
            found_items = []
            for row in range(self.tableWidget.rowCount()):
                item = self.tableWidget.item(row, 1)  # Ad Soyad sütunu
                if item and search_text in item.text().lower():
                    found_items.append(row)
            if found_items:
                self.highlight_rows(found_items)
            else:
                self.show_message("Arama Sonucu", "Aranan metin bulunamadı.")
        else:
            self.clear_highlight()

    def filter_data(self):
        filter_text = self.comboBox.currentText()
        if filter_text:
            if filter_text == "VIT Projesinin tamamina katilmasi uygun olur":
                search_text = "Vit projesinin tamamina katilmasi uygun olur."
            elif filter_text == "Bir sonraki VIT Projesube Katilmasi Daha Uygun Olur.":
                search_text = "Bir sonraki VIT Projesube Katilmasi Daha Uygun Olur."
            else:
                search_text = filter_text

            found_items = []
            for row in range(self.tableWidget.rowCount()):
                item = self.tableWidget.item(row, 5)  # Yorumlar sütunu
                if item and search_text in item.text():
                    found_items.append(row)
            if found_items:
                self.highlight_rows(found_items)
            else:
                self.show_message("Filtreleme Sonucu", "Filtreleme sonucu bulunamadı.")
        else:
            self.clear_highlight()

    def highlight_rows(self, rows):
        for row in range(self.tableWidget.rowCount()):
            if row in rows:
                self.tableWidget.setRowHidden(row, False)
            else:
                self.tableWidget.setRowHidden(row, True)

    def clear_highlight(self):
        for row in range(self.tableWidget.rowCount()):
            self.tableWidget.setRowHidden(row, False)

    def show_message(self, title, message):
        msg_box = QMessageBox()
        msg_box.setWindowTitle(title)
        msg_box.setText(message)
        msg_box.exec()

    def show_all_data(self):
        self.tableWidget.setRowCount(0)
        self.load_data()

    def open_selection_window(self):
        # Başvurular penceresini aç
        self.hide()
        from tercih_menu import SelectionWindow
        # ikinci defa ayni tuslar ile ileri geri yapinca hata veriyordu bu sekilde hata gitti
        self.mentor_window = SelectionWindow()  # Tercihler penceresini oluştur
        self.mentor_window.show()  # Tercihler penceresini göster

    def close_application(self):
        self.close()

    def open_page(self):
        self.show()

    def center(self):
        screen_geometry = QtWidgets.QApplication.primaryScreen().geometry()  # Ekranın geometrisini al
        x = (screen_geometry.width() - self.width()) // 2  # Pencerenin x koordinatı
        y = (screen_geometry.height() - self.height()) // 2  # Pencerenin y koordinatı
        self.move(x, y)  # Pencereyi bu koordinatlara taşı


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MentorGorusmesiSayfasiWindow()
    window.show()
    sys.exit(app.exec())
