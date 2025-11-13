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

    def siparis_olustur(self, kahve_kodu: int) -> Optional[Siparis]:
        """Kullanıcının seçtiği kahve numarasına göre Siparis nesnesi döner."""

        if kahve_kodu == 1:
            # Espresso (60 ₺) 1x Espresso
            return Siparis(
                kahve_adi="Espresso",
                fiyat=60,
                kullanilanlar=[
                    HammaddeMiktari(hammadde=self.espresso, adet=1),
                ],
            )

        if kahve_kodu == 2:
            # Double Espresso (90 ₺) 2x Espresso
            return Siparis(
                kahve_adi="Double Espresso",
                fiyat=90,
                kullanilanlar=[
                    HammaddeMiktari(hammadde=self.espresso, adet=2),
                ],
            )

        if kahve_kodu == 3:
            # Cappuccino (85 ₺)
            # 1x Espresso
            # 2x Steamed Milk
            # 2x Milk Foam
            return Siparis(
                kahve_adi="Cappuccino",
                fiyat=85,
                kullanilanlar=[
                    HammaddeMiktari(hammadde=self.espresso, adet=1),
                    HammaddeMiktari(hammadde=self.steamed_milk, adet=2),
                    HammaddeMiktari(hammadde=self.milk_foam, adet=2),
                ],
            )

        if kahve_kodu == 4:
            # Caffe Latte (95 ₺)
            # 1x Espresso
            # 3x Steamed Milk
            # 1x Milk Foam
            return Siparis(
                kahve_adi="Caffe Latte",
                fiyat=95,
                kullanilanlar=[
                    HammaddeMiktari(hammadde=self.espresso, adet=1),
                    HammaddeMiktari(hammadde=self.steamed_milk, adet=3),
                    HammaddeMiktari(hammadde=self.milk_foam, adet=1),
                ],
            )

        if kahve_kodu == 5:
            # Mocha (110 ₺)
            # 1x Espresso
            # 1x Steamed Milk
            # 1x Milk Foam
            # 2x Hot Chocolate
            return Siparis(
                kahve_adi="Mocha",
                fiyat=110,
                kullanilanlar=[
                    HammaddeMiktari(hammadde=self.espresso, adet=1),
                    HammaddeMiktari(hammadde=self.steamed_milk, adet=1),
                    HammaddeMiktari(hammadde=self.milk_foam, adet=1),
                    HammaddeMiktari(hammadde=self.hot_chocolate, adet=2),
                ],
            )

        if kahve_kodu == 6:
            # Americano (100 ₺)
            # 1x Espresso
            # 4x Hot Water
            return Siparis(
                kahve_adi="Americano",
                fiyat=100,
                kullanilanlar=[
                    HammaddeMiktari(hammadde=self.espresso, adet=1),
                    HammaddeMiktari(hammadde=self.sicak_su, adet=4),
                ],
            )

        if kahve_kodu == 7:
            # Hot Water (15 ₺)
            # 5x Hot Water
            return Siparis(
                kahve_adi="Hot Water",
                fiyat=15,
                kullanilanlar=[
                    HammaddeMiktari(hammadde=self.sicak_su, adet=5),
                ],
            )

        # Geçersiz kod girilirse None döndür
        return None
