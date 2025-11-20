from menu import Menu
from OrderMessageBuilder import SiparisAciklayici
from exceptions import InvalidCoffeeCodeError


def main():
    menu = Menu()
    aciklayici = SiparisAciklayici()

    print("Kafe Sipariş Uygulamasına Hoş Geldiniz!\n")

    while True:
        print("Menü:")
        for kod, ad, fiyat in menu.menu_icerikleri():
            print(f"{kod}. {ad} ({fiyat} ₺)")

        print("\nÇıkmak için 'exit' yazabilirsiniz.\n")

        secim = input("Lütfen içmek istediğiniz kahvenin numarasını giriniz: ").strip()

        if secim.lower() == "exit":
            print("Uygulamadan çıkılıyor. İyi günler.")
            return

        if not secim.isdigit():
            print("Geçersiz giriş. Lütfen bir sayı ya da 'exit' yazınız.\n")
            continue

        kod = int(secim)

        try:
            siparis = menu.siparis_olustur(kod)
        except InvalidCoffeeCodeError:
            print("Geçersiz kahve numarası.\n")
            continue

        print("\nTeşekkürler, kahveniz hazırlanıyor.\n")

        aciklama = aciklayici.aciklama_olustur(siparis)
        print(aciklama)
        print()

        break


if __name__ == "__main__":
    main()
