from src.item import Item


class MixinLog:
    def __init__(self, name: str, price: float, quantity: int, language: str) -> None:
        super().__init__(name, price, quantity)
        self._language = language

    @property
    def language(self) -> str:
        return self._language

    def change_lang(self) -> None:
        if self._language == "EN":
            self._language = "RU"
        else:
            self._language = "EN"


class Keyboard(MixinLog, Item):
    def __init__(self, name: str, price: float, quantity: int, language: str = "EN") -> None:
        super().__init__(name, price, quantity, language)
