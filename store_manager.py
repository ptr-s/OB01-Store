"""
*Дополнительное задание:
Ты разрабатываешь программное обеспечение для сети магазинов. Каждый магазин
в этой сети имеет свои особенности, но также существуют общие характеристики,
такие как адрес, название и ассортимент товаров. Ваша задача — создать класс
`Store`, который можно будет использовать для создания различных магазинов.

Шаги:

1. Создай класс `Store`:
-Атрибуты класса:
- `name`: название магазина.
- `address`: адрес магазина.
- `items`: словарь, где ключ - название товара, а значение - его цена. Например,
    `{'apples': 0.5, 'bananas': 0.75}`.
- Методы класса:
- `__init__ - конструктор, который инициализирует название и адрес, а также пустой словарь для `items`.
- метод для добавления товара в ассортимент.
- метод для удаления товара из ассортимента.
- метод для получения цены товара по его названию. Если товар отсутствует, возвращайте `None`.
- метод для обновления цены товара.

2. Создай несколько объектов класса `Store`:
Создай не менее трех различных магазинов с разными названиями, адресами и добавь
в каждый из них несколько товаров.

3. Протестировать методы:
Выбери один из созданных магазинов и протестируй все его методы: добавь товар,
обнови цену, убери товар и запрашивай цену.
"""

class Store():
    def __init__(self, name: str, address: str):
        self.name = name
        self.address = address
        self.items = {}

    def info(self):
        print(f"Магазин '{self.name}' по адресу '{self.address}'")

    def show_goods(self):
        for goods_name, goods_price in self.items.items():
            print(f"товар '{goods_name}' по цене {goods_price}")

    def add_goods(self, name: str, price: float):
        if not name in self.items:
            self.items[name] = price
            print(f"добавлен товар '{name}' по цене {price}")
        else:
            print(f"Ошибка при добавлении товара, товар '{name}' уже существует")

    def remove_goods(self, name: str):
        if name in self.items:
            self.items.pop(name, None)
            print(f"товар '{name}' удален")
        else:
            print(f"товар '{name}' не найден")

    def get_price(self, name: str):
        if name in self.items:
            return self.items[name]
        else:
            return None

    def set_price(self, name: str, price: float):
        if name in self.items:
            self.items[name] = price
            print(f"цена на товар '{name}' изменена, новая цена: {price}")
        else:
            print(f"товар '{name}' не найден")


def main():
    print("")
    # Магазин №1: Шестёрочка, ул. Вавилова, 13
    store1 = Store("Шестёрочка", "ул. Вавилова, 13")
    store1.info()
    store1.add_goods("яблоки", 69.5)
    store1.add_goods("апельсины", 78.6)
    store1.add_goods("картошка", 39.5)
    store1.add_goods("капуста", 41.5)

    print("")
    # Магазин №2: Пыжик, ул. Фонвизина, 3
    store2 = Store("Пыжик", "ул. Фонвизина, 3")
    store2.info()
    store2.add_goods("молоко", 80)
    store2.add_goods("сыр", 950)
    store2.add_goods("масло", 160)
    store2.add_goods("кефир", 85)

    print("")
    # Магазин №3: GNS, проспект Мира, 24
    store3 = Store("GNS", "проспект Мира, 24")
    store3.info()
    store3.add_goods("скороварка", 1200)
    store3.add_goods("печка", 3000)
    store3.add_goods("соковыжималка", 5000)

    print("")
    # работа с магазином №1
    store1.info()

    # добавим один новый товар
    store1.add_goods("томаты", 120)
    # удалим один товар
    store1.remove_goods("яблоки")
    # обновим цену
    store1.set_price("апельсины", 95)
    # посмотрим цену одно товара
    price = store1.get_price("картошка")
    if price:
        print(f"товар 'картошка' по цене {price}")
    else:
        print(f"товар 'картошка' не найден")

    # распечатаем список всех товаров
    print(f"\nитоговый список всех товаров в магазине '{store1.name}':")
    store1.show_goods()


if __name__ == "__main__":
    main()