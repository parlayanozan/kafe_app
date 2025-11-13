from menu import Menu


def main():
    menu = Menu()

    print("Kafe Sipariş Uygulamasına Hoş Geldiniz!\n")
    print("1. Espresso (60 ₺)")
    print("2. Double Espresso (90 ₺)")
    print("3. Cappuccino (85 ₺)")
    print("4. Caffe Latte (95 ₺)")
    print("5. Mocha (110 ₺)")
    print("6. Americano (100 ₺)")
    print("7. Hot Water (15 ₺)\n")

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
