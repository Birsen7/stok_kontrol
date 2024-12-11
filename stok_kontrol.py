import json


stok = {}


def stok_dosyasi_oku():
    global stok
    try:
        with open("stok.json", "r") as file:
            stok = json.load(file)
    except FileNotFoundError:
        stok = {}
    except json.JSONDecodeError:
        stok = {}


def stok_dosyasi_yaz():
    with open("stok.json", "w") as file:
        json.dump(stok, file)


def stok_ekle(urun, miktar):
    if miktar <= 0:
        print("Hata: Miktar 0'dan büyük olmalıdır.")
        return
    if urun in stok:
        stok[urun] += miktar
    else:
        stok[urun] = miktar
    stok_dosyasi_yaz() 
    print(f"{urun} için {miktar} adet eklendi.")


def stok_guncelle(urun, yeni_miktar):
    if urun in stok:
        if yeni_miktar <= 0:
            print("Hata: Yeni miktar 0'dan büyük olmalıdır.")
            return
        stok[urun] = yeni_miktar
        stok_dosyasi_yaz()  
        print(f"{urun} miktarı {yeni_miktar} olarak güncellendi.")
    else:
        print(f"{urun} stokta yok.")


def stok_sil(urun):
    if urun in stok:
        del stok[urun]
        stok_dosyasi_yaz()  
        print(f"{urun} stoktan silindi.")
    else:
        print(f"{urun} stokta yok!")


def stok_listele():
    if stok:
        print("Stokta bulunan ürünler:")
        for urun, miktar in stok.items():
            print(f"{urun}: {miktar} adet.")
    else:
        print("Stokta ürün bulunmuyor.")


def urun_sorgula(urun):
    if urun in stok:
        print(f"{urun} miktarı: {stok[urun]} adet.")
    else:
        print(f"{urun} stokta yok!")


def ana_menu():
    while True:
        print("\nStok Takip Sistemi")
        print("1. Stok Ekle")
        print("2. Stok Güncelle")
        print("3. Stok Sil")
        print("4. Stok Listele")
        print("5. Ürün Sorgula")
        print("6. Çıkış")
        
        secim = input("Bir seçenek giriniz (1-6): ")
        
        if secim == "1":
            urun = input("Eklenecek ürün adı: ")
            try:
                miktar = int(input("Eklenecek miktar: "))
                stok_ekle(urun, miktar)
            except ValueError:
                print("Hata: Lütfen geçerli bir sayı girin.")
        elif secim == "2":
            urun = input("Güncellenecek ürün adı: ")
            try:
                yeni_miktar = int(input("Yeni miktar: "))
                stok_guncelle(urun, yeni_miktar)
            except ValueError:
                print("Hata: Lütfen geçerli bir sayı girin.")
        elif secim == "3":
            urun = input("Silinecek ürün adı: ")
            stok_sil(urun)
        elif secim == "4":
            stok_listele()
        elif secim == "5":
            urun = input("Sorgulamak istediğiniz ürün adı: ")
            urun_sorgula(urun)
        elif secim == "6":
            print("Programdan çıkılıyor...")
            break
        else:
            print("Geçersiz seçim! Lütfen 1-6 arasında bir sayı girin.")

stok_dosyasi_oku()

ana_menu()