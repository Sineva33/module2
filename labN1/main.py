from task_1 import CoffeeMachine, SmartLamp

def test_coffee_machine():
    try:
        machine = CoffeeMachine("Philips", -500)
    except ValueError as e:
        print(f"Ошибка: {e}")

    machine = CoffeeMachine("Philips", 1000)
    print(machine.add_water(300))
    try:
        print(machine.make_coffee("large"))
    except ValueError as e:
        print(f"Ошибка: {e}")

def test_smart_lamp():
    lamp = SmartLamp("Спальня")
    print(lamp.toggle())
    try:
        lamp.set_brightness(150)
    except ValueError as e:
        print(f"Ошибка: {e}")

if __name__ == "__main__":
    test_coffee_machine()
    test_smart_lamp()