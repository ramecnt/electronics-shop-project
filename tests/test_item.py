"""Здесь надо написать тесты с использованием pytest для модуля item."""

import pytest
from src.item import Item, InstantiateCSVError


class TestItem:
    test_item = Item('Test', 12000, 5)
    test_item.pay_rate = 1.2

    def test_calculate_total_price(self):
        assert self.test_item.price * self.test_item.quantity == self.test_item.calculate_total_price()

    def test_apply_discount(self):
        usuall_price = self.test_item.price * self.test_item.pay_rate
        self.test_item.apply_discount()
        price = self.test_item.price
        assert usuall_price == price

    def test_name(self):
        self.test_item.name = "SuperTester"
        assert self.test_item.name == "SuperTeste"

    def test_str_to_int(self):
        assert Item.string_to_number('24.8') == 24
        assert Item.string_to_number('3') == 3

    def test_instantiate_from_csv(self):
        Item.instantiate_from_csv('../src/items.csv')
        assert len(Item.all) == 5

        item3 = Item.all[3]
        assert item3.price == 50
        assert item3.quantity == 5
        with pytest.raises(FileNotFoundError):
            Item.instantiate_from_csv('../src/item.csv')
        with pytest.raises(InstantiateCSVError):
            Item.instantiate_from_csv('../src/wrong.csv')


    def test_repr_str(self):
        assert repr(self.test_item) == "Item('SuperTeste', 14400, 5, 1.2)"
        assert str(self.test_item) == "SuperTeste"

