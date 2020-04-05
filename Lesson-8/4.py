class OfficeEquipment:
    def __init__(self, tech):
        self.tech = tech

    def work(self):
        return f'Включение'

    def sleep(self):
        return f'Выключение'

class Printer(OfficeEquipment):
    def __init__(self, tech):
        super().__init__(tech)
    def print(self):
        return f'Печать'

class Scanner(OfficeEquipment):
    def __init__(self, tech):
        super().__init__(tech)
    def scan(self):
        return f'Сканировать'

class Xerox(OfficeEquipment):
    def __init__(self, tech):
        super().__init__(tech)

    def copy(self):
        return f'Копировать'

p = Printer
s = Scanner
x = Xerox
