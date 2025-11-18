from menu import Menu


def main():
    menu = Menu()

    print("Kafe Sipariş Uygulamasına Hoş Geldiniz!\n")
    print("Menümüz bu şekildedir:\n")

    for kod, kahve_adi, kahve_fiyati in menu.menu_icerikleri():
        print(kod,"-", kahve_adi, ":", kahve_fiyati, "₺")
    secim = input("Lütfen içmek istediğiniz kahvenin numarasını giriniz: ")

    if not secim.isdigit():
        print("Geçersiz giriş. Lütfen sayı giriniz.")
        return

    kod = int(secim)
    siparis = menu.siparis_olustur(kod)

    if siparis is None:
        print("Geçersiz kahve numarası.")
        return

    print("\nTeşekkürler kahveniz hazırlanıyor.\n")
    print(siparis.aciklama_olustur())


if __name__ == "__main__":
    main()
