import pytest
from menu import Menu
from exceptions import InvalidCoffeeCodeError


def test_espresso_siparis_olustur():
    menu = Menu()
    siparis = menu.siparis_olustur(1)

    assert siparis.kahve_adi == "Espresso"
    assert siparis.fiyat == 60
    assert len(siparis.kullanilanlar) == 1
    assert siparis.kullanilanlar[0].adet == 1


def test_invalid_code_throws_exception():
    menu = Menu()

    with pytest.raises(InvalidCoffeeCodeError):
        menu.siparis_olustur(999)
