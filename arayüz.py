from Kütüphane import *
print("""Sisteme Hoş Geldiniz
1. Ürünleri Gör
2. Stok Düzenle
3. Ürün Ekle
4. Ürün Ara
5. Üürn sil
Çıkış için q""")
islem = Kutuphane()
while True:
    cevap = input("Lütfen İşlem Seçiniz:")
    if cevap == "q":
        print("Çıkış yapılıyor...")
        time.sleep(1)
        break
    elif cevap == "1":
        islem.Urun_goster()
    elif cevap == "2":
        try:
            isim = input("isim yaz:")
            miktar = int(input("miktar yaz:"))
            isim = isim.upper()
            islem.stock_ekle(isim, miktar)
        except:
            print("hatalı işlem")
    elif cevap == "3":
        print("lütfem gereken bilgileri giriniz")
        tur = input("Tür: ")
        isim = input("İsim: ")
        stock = int(input("Stok: "))
        print("Lütfen bekleyin ürünler ekleniyor...")
        time.sleep(1)
        tur = tur.upper()
        isim = isim.upper()
        yeni_urun = Good(tur,isim,stock)
        islem.Urun_ekle(yeni_urun)
        print("Ürünler eklendi")

    elif cevap == "4":
        soru = input("""
        1. Türe Göre Arama
        2. İsme Göre Arama
        İşlem Seçiniz: """)
        if soru == "1":
            tur = input("Tür İsimini Yazınız:")
            tur =tur.upper()
            print(tur, "Türündeki Meyveler Şunlar:")
            islem.Tur_arama(tur)
        elif soru =="2":
            isim = input("Meyve İsmini Giriniz")
            isim= isim.upper()
            islem.Isim_arama(isim)
    elif cevap =="5":
        isim = input("silinecek ürünün ismini giriniz: ")
        isim = isim.upper()
        islem.Sil(isim)

