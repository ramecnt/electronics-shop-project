"""Здесь надо написать тесты с использованием pytest для модуля item."""

import pytest
from src.item import Item

test_item = Item('Test', 12000, 5)
test_item.pay_rate = 1.2


def test_calculate_total_price():
    assert test_item.price * test_item.quantity == test_item.calculate_total_price()


def test_apply_discount():
    usuall_price = test_item.price * test_item.pay_rate
    test_item.apply_discount()
    price = test_item.price
    assert usuall_price == price


def test_name():
    test_item.name = "SuperTester"
    assert test_item.name == "SuperTeste"


def test_str_to_int():
    assert Item.string_to_number('24.8') == 24
    assert Item.string_to_number('3') == 3


def test_instantiate_from_csv():
    Item.instantiate_from_csv('./src/items.csv')
    assert len(Item.all) == 5

    item3 = Item.all[3]
    assert item3.price == 50
    assert item3.quantity == 5


def test_repr_str():
    assert repr(test_item) == "Item('SuperTeste', 14400, 5)"
    assert str(test_item) == "SuperTeste"
