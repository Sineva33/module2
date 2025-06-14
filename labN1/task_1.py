from typing import Optional

class CoffeeMachine:
    """Кофемашина с управлением водой и зернами"""
    def __init__(self, brand: str, water_capacity: int):
        if water_capacity <= 0:
            raise ValueError("Емкость воды должна быть > 0")
        self.brand = brand
        self._water = 0
        self._beans = 0
        self._max_water = water_capacity

    def add_water(self, ml: int) -> str:
        """Добавить воду (ml > 0)"""
        if ml <= 0:
            raise ValueError("Объем воды должен быть > 0")
        self._water = min(self._max_water, self._water + ml)
        return f"Добавлено {ml} мл воды"

    def make_coffee(self, size: str = "medium") -> str:
        """Приготовить кофе (small/medium/large)"""
        sizes = {"small": 100, "medium": 150, "large": 200}
        if self._water < sizes[size]:
            raise ValueError("Недостаточно воды")
        self._water -= sizes[size]
        return f"Готовим {size} кофе"

class SmartLamp:
    """Умная лампа с настройками"""
    def __init__(self, location: str):
        self.location = location
        self._brightness = 50
        self._is_on = False

    def toggle(self) -> str:
        """Включить/выключить лампу"""
        self._is_on = not self._is_on
        return f"Лампа {'включена' if self._is_on else 'выключена'}"

    def set_brightness(self, level: int) -> None:
        """Установить яркость (0-100)"""
        if not 0 <= level <= 100:
            raise ValueError("Яркость должна быть 0-100")
        self._brightness = level

if __name__ == "__main__":
    # Тестирование CoffeeMachine
    machine = CoffeeMachine("Bosch", 1000)
    print(machine.add_water(500))
    print(machine.make_coffee())

    # Тестирование SmartLamp
    lamp = SmartLamp("Гостиная")
    print(lamp.toggle())
    lamp.set_brightness(75)