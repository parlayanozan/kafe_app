from models import Siparis, Hammadde, HammaddeMiktari
from OrderMessageBuilder import SiparisAciklayici


def test_order_description():
    espresso = Hammadde("Espresso")
    items = [HammaddeMiktari(hammadde=espresso, adet=1)]

    siparis = Siparis(
        kahve_adi="Espresso",
        fiyat=60,
        kullanilanlar=items
    )

    builder = SiparisAciklayici()
    result = builder.aciklama_olustur(siparis)

    assert "Espresso seçtiniz" in result
    assert "1 doz Espresso" in result
