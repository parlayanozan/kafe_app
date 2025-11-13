from dataclasses import dataclass
from typing import List

# Kahve yapımında kullanılan hammaddeleri tutar.
@dataclass
class Hammadde:
    ad: str

# Kullanılan hammadde ve miktarını tutar. Bunu liste olarak Siparis içinde kullanacağız.
@dataclass
class HammaddeMiktari:
    hammadde: Hammadde
    adet: int

@dataclass
class Siparis:
    kahve_adi: str
    fiyat: int
    kullanilanlar: List[HammaddeMiktari]

    def aciklama_olustur(self) -> str:
        parcalari = []

        for item in self.kullanilanlar:
            adet = str(item.adet)
            ad = item.hammadde.ad
            parca = adet + "x " + ad # Bu daha sonra dört doz gibi sayısal ifade edilecek şekilde güncellenecek
            parcalari.append(parca)

        tarif = ", ".join(parcalari)

        mesaj = (
            self.kahve_adi + " seçtiniz. Bu içeceğimiz " + tarif + " içermektedir. Afiyet olsun."
        )

        return mesaj
