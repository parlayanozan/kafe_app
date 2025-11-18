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

    
