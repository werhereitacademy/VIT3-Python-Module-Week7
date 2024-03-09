import os
import sys
import json
from PyQt6.QtWidgets import *
from Arayüz_giriş_penceresi import *
from tercih_admin_secimi import *
from tercih_menu import *
# -*- coding: utf-8 -*-




class ApplicationsWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Başvurular")
        self.setGeometry(200, 600, 400, 200)
        self.center()

        # Ara butonu ve input kutusu
        self.search_label = QLabel("Arama:")
        self.search_input = QLineEdit()
        self.search_button = QPushButton("Ara")
        self.search_button.clicked.connect(self.search_in_applications)
        self.search_input.returnPressed.connect(self.search_in_applications)


        # Butonlar
        self.previous_page_button = QPushButton("Tercihler")
        self.show_all_button = QPushButton("Tüm Başvurular")
        self.mentored_button = QPushButton("Mentor Görüşmesi Yapılanlar")
        self.unmentored_button = QPushButton("Mentor Görüşmesi Yapılmayanlar")

        self.show_all_button.setObjectName("allapplicationswindowbuton")
        self.show_all_button.clicked.connect(lambda: self.filter_applications())

        self.mentored_button.setObjectName("mentoredwindowbuton")
        self.mentored_button.clicked.connect(lambda: self.filter_applications("Yapıldı"))

        self.unmentored_button.setObjectName("unmentoredwindowbuton")
        self.unmentored_button.clicked.connect(lambda: self.filter_applications("Yapılmadı"))

        self.previous_page_button.setObjectName("PreviousPagebuton")
        self.previous_page_button.clicked.connect(self.open_previous_page_window)

        self.close_button = QPushButton("Kapat", self)
        self.close_button.setObjectName("closeButton")
        self.close_button.clicked.connect(self.close_application)


        # Tablo widget'ını başlatma
        self.table_widget = QTableWidget()
        self.table_widget.setColumnCount(4)  # İsim, Soyisim, Mentorluk, Şehir
        self.table_widget.setHorizontalHeaderLabels(['İsim', 'Soyisim', 'Mentörlük Durumu', 'Şehir'])
        #self.table_widget.hide()  # İlk başta tabloyu gizle


        #Layout
        v_layout = QVBoxLayout()
        h_layout = QHBoxLayout()
        h_layout.addWidget(self.search_label)
        h_layout.addWidget(self.search_input)
        h_layout.addWidget(self.search_button)
        h_layout.addWidget(self.close_button)
        v_layout.addLayout(h_layout)
        v_layout.addWidget(self.previous_page_button)
        v_layout.addWidget(self.show_all_button)
        v_layout.addWidget(self.mentored_button)
        v_layout.addWidget(self.unmentored_button)
        v_layout.addWidget(self.table_widget)############burayi sonra ekledim - tablo en altta
        self.setLayout(v_layout)

        dosya_yolu = os.path.join(os.path.dirname(__file__), "styles.qss")
        self.setStyleSheet(open(dosya_yolu).read())
        

    def center(self):
        screen_geometry = QApplication.primaryScreen().geometry()  # Ekranın geometrisini al
        x = (screen_geometry.width() - self.width()) // 2  # Pencerenin x koordinatı
        y = (screen_geometry.height() - self.height()) // 2  # Pencerenin y koordinatı
        self.move(x, y)  # Pencereyi bu koordinatlara taşı
    
    def open_previous_page_window(self):
        self.close()
        self.previous_page = SelectionWindow()
        self.previous_page.show()
        self.close()

    def close_application(self):
        #uygulamayi kapat komutu ile kapatir
        self.close()
    
    def search_in_applications(self):
        search_term = self.search_input.text().lower()
        file_path = os.path.join(os.path.dirname(__file__), "all_applications.json")
        try:
            with open(file_path, 'r') as file:
                data = json.load(file)
            # Arama terimine göre filtreleme
            filtered_data = [entry for entry in data if search_term in entry['isim'].lower() or 
                             search_term in entry['soyisim'].lower() or 
                             search_term in entry['sehir'].lower() or
                             search_term in entry['mentorluk'].lower()]
            self.show_data_in_table(filtered_data)
        except FileNotFoundError:
            print("Dosya bulunamadı.")


    def filter_applications(self, filter_status=None):
        file_path = os.path.join(os.path.dirname(__file__), "all_applications.json")
        try:
            with open(file_path, 'r') as file:
                data = json.load(file)
            if filter_status:
                data = [entry for entry in data if entry["mentorluk"] == filter_status]
            self.show_data_in_table(data)
        except FileNotFoundError:
            print("Dosya bulunamadı.")

    def show_data_in_table(self, data):
        self.table_widget.clear()  # Mevcut verileri temizle
        self.table_widget.setRowCount(len(data))
        self.table_widget.setColumnCount(4)
        self.table_widget.setHorizontalHeaderLabels(['İsim', 'Soyisim', 'Mentörlük Durumu', 'Şehir'])
        
        for row, entry in enumerate(data):
            self.table_widget.setItem(row, 0, QTableWidgetItem(entry['isim']))
            self.table_widget.setItem(row, 1, QTableWidgetItem(entry['soyisim']))
            self.table_widget.setItem(row, 2, QTableWidgetItem(entry['mentorluk']))
            self.table_widget.setItem(row, 3, QTableWidgetItem(entry['sehir']))
        self.table_widget.show()  # Tabloyu güncelle ve göster
    


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ApplicationsWindow()
    window.show()
    sys.exit(app.exec())

