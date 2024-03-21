import sys
import os
import pickle
from google.auth.transport.requests import Request
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QTableWidgetItem, QMessageBox, QPushButton
from PyQt6 import QtCore
from PyQt6.QtCore import QCoreApplication, QTimer
from PyQt6.uic import loadUi
import gspread
from oauth2client.service_account import ServiceAccountCredentials
from google.oauth2.credentials import Credentials
import pandas as pd
# e-mail 
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Google Sheets API için kimlik doğrulama bilgileri
creds = 'key.json'
gc=gspread.service_account(filename=creds)

# Kullanıcıların bulunduğu Google Sheets dosyasını açma ve verileri alma
spreadsheet=gc.open('Kullanicilar')
worksheet= spreadsheet.get_worksheet(0)
all_values = worksheet.get_all_values()
del all_values[0]

class ProjeArayuz(QMainWindow):
    def __init__(self):
        super(ProjeArayuz, self).__init__()
        loadUi('proje_arayuz.ui', self)
        self.Uyari.clear()
        self.girisButonu.clicked.connect(self.Giris)
        self.cikisButonu.clicked.connect(QCoreApplication.exit)
        self.setWindowFlags(QtCore.Qt.WindowType.FramelessWindowHint)

    # interface heryere hareket ettirme kodlari
    def mousePressEvent(self, event):
        self.draPos = event.globalPosition().toPoint()

    def mouseMoveEvent(self, event):
        self.move(self.pos() + event.globalPosition().toPoint() - self.draPos)
        self.draPos = event.globalPosition().toPoint()
        event.accept()

    def Giris(self):
        kullaniciadi = self.kullaniciAdi.text()
        sifre = self.kullaniciParola.text()

        try:
            for row in all_values:
                k = row[0]
                s = row[1]
                y = row[2]
                if kullaniciadi==k and sifre==s:
                    if y == "admin":
                      tercih_menu_admin.show()  # Admin yetkisi varsa admin menüsünü göster
                    else:
                      tercih_menu.show()  # Admin yetkisi yoksa standart menüyü göster
                      
                    proje_arayuz.hide()
                    self.kullaniciAdi.clear()
                    self.kullaniciParola.clear()
                    self.Uyari.clear()
                    break
                
                elif kullaniciadi!=k or sifre!=s:
                    self.kullaniciAdi.clear()
                    self.kullaniciParola.clear()
                    self.Uyari.setText('Sisteme giriş başarısız ! Kullanıcı adı veya Kullanici sifresi hatalı!')
        except Exception as e:
            pass
            # QMessageBox.critical(self, "Hata", f"Veri alınırken bir hata oluştu: {str(e)}", QMessageBox.Ok)

class TercihMenu(QMainWindow):
    def __init__(self):
        super().__init__()
        loadUi('tercih_menu.ui', self)

        self.basvurularButon.clicked.connect(lambda: (basvurular_sayfasi.show(), tercih_menu.hide()))
        self.mentorGorusmesiButon.clicked.connect(lambda: (mentor_gorusme_sayfasi.show(), tercih_menu.hide()))
        self.mulakatlarButonu.clicked.connect(lambda: (mulakatlar.show(), tercih_menu.hide()))
        self.cikisButonu.clicked.connect(QCoreApplication.exit)
        self.geriButonu.clicked.connect(lambda: (proje_arayuz.show(), tercih_menu.hide()))
        self.setWindowFlags(QtCore.Qt.WindowType.FramelessWindowHint)
    
    def mousePressEvent(self, event):
        self.draPos = event.globalPosition().toPoint()

    def mouseMoveEvent(self, event):
        self.move(self.pos() + event.globalPosition().toPoint() - self.draPos)
        self.draPos = event.globalPosition().toPoint()
        event.accept()

class TercihMenuAdmin(QMainWindow):
    def __init__(self):
        super().__init__()
        loadUi('tercih_menu_admin.ui', self)

        self.basvurularButon.clicked.connect(lambda: (basvurular_sayfasi.show(), tercih_menu.hide()))
        self.mentorGorusmesiButon.clicked.connect(lambda: (mentor_gorusme_sayfasi.show(), tercih_menu.hide()))
        self.mulakatlarButonu.clicked.connect(lambda: (mulakatlar.show(), tercih_menu.hide()))
        self.adminMenuButonu.clicked.connect(lambda: (admin_menu.show(), tercih_menu.hide()))
        self.cikisButonu.clicked.connect(QCoreApplication.exit)
        self.geriButonu.clicked.connect(lambda: (proje_arayuz.show(), tercih_menu.hide()))
        self.setWindowFlags(QtCore.Qt.WindowType.FramelessWindowHint)

    def mousePressEvent(self, event):
        self.draPos = event.globalPosition().toPoint()

    def mouseMoveEvent(self, event):
        self.move(self.pos() + event.globalPosition().toPoint() - self.draPos)
        self.draPos = event.globalPosition().toPoint()
        event.accept()

spreadsheet=gc.open('Basvurular')
worksheet3= spreadsheet.get_worksheet(0)
all_values3 = worksheet3.get_all_values()
del all_values3[0]

spreadsheet=gc.open('VIT1')
worksheet4= spreadsheet.get_worksheet(0)
all_values4 = worksheet4.get_all_values()
del all_values4[0] 

spreadsheet=gc.open('VIT2')
worksheet5= spreadsheet.get_worksheet(0)
all_values5 = worksheet5.get_all_values()
del all_values5[0]
class BasvurularSayfasi(QMainWindow):
    def __init__(self):
        super().__init__()
        loadUi('basvurular.ui', self)
        self.cikisButonu.clicked.connect(QCoreApplication.exit)
        self.geriButonu.clicked.connect(lambda: (self.tableWidget.setRowCount(0), self.aramaKutusu.clear(), tercih_menu.show(), basvurular_sayfasi.hide()))
        self.araButonu.clicked.connect(self.Arama)
        self.tumBasvurularButonu.clicked.connect(self.tumBasvurular)
        self.oncekiVitKontrolButonu.clicked.connect(self.oncekiVitKontrol)
        self.mukerrerKayitButonu.clicked.connect(self.mukerrerKayit)
        self.basvuruFiltreliButonu.clicked.connect(self.basvuruFiltreli)
        self.farkliKayitButonu.clicked.connect(self.farkliKayit)
        self.mentorGorusmesiTanimlananlarButonu.clicked.connect(self.MgTamamlanan)
        self.mentorGorusmesiTanimlanmayanlarButonu.clicked.connect(self.MgTamamlanmayan)
        self.setWindowFlags(QtCore.Qt.WindowType.FramelessWindowHint)

    def mousePressEvent(self, event):
        self.draPos = event.globalPosition().toPoint()

    def mouseMoveEvent(self, event):
        self.move(self.pos() + event.globalPosition().toPoint() - self.draPos)
        self.draPos = event.globalPosition().toPoint()
        event.accept()

    def SonucGosterme(self):
        self.tableWidget.setRowCount(0)
        for row_index, (index, row) in enumerate(self.df.iterrows()):
            self.tableWidget.insertRow(row_index)
            for col_index, col_value in enumerate(row):
                item = QTableWidgetItem(str(col_value))
                self.tableWidget.setItem(row_index, col_index, item)
            self.liste_kisi_sayisi.setText(f'Bulunan Kişi Sayısı : {len(self.df)}')
            QTimer.singleShot(3000, lambda: self.liste_kisi_sayisi.clear())

    def Arama(self):
        if self.arama_kutusu.text()!='':
            results= []
            ara= self.arama_kutusu.text()
            for kayit in all_values3:
                if ara.lower() in kayit[1].lower():
                    results.append(kayit)
            if not results:
                    self.arama_negatif.setText('Aradığınız kişi listede bulunmamaktadır!')
                    QTimer.singleShot(3000, lambda: self.arama_negatif.clear())
            self.df = pd.DataFrame(results)
        self.SonucGosterme()

    def tumBasvurular(self):
        self.df = pd.DataFrame(all_values3)
        self.SonucGosterme()

    def oncekiVitKontrol(self):
        results = []
        
        # Başvurular dosyasındaki adayları alın
        for row in all_values3:
            basvuru_adi_soyadi = row[1]  # Adayın kullanıcı adı
            basvuru_mail_adresi = row[2]  # Adayın e-posta adresi

            # VIT1 ve VIT2 dosyalarındaki adaylarla karşılaştırma yapın
            for vit_kaydi in all_values4:
                if basvuru_adi_soyadi == vit_kaydi[1] or basvuru_mail_adresi == vit_kaydi[2]:
                    results.append(row)
                    break
            
            for vit_kaydi in all_values5:
                if basvuru_adi_soyadi == vit_kaydi[1] or basvuru_mail_adresi == vit_kaydi[2]:
                    results.append(row)
                    break

        self.df = pd.DataFrame(results)
        self.SonucGosterme()

    def mukerrerKayit(self):
        results = []
        unique_records = set()  # Tekil kayıtları takip etmek için bir küme oluştur
        for kayit in all_values3:
            aday = (kayit[1], kayit[2])  # İsim ve mail adresi tuple'ını oluştur
            if aday in unique_records:  # Eğer bu kayıt daha önce eklenmişse, mükerrerdir
                results.append(kayit)
            else:
                unique_records.add(aday)  # Eğer daha önce eklenmemişse, set'e ekle
        self.df = pd.DataFrame(results)
        self.SonucGosterme()
    
    def basvuruFiltreli(self):
        # Kayıtları tutacak boş bir liste oluştur
        unique_records = []
        # Her kaydın benzersiz olup olmadığını kontrol etmek için bir set oluştur
        seen = set()
        for kayit in all_values3:
            # Kayıt tuple'ını (isim, e-posta) kontrol et
            record_tuple = (kayit[1], kayit[2])  # İsim ve e-posta adresini kullanarak bir tuple oluştur
            if record_tuple not in seen:
                seen.add(record_tuple)  # Görülen kayıtlara ekle
                unique_records.append(kayit)  # Kaydı benzersiz kayıtlar listesine ekle

        # DataFrame'i benzersiz kayıtlar ile oluştur
        self.df = pd.DataFrame(unique_records)
        self.SonucGosterme()  # Sonuçları gösterme fonksiyonunu çağır

    
    def farkliKayit(self):
        results = []

        # Başvurular dosyasındaki adayları alın
        basvurular = set((kayit[1], kayit[2]) for kayit in all_values3)

        # VIT1 dosyasındaki adayları alın
        vit1_adaylar = set((kayit[1], kayit[2]) for kayit in all_values4)

        # VIT2 dosyasındaki adayları alın
        vit2_adaylar = set((kayit[1], kayit[2]) for kayit in all_values5)

        # Başvurular dosyasında ancak VIT1 ve VIT2 dosyalarında olmayan adayları bulun
        for basvuru in basvurular:
            if basvuru not in vit1_adaylar and basvuru not in vit2_adaylar:
                for row in all_values3:
                    if (row[1], row[2]) == basvuru:
                        results.append(row)
                        break

        self.df = pd.DataFrame(results)
        self.SonucGosterme()
    
    def MgTamamlanan(self):
        results= []
        for kayit in all_values3:
            for x in all_values2:
                if kayit[1] == x[1]:
                    results.append(kayit)
        
        self.df = pd.DataFrame(results)
        self.SonucGosterme()

    def MgTamamlanmayan(self):
        results= []
        x=[]
        for kayit in all_values2:
            x.append(kayit[1])
        for kayit in all_values3:
            if not (kayit[1] in x):
                results.append(kayit)
                break
            
        self.df = pd.DataFrame(results)
        self.SonucGosterme()


spreadsheet=gc.open('Mulakatlar')
worksheet1= spreadsheet.get_worksheet(0)
all_values1 = worksheet1.get_all_values()
del all_values1[0]

class Mulakatlar(QMainWindow):

    def __init__(self):
        super().__init__()
        loadUi('mulakatlar.ui', self)
        self.exitButonu.clicked.connect(QCoreApplication.exit)
        self.tercihlerButonu.clicked.connect(lambda: (self.tableWidget.setRowCount(0), self.aramaKutusu.clear(), tercih_menu.show(), mulakatlar.hide()))
        self.araButonu.clicked.connect(self.Arama)
        self.projesiGonderilmisOlanlarButonu.clicked.connect(self.proje1)
        self.projesiGelmisOlanlarButonu.clicked.connect(self.proje2)
        self.setWindowFlags(QtCore.Qt.WindowType.FramelessWindowHint)

    def mousePressEvent(self, event):
        self.draPos = event.globalPosition().toPoint()

    def mouseMoveEvent(self, event):
        self.move(self.pos() + event.globalPosition().toPoint() - self.draPos)
        self.draPos = event.globalPosition().toPoint()
        event.accept()

    def SonucGosterme(self):
        self.tableWidget.setRowCount(0)
        for row_index, (index, row) in enumerate(self.df.iterrows()):
            self.tableWidget.insertRow(row_index)
            for col_index, col_value in enumerate(row):
                item = QTableWidgetItem(str(col_value))
                self.tableWidget.setItem(row_index, col_index, item)
            self.liste_kisi_sayisi.setText(f'Bulunan Kişi Sayısı : {len(self.df)}')
            QTimer.singleShot(3000, lambda: self.liste_kisi_sayisi.clear())

    def Arama(self):
        if self.arama_kutusu.text()!='':
            results= []
            ara= self.arama_kutusu.text()
            for kayit in all_values1:
                if ara.lower() in kayit[0].lower():
                    results.append(kayit)
            if not results:
                    self.arama_negatif.setText('Aradığınız kişi listede bulunmamaktadır!')
                    QTimer.singleShot(3000, lambda: self.arama_negatif.clear())
            self.df = pd.DataFrame(results)
        self.SonucGosterme()
       
    def proje1(self):
        results= []
        for kayit in all_values1:
            if kayit[1]!='':
                results.append(kayit)
        
        self.df = pd.DataFrame(results)
        self.SonucGosterme()

    def proje2(self):
        results = []
        for kayit in all_values1:
            if kayit[2]!='':
                results.append(kayit)
        self.df = pd.DataFrame(results)
        self.SonucGosterme()


spreadsheet=gc.open('Mentor')
worksheet2= spreadsheet.get_worksheet(0)
all_values2 = worksheet2.get_all_values()
del all_values2[0]
for kayit in all_values2:
    kayit[4], kayit[5], kayit[6], kayit[7] = kayit[6], kayit[7], kayit[4], kayit[5]

class MentorGorusmeSayfasi(QMainWindow):
    def __init__(self):
        super().__init__()
        loadUi('mentor_menu.ui', self)
        self.cikisButonu.clicked.connect(QCoreApplication.exit)
        self.tercihlerButonu.clicked.connect(lambda: (self.tableWidget.setRowCount(0), self.aramaKutusu.clear(), tercih_menu.show(), mentor_gorusme_sayfasi.hide()))
        self.araButonu.clicked.connect(self.Arama)
        self.tumGorusmelerButonu.clicked.connect(self.TumGorusmeler)
        self.cokluSecenekKutusu.currentIndexChanged.connect(self.update_table)
        self.setWindowFlags(QtCore.Qt.WindowType.FramelessWindowHint)
    
    def mousePressEvent(self, event):
        self.draPos = event.globalPosition().toPoint()

    def mouseMoveEvent(self, event):
        self.move(self.pos() + event.globalPosition().toPoint() - self.draPos)
        self.draPos = event.globalPosition().toPoint()
        event.accept()

    def SonucGosterme(self):
        self.tableWidget.setRowCount(0)
        for row_index, (index, row) in enumerate(self.df.iterrows()):
            self.tableWidget.insertRow(row_index)
            for col_index, col_value in enumerate(row):
                item = QTableWidgetItem(str(col_value))
                self.tableWidget.setItem(row_index, col_index, item)
            self.liste_kisi_sayisi.setText(f'Bulunan Kişi Sayısı : {len(self.df)}')
            QTimer.singleShot(3000, lambda: self.liste_kisi_sayisi.clear())

    def Arama(self):
        if self.aramaKutusu.text()!='':
            results= []
            ara= self.aramaKutusu.text()
            for kayit in all_values2:
                if ara.lower() in kayit[1].lower():
                    results.append(kayit)
            if not results:
                    self.arama_negatif.setText('Aradığınız kişi listede bulunmamaktadır!')
                    QTimer.singleShot(3000, lambda: self.arama_negatif.clear())
            self.df = pd.DataFrame(results)
            self.SonucGosterme()
    
    def TumGorusmeler(self):
        self.df = pd.DataFrame(all_values2)
        self.SonucGosterme()

    def update_table(self):
        results = []
        for kayit in all_values2:
            if self.cokluSecenekKutusu.currentText() == kayit[6]:
                results.append(kayit)
        self.df = pd.DataFrame(results)
        self.SonucGosterme()

SCOPES = ['https://www.googleapis.com/auth/calendar.readonly']

class AdminMenu(QMainWindow):
    def __init__(self):
        super().__init__()
        loadUi('admin_menu.ui', self)

        self.etkinlikKontrolButon.clicked.connect(self.etkinlik_kaydi)
        self.mailGonderButon.clicked.connect(self.mail_gonder)
        self.tercihlerAdminMenuButon.clicked.connect(lambda: (self.tableWidget.setRowCount(0), tercih_menu_admin.show(), admin_menu.hide()))       
        self.exitButon.clicked.connect(QCoreApplication.exit)   

    # def etkinlik_kaydi(self):
    #     creds = None
    #     if os.path.exists('token.pickle'):
    #         with open('token.pickle', 'rb') as token:
    #             creds = pickle.load(token)
    #     if not creds or not creds.valid:
    #         if creds and creds.expired and creds.refresh_token:
    #             creds.refresh(Request())
    #         else:
    #             flow = InstalledAppFlow.from_client_secrets_file(
    #                 'credentials.json', SCOPES)
    #             creds = flow.run_local_server(port=0)
    #         with open('token.pickle', 'wb') as token:
    #             pickle.dump(creds, token)

    #     service = build('calendar', 'v3', credentials=creds)

    #     # Etkinlikleri çekme
    #     print('Getting the upcoming 10 events')
    #     events_result = service.events().list(calendarId='primary', 
    #                                           timeMin='2020-01-01T00:00:00Z', 
    #                                           maxResults=10, singleEvents=True, 
    #                                           orderBy='startTime').execute()
    #     events = events_result.get('items', [])

    #     if not events:
    #         print('No upcoming events found.')
    #         return

    #     for event in events:
    #         start = event['start'].get('dateTime', event['start'].get('date'))
    #         print(start, event['summary'])

    def etkinlik_kaydi(self):
        creds = None
        # Eğer token.pickle dosyası varsa ve geçerliyse, mevcut kimlik bilgilerini kullan
        if os.path.exists('token.pickle'):
            with open('token.pickle', 'rb') as token:
                creds = pickle.load(token)
        # Eğer kimlik bilgileri yoksa veya geçersizse, yeniden kimlik doğrulama yap
        if not creds or not creds.valid:
            if creds and creds.expired and creds.refresh_token:
                creds.refresh(Request())
            else:
                flow = InstalledAppFlow.from_client_secrets_file(
                    'credentials.json', SCOPES)
                creds = flow.run_local_server(port=0)
            # Yeni kimlik bilgilerini token.pickle dosyasına kaydet
            with open('token.pickle', 'wb') as token:
                pickle.dump(creds, token)

        service = build('calendar', 'v3', credentials=creds)

        # Google Takvim API'sinden etkinlikleri çek
        events_result = service.events().list(calendarId='primary', 
                                            timeMin='2020-01-01T00:00:00Z', 
                                            maxResults=10, singleEvents=True, 
                                            orderBy='startTime').execute()
        events = events_result.get('items', [])

        # Etkinliklerin gösterileceği tableWidget'ı ayarla
        self.tableWidget.setRowCount(len(events))
        self.tableWidget.setColumnCount(4)  # Dört sütun: Etkinlik Adı, Başlangıç Zamanı, Katılımcılar, Organizatör
        self.tableWidget.setHorizontalHeaderLabels(['Etkinlik Adı', 'Başlangıç Zamanı', 'Katılımcı Mail Adresleri', 'Organizatör Mail Adresi'])

        for i, event in enumerate(events):
            summary = event.get('summary', 'No Title')
            start = event['start'].get('dateTime', event['start'].get('date'))
            # Etkinliğe katılanların e-posta adreslerini al (varsa)
            attendees_emails = ', '.join([attendee['email'] for attendee in event.get('attendees', []) if 'email' in attendee])
            # Organizatörün e-posta adresini al
            organizer_email = event.get('organizer', {}).get('email', 'No Organizer Email')

            # tableWidget'a etkinlik bilgilerini ekle
            self.tableWidget.setItem(i, 0, QTableWidgetItem(summary))
            self.tableWidget.setItem(i, 1, QTableWidgetItem(start))
            self.tableWidget.setItem(i, 2, QTableWidgetItem(attendees_emails))
            self.tableWidget.setItem(i, 3, QTableWidgetItem(organizer_email))


    def mail_gonder(self):
        try:
            # Define the path to your service account credentials JSON file
            creds_path = r'C:\Users\dell\OneDrive\Masaüstü\CRM_V3_G2\CRM_V3\key.json'

            # Define the scope of access for the Google Sheets API
            scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']

            # Authenticate using the service account credentials
            creds = ServiceAccountCredentials.from_json_keyfile_name(creds_path, scope)

            # Authorize gspread with the credentials
            gc = gspread.authorize(creds)

            # Open the Google Sheet named 'Basvurular'
            spreadsheet = gc.open('Basvurular')

            # Get the first worksheet from the spreadsheet (index 0)
            worksheet = spreadsheet.get_worksheet(0)

            # Retrieve all values from the email column (assuming email addresses are in the second column)
            email_column = worksheet.col_values(3)[1:]  # Exclude the header row

            # Email configuration
            sender_email = "werherevit@gmail.com"  # Your Gmail address
            sender_password = "projectgroup"  # Your Gmail password

            # Connect to Gmail's SMTP server
            server = smtplib.SMTP('smtp.gmail.com', 587)
            server.starttls()
            server.login(sender_email, sender_password)

            # Email content
            subject = "TEST"
            body = "Group 2 test e-maili, Lütfen yanıt vermeyin"

            for email in email_column:
                # Create message container
                message = MIMEMultipart()
                message['From'] = sender_email
                message['To'] = email
                message['Subject'] = subject

                # Attach the body to the message
                message.attach(MIMEText(body, 'plain'))

                # Send the message via Gmail's SMTP server
                server.send_message(message)

                # Clear the message container
                del message

            # Quit the SMTP server
            server.quit()

        except Exception as e:
            # Handle any exceptions that occur during the process
            print("An error occurred:", e)

    def geri_don(self):
        tercih_menu_admin.show()
        self.hide()

app = QApplication(sys.argv)
proje_arayuz = ProjeArayuz()
tercih_menu = TercihMenu()
tercih_menu_admin = TercihMenuAdmin()
basvurular_sayfasi = BasvurularSayfasi()
mulakatlar = Mulakatlar()
mentor_gorusme_sayfasi = MentorGorusmeSayfasi()
admin_menu = AdminMenu()

proje_arayuz.show()
sys.exit(app.exec())