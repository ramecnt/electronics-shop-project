import csv


class Item:
    """
    Класс для представления товара в магазине.
    """
    pay_rate = 1.0
    all = []

    def __init__(self, name: str, price: float, quantity: int) -> None:
        """
        Создание экземпляра класса item.

        :param name: Название товара.
        :param price: Цена за единицу товара.
        :param quantity: Количество товара в магазине.
        """
        self._name = name
        self.price = price
        self.quantity = quantity
        self._append()

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({str(list(self.__dict__.values()))[1:-1]})"

    def __str__(self) -> str:
        return self._name

    def __add__(self, other):
        if issubclass(other.__class__, self.__class__):
            return other.quantity + self.quantity

    def calculate_total_price(self) -> float or int:
        """
        Рассчитывает общую стоимость конкретного товара в магазине.

        :return: Общая стоимость товара.
        """
        return self.price * self.quantity

    def apply_discount(self) -> None:
        """
        Применяет установленную скидку для конкретного товара.
        """
        k = self.price * self.pay_rate
        self.price = int(k) if str(k)[-1] == "0" else k

    def _append(self) -> None:
        """
        Скрытый метод добавляющиий экземпляр класса в атрибут all.
        """
        self.all.append(self)

    @property
    def name(self) -> str:
        return self._name

    @name.setter
    def name(self, name) -> str or None:
        if len(name) > 10:
            self._name = name[:10]
            print("Длина наименования товара превышает 10 символов.")
        else:
            self._name = name

    @classmethod
    def instantiate_from_csv(cls, file) -> None:
        cls.all.clear()
        with open(file, newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                cls(row["name"], int(row["price"]), int(row["quantity"]))

    @staticmethod
    def string_to_number(string) -> int:
        return int(float(string))
