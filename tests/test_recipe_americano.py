from menu import Menu

def test_americano_recipe():
    menu = Menu()
    s = menu.siparis_olustur(6)

    assert len(s.kullanilanlar) == 2

    espresso = s.kullanilanlar[0]
    su = s.kullanilanlar[1]

    assert espresso.hammadde.ad == "Espresso"
    assert espresso.adet == 1

    assert su.hammadde.ad == "Hot Water"
    assert su.adet == 4
