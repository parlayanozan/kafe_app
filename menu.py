from typing import Optional

from models import Hammadde, HammaddeMiktari, Siparis

class Menu:
    """Menüdeki tüm kahve seçeneklerini ve sipariş oluşturma mantığını tutar."""

    def __init__(self) -> None:
        self.espresso = Hammadde(ad="Espresso")
        self.sicak_su = Hammadde(ad="Hot Water")
        self.steamed_milk = Hammadde(ad="Steamed Milk")
        self.milk_foam = Hammadde(ad="Milk Foam")
        self.hot_chocolate = Hammadde(ad="Hot Chocolate")

    def menu_icerikleri(self) :
        """Menüdeki kahve seçeneklerini döner. Bunu da (kod, ad, fiyat) olarak yapıyoruz.
         """
        return [
            (1, "Espresso", 60),
            (2, "Double Espresso", 90),
            (3, "Cappuccino", 85),
            (4, "Caffe Latte", 95),
            (5, "Mocha", 110),
            (6, "Americano", 100),
            (7, "Hot Water", 15),
            
        ]
    def _kahve_bilgisi_bul(self, kahve_kodu: int):
        for kod, ad, fiyat in self.menu_icerikleri():
            if kod == kahve_kodu:
                return ad, fiyat
        return None, None
    def _tarif_haritasi(self):
        return {
            1: [
                (self.espresso, 1),
            ],
            2: [
                (self.espresso, 2),
            ],
            3: [
                (self.espresso, 1),
                (self.steamed_milk, 2),
                (self.milk_foam, 2),
            ],
            4: [
                (self.espresso, 1),
                (self.steamed_milk, 3),
                (self.milk_foam, 1),
            ],
            5: [
                (self.espresso, 1),
                (self.steamed_milk, 1),
                (self.milk_foam, 1),
                (self.hot_chocolate, 2),
            ],
            6: [
                (self.espresso, 1),
                (self.sicak_su, 4),
            ],
            7: [
                (self.sicak_su, 5),
            ],
        }

    def siparis_olustur(self, kahve_kodu: int) -> Optional[Siparis]:
        ad, fiyat = self._kahve_bilgisi_bul(kahve_kodu)
        if ad is None:
            return None

        tarif_haritasi = self._tarif_haritasi()
        if kahve_kodu not in tarif_haritasi:
            return None

        kullanilanlar = []

        tarif_listesi = tarif_haritasi[kahve_kodu]
        for hammadde, adet in tarif_listesi:
            miktar = HammaddeMiktari(hammadde=hammadde, adet=adet)
            kullanilanlar.append(miktar)

        siparis = Siparis(
            kahve_adi=ad,
            fiyat=fiyat,
            kullanilanlar=kullanilanlar
        )

        return siparis
        # Geçersiz kod girilirse None döndür
        return None
