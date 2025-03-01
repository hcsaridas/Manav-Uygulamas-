import sqlite3
import time

class Good():
    def __init__(self,tur,isim,stock):
        self.tur = tur
        self.isim = isim
        self.stock = stock
    def __str__(self):
        return "Tür: {}\nİsim: {}\nStok: {}\n".format(self.tur,self.isim,self.stock)

class Kutuphane():
    def __init__(self):
        self.baglanti_olustur()

    def baglanti_olustur(self):
        self.baglanti = sqlite3.connect("manav.db")
        self.cursor = self.baglanti.cursor()
        sorgu = "create table if not exists Manav (Tür TEXT,İSİM TEXT,STOK INT)"
        self.cursor.execute(sorgu)
        self.baglanti.commit()
    def baglantiyi_kes(self):
        self.baglanti.close()
    def Urun_goster(self):
        sorgu = "select * from Manav"
        self.cursor.execute(sorgu)
        Manav = self.cursor.fetchall()
        if len(Manav) == 0:
            print("Manavda Ürün Bulunamadı")
        else:
            for i in Manav:
                Manav2 = Good(i[0],i[1],i[2],)
                print(Manav2)
    def Urun_sorgula(self,isim):
        sorgu = "Select * from Manav ?"
        self.cursor.execute(sorgu,isim,)
        urun = self.cursor.fetchall()
        if len(urun) == 0:
            print("ürün bulunamadı")
        else:
            urun = Good([0][0],[0][1],[0][2])
            print(urun)
    def Urun_ekle(self,Good):
        sorgu = "insert into Manav Values(?,?,?)"
        self.cursor.execute(sorgu,(Good.tur,Good.isim,Good.stock),)
        self.baglanti.commit()
    def stock_ekle(self,isim,miktar):
        sorgu = "select STOK from Manav WHERE İSİM = ?"
        self.cursor.execute(sorgu,(isim,))
        asd = self.cursor.fetchall()
        if len(asd) == 0:
            print("Ürün Bulunamadı")
        else:
            mevcut_stok = asd[0][0]
            yeni_stock = mevcut_stok + miktar
            if yeni_stock < 0:
                print("Stok miktarı sıfırın altına düşemez")
                return
            sorgu = "update Manav set STOK = ? WHERE İSİM = ?"
            self.cursor.execute(sorgu,(yeni_stock,isim,))
            print("işem gerçekleşiyor..")
            time.sleep(1)
            self.baglanti.commit()

    def Tur_arama(self, tur):
        sorgu = "select * from Manav WHERE Tür = ?"
        self.cursor.execute(sorgu, (tur,))
        asd = self.cursor.fetchall()
        if len(asd) == 0:
            print("Ürün Bulunamadı")
        else:
            for i in asd:

                time.sleep(1)
                print(i[1],i[2])
    def Isim_arama(self,isim):
        sorgu = "select * from Manav Where İSİM = ?"
        self.cursor.execute(sorgu,(isim,))
        asd =self.cursor.fetchall()
        if len(asd) ==0:
            print("Ürün bulunamadı")
        else:
            for i in asd:
                print(isim, "için veriler yükleniyor...")
                time.sleep(1)
                print(i[0],i[2])
    def Sil(self,isim):
        sorgu = "select * from Manav Where İSİM = ?"
        self.cursor.execute(sorgu, (isim,))
        asd = self.cursor.fetchall()
        if len(asd) == 0:
            print("Ürün bulunamadı")
        else:
            sorgu = "delete from Manav where İSİM = ?"
            self.cursor.execute(sorgu,(isim,))
            self.baglanti.commit()
            print("işlem gerçekleştiriliyorr...")
            time.sleep(1)
            print("işlem baarılı")







