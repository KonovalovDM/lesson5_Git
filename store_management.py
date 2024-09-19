# Создаем класс 'Stor'
class Store:
    def __init__(self, name, address):
        self.name = name
        self.address = address
        self.items = {}

    def add_item(self, item_name, price):
        """Добавляет товар в ассортимент."""
        self.items[item_name] = price

    def remove_item(self, item_name):
        """Удаляет товар из ассортимента."""
        if item_name in self.items:
            del self.items[item_name]
        else:
            print(f"Товар '{item_name}' отсутствует в ассортименте.")

    def get_price(self, item_name):
        """Возвращает цену товара, если он есть в ассортименте, иначе возвращает None."""
        return self.items.get(item_name, None)

    def update_price(self, item_name, new_price):
        """Обновляет цену товара."""
        if item_name in self.items:
            self.items[item_name] = new_price
        else:
            print(f"Товар '{item_name}' отсутствует в ассортименте.")

    def __str__(self):
        return f"Магазин: {self.name}, Адрес: {self.address}, Ассортимент: {self.items}"

# Создаем объекты класса 'Stor'
# Создаем три магазина
store1 = Store("\nМагазин №1", "ул. Ленина, д. 1")
store2 = Store("\nМагазин №2", "ул. Пушкина, д. 2")
store3 = Store("\nМагазин №3", "ул. Чехова, д. 3")

# Добавляем товары в каждый магазин
store1.add_item("яблоки", 0.5)
store1.add_item("бананы", 0.75)

store2.add_item("апельсины", 0.8)
store2.add_item("груши", 1.0)

store3.add_item("вишня", 2.0)
store3.add_item("виноград", 1.5)

### Тестирование методов

# Выбираем первый магазин для тестирования
print(store1)

# Добавляем товар
store1.add_item("киви", 1.2)
print("\nПосле добавления киви:", store1)

# Обновляем цену
store1.update_price("яблоки", 0.55)
print("\nПосле обновления цены на яблоки:", store1)

# Запрашиваем цену
price = store1.get_price("бананы")
print(f"\nЦена на бананы: {price}")

# Удаляем товар
store1.remove_item("бананы")
print("\nПосле удаления бананов:", store1)

# Попытка получить цену удаленного товара
price = store1.get_price("бананы")
print(f"\nЦена на бананы после удаления: {price}")


