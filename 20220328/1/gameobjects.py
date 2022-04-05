"""Данный файл определяет работу с геймобджектами Муда."""

class Player:
    """Класс игрока - юзера приложения."""
    coords = []

    def __init__(self, coords=[0, 0]):
        self.coords = coords


class Monster:
    """Класс монстра, блуждающего в поисках нуба."""
    name = 0
    hp = 0

    def __init__(self, name, hp=15):
        self.name = name
        self.hp = hp


class Cage:
    """Класс клетки (связаны) - минимального мерила игрового пространства."""
    monsters = []   # Better use ditctionary

    def __init__(self, monstr_count):
        self.monsters = [Monster(f"Creep {i}") for i in range(monstr_count)]
        pass

    def addmonstr(self, name, hp):
        """Подселить товарища-друга в клетку игрового пространства."""
        for ind, i in enumerate(self.monsters):
            if i.name == name:
                self.monsters.pop(ind)
        self.monsters.append(Monster(name, hp))
