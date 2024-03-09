import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QLabel, QLineEdit, QPushButton, QVBoxLayout, QHBoxLayout, \
    QWidget, QTreeWidget, QTreeWidgetItem
import json


class MulakatlarSayfasi(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Mulakatlar Sayfası")

        # Ana widget oluştur
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)

        self.layout = QVBoxLayout(self.central_widget)

        # Arama kutusu ve butonu
        self.arama_entry = QLineEdit()
        self.arama_buton = QPushButton("Ara")
        self.arama_buton.clicked.connect(self.arama_yap)
        arama_layout = QHBoxLayout()
        arama_layout.addWidget(self.arama_entry)
        arama_layout.addWidget(self.arama_buton)
        self.layout.addLayout(arama_layout)

        self.layout1 = QHBoxLayout()

        # Projesi Gonderilenler Butonu
        self.proje_gonderilenler_buton = QPushButton("Projesi Gönderilenler")
        self.proje_gonderilenler_buton.clicked.connect(self.proje_gonderilenler)
        self.layout1.addWidget(self.proje_gonderilenler_buton)

        # Projesi Gelmis Olanlar Butonu
        self.proje_gelmis_olanlar_buton = QPushButton("Projesi Gelmiş Olanlar")
        self.proje_gelmis_olanlar_buton.clicked.connect(self.proje_gelmis_olanlar)
        self.layout1.addWidget(self.proje_gelmis_olanlar_buton)

        # Geri Dön Butonu
        self.geri_don_buton = QPushButton("Tercihler Ekranına Geri Dön")
        self.geri_don_buton.clicked.connect(self.open_previous_page_window)
        self.layout1.addWidget(self.geri_don_buton)

        # Uygulamayı kapatma butonu
        self.kapat_buton = QPushButton("Uygulamayı Kapat")
        self.kapat_buton.clicked.connect(self.close)
        self.layout1.addWidget(self.kapat_buton)
        self.layout.addLayout(self.layout1)

        # Kullanıcı admin mi kontrol et
        self.kullanici_admin_mi = self.kullanici_admin_kontrol_et()
        # Sonuç tablosu
        self.sonuc_tablosu = QTreeWidget()
        self.sonuc_tablosu.setColumnCount(3)
        self.sonuc_tablosu.setHeaderLabels(["Ad", "Soyad", "Proje Durumu"])
        self.layout.addWidget(self.sonuc_tablosu)
        self.center()

    def arama_yap(self):
        # Arama kutusundan alınan değeri al
        arama_kriteri = self.arama_entry.text()

        # Arama kriterine göre sonuçları filtrele
        sonuclar = []
        with open("mulakat_listesi.json", "r") as file:
            veriler = json.load(file)
            for veri in veriler:
                if arama_kriteri.lower() in veri["Ad"].lower() or arama_kriteri.lower() in veri["Soyad"].lower():
                    sonuclar.append((veri["Ad"], veri["Soyad"], veri["Proje Durumu"]))

        # Eski verileri temizle
        self.sonuc_tablosu.clear()

        # Yeni sonuçları ekle
        for sonuc in sonuclar:
            item = QTreeWidgetItem(self.sonuc_tablosu)
            item.setText(0, sonuc[0])
            item.setText(1, sonuc[1])
            item.setText(2, sonuc[2])

    def proje_gonderilenler(self):
        # Projesi Gonderilenler fonksiyonu buraya yazılabilir
        self.sonuc_tablosu.clear()  # Eski verileri temizle
        with open("mulakat_listesi.json", "r") as file:
            veriler = json.load(file)
            for veri in veriler:
                if veri["Proje Durumu"] == "Gonderilenler":
                    item = QTreeWidgetItem(self.sonuc_tablosu)
                    item.setText(0, veri["Ad"])
                    item.setText(1, veri["Soyad"])
                    item.setText(2, veri["Proje Durumu"])

    def proje_gelmis_olanlar(self):
        # Projesi Gelmis Olanlar fonksiyonu buraya yazılabilir
        self.sonuc_tablosu.clear()  # Eski verileri temizle
        with open("mulakat_listesi.json", "r") as file:
            veriler = json.load(file)
            for veri in veriler:
                if veri["Proje Durumu"] == "Gelmis Olanlar":
                    item = QTreeWidgetItem(self.sonuc_tablosu)
                    item.setText(0, veri["Ad"])
                    item.setText(1, veri["Soyad"])
                    item.setText(2, veri["Proje Durumu"])

    def tercihlere_don(self):
        self.sonuc_tablosu.clear()  # Eski verileri temizle
        if self.kullanici_admin_mi:
            # Eğer kullanıcı admin ise, Tercihler-Admin Ekranına dön
            self.setWindowTitle("Tercihler-Admin Ekranı")
            # Burada Tercihler-Admin ekranının oluşturulması ve gösterilmesi sağlanabilir
        else:
            # Eğer kullanıcı admin değilse, Tercihler Ekranına dön
            self.setWindowTitle("Tercihler Ekranı")
            # Burada Tercihler ekranının oluşturulması ve gösterilmesi sağlanabilir

    def kullanici_admin_kontrol_et(self):
        # Rastgele bir JSON dosyası oluşturalım
        with open("kullanici.json", "w") as f:
            json.dump({"kullanici_tipi": "admin"}, f)

        # JSON dosyasını okuyalım ve kullanıcı tipini kontrol edelim
        with open("kullanici.json", "r") as f:
            veri = json.load(f)
            if veri["kullanici_tipi"] == "admin":
                return True
            else:
                return False

    def center(self):
        screen_geometry = QApplication.primaryScreen().geometry()  # Ekranın geometrisini al
        x = (screen_geometry.width() - self.width()) // 2  # Pencerenin x koordinatı
        y = (screen_geometry.height() - self.height()) // 2  # Pencerenin y koordinatı
        self.move(x, y)  # Pencereyi bu koordinatlara taşı

    def open_previous_page_window(self):
        self.close()
        from tercih_menu import SelectionWindow
        self.previous_page = SelectionWindow()
        self.previous_page.show()


def main():
    app = QApplication(sys.argv)
    window = MulakatlarSayfasi()
    window.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
