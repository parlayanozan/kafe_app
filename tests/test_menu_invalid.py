import pytest
from menu import Menu
from exceptions import InvalidCoffeeCodeError

@pytest.mark.parametrize("wrong_code", [-1, 0, 8, 9, 999,"abc"])
def test_invalid_codes_throw_exception(wrong_code):
    menu = Menu()

    with pytest.raises(InvalidCoffeeCodeError):
        menu.siparis_olustur(wrong_code)
