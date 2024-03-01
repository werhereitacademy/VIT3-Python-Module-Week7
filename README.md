# VIT3-Python-Module-Week7

* Bu odevimizde https://werhere-it-academy.gitbook.io/werhere-it-academy-handbook/python-modulu/modul-project/crm.v2 sayfasinda olan  python modulu bitirme projesinin arayuzunu ozgun bir calisma ile tamamlamaniz beklenmektedir.

## Arayüz giriş penceresi
* Uygulamaya özelleştirilmiş bir giriş sayfası oluşturunuz.  Bu sayfa asagidaki ozellikleri icersin
1. Kullanici ve sifre icin iki ayrı input ogesi.
2. Bu iki bilgiye reaksiyon verecek ve sonraki bir giris buton.
3. Butonun tiklandiginda basarili olup olmadigini bildirecek bir uyari yazisi.
* Istege gore uygulamayi kapatacak baska bir buton ekleyip pencere goruntusunu kaldirabilirsiniz.
* Tutarli ardalan renkleri , kutu kenar sekilleri, buton ozellikleri (hover, pressed, yuvarlak kenar), yazilar icin farkli fontlar ve renkler kullanarak ozellesmis ve  giris penceresi olusturunuz.
* Ipucu: Once bir frame yerlestirip ogeleri ustune yerlestirerek, hem frame i hem de uzerine yerlestirdiginiz ogeleri layout,spacer kullanarak dinamik boyut olusturabilirsiniz.

## Tercih-Menu
* Basariyla giris yapan bir kullaniciya uc farkli pencereye yonlendirecek uc buton gostermeli.
1. Basvurular Menü-basvurular butonu kullaniciyi ilk basvuru penceresine yönlendirmelidir.
2. Mentor Gorusmesi-mentor gorusmesi butonu kullaniciyi mentor penceresine yonlendirmeli
3 .Mulakatlar-mulakatlar butonu kullaniciyi mulakatlar penceresine yonlendirmeli
4 .Kapat-Uygulamadan cikma butonu ekleyiniz
* Bunun, bir onceki giris penceresiyle (renk,bicim vs.) tutarli bir sekilde farklilastiriniz.

## Tercih-Admin-Menu
* Basariyla giris yapan bir admini dört farkli pencereye yonlendirecek dört farlı buton gostermeli.
1. Tercih-Menü’nün ulaştığı 3 ayrı menüye ulaşabildiği gibi, aynı zamanda Admin  Menü’ye de ulaşabilmelidir.
2. Kapat-Uygulamadan cikma butonu içermelidir. 
* Pencereler, bir onceki pencerelerle (giriş) (renk,bicim vs.) tutarli bir sekilde farkli olmalıdır. 

## Basvurular Sayfasi
* Tercihlerden Basvurular butonuna tiklandiginda acilacak arayuz. Su ogeleri icermelidir.
1. Ara butonu ve Input kutusu -text girilecek bir kutu ve arama fonksiyonu ekleyecegimiz bir buton
2. Tum Basvurular butonu: Basvurular dosyasındaki tüm kayıtları göstermelidir. 
3. Mentor Gorusmesi Tanimlananlar butonu: Basvurular dosyasındaki İlgili Sutundaki verileri ekranda göstermelidir. 
4. Mentor Gorusmesi Tanimlanmayanlar butonu: Basvurular dosyasındaki İlgili Sutundaki verileri ekranda göstermelidir. 
5. Ustteki uc butonun cagiracagi verileri cagirildiginda ekranda kolonlar ve satirlar seklinde gosterilmesini saglayacak 7 sutunluk bir tablo.  
6. Tercihler Ekranina Geri Don Butonu - Tercihler Menusüne dönmeyi saglayacak bir buton. Not: Eğer giriş yapan kişi admin’se Tercihler-Admin Ekranına geri döndürmelidir.
* Her pencere tasarımları diğer pencere tasarımlarıyla (renk,bicim, butonlarin cerceve kenarligi renkleri, tablonun saydam ardalan rengi vs.) tutarli bir sekilde farklilastirılmalıdır.
* Buraya yoğunluk durumunuza göre isterseniz eğer, VIT1 ve VIT2 dosya kayıtlarını gösteren ayrı butonlar’da ekleyebilirsiniz.
* Yine bu sayfayi diger sayfalarla (renk,bicim, butonlarin cerceve kenarligi renkleri, tablonun saydam ardalan rengi vs.) tutarli bir sekilde farklilastiriniz. 

## Mentor Gorusmesi Sayfasi
* Mentor Gorusmesi butonuna basildiginda acilacak arayuz. Su ogeleri icermeli:
1. Ara butonu ve Input kutusu -text girilecek bir kutu ve arama fonksiyonu ekleyecegimiz bir buton
2. Tum Gorusmeler- Mentor Dosyasındaki tüm verileri tabloya cagiracak bir butondur.  
3. Coklu sekme - ustune gelindiginde asagi dogru acilarak birden fazla secenek gosteren bir arac ekleyiniz. Ipucu: Combobox> Edit Items. Not: Coklu Sekme verilerini Mentor Dosyası 2.sayfa’da bulabilirsiniz! Bu sekme Mentor Dosyasındaki ilgili sutundaki bu verileri ekrana yazdırma işlevi görür. 
* ipucu: Combobox> Edit Items
4. Tercihler Ekranina Geri Don butonu.
Not: Eğer giriş yapan kişi admin’se Tercihler-Admin Ekranına geri dönmeli

## Mulakatlar sayfasi
* Menu sayfasinda mulakatlar butonuna basilinca cagiralacak arayuz. Su ogeleri icermeli:
1. Ara butonu ve Input kutusu -text girilecek bir kutu ve arama fonksiyonu ekleyecegimiz bir buton
2. Projesi Gonderilenler Butonu: Mulakatlar Dosyasındaki ilgili Sutundaki veriler ekranda gözükmelidir. 
3. Projesi Gelmis Olanlar Butonu: Mulakatlar Dosyasındaki ilgili Sutundaki veriler ekranda gözükmelidir. 
4. Tercihler ekranina geri don butonu. Not: Eğer giriş yapan kişi admin’se Tercihler-Admin Ekranına geri dönmelidir.
* Her sayfanin etrafindaki pencere goruntusunu silip yerine aplikasyonu kapatma butonu ekleyebilirsiniz.

## Admin Menü
1. Etkinlik Kaydı Butonu
Etkinlik Kaydı Butonu’na tıklandığında Google Takvimde’ yer alan Etkinliklerin kayıtlarını ekrana getirmeli. Burda e-mail adreslerini, toplantı konum vb özellikleri eklemek tercihinize kalmış. Format Toplantı Başlığı, Başlangıç Zamanı, katılımcı mail adresi ve organizatör mail adresi şeklinde oluşturuldu. 
2. Mail Butonu
Mail Butonu’na tıklandığında Google Takvim’de bulunan etkinliklerdeki kayıtlı e-mail adreslerine mail gönderilmesi sağlanmalı. Tercih edilmesi durumunda mail iletildi bilgisi de mesaj olarak ekranda gösterilebilir.
3. Tercihler-Admin Ekranina Geri Don Butonu
Tercihler-Admin Ekranina Geri Don butonu tiklandiginda admin Tercihler-Admin ekranina geri dönmeli
4. Çıkış Butonu
* Çıkış Butonu tiklandiginda admin uygulamadan çıkmalı. 


## Sayfa Gecisi
* Giris sayfasindaki, Tercihler menusundeki ve her sayfadaki 'Tercihler ekranina geri don' butonlarina islev kazandiracak fonksiyonlari ekleyip, sayfalar arasi gecisleri test ediniz.

## Hackerrank Questions

1. Utopian Tree: https://www.hackerrank.com/challenges/utopian-tree/problem
