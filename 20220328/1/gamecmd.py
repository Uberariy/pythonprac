"""Содержимое этого файла в основном используется для работы с интеративной командной 
строкой.
"""

import shlex
import cmd
from .gameobjects import Cage, Player

Field = [[Cage(0) for i in range(10)] for j in range(10)]
Pl1 = Player()


class Repl(cmd.Cmd):
    """Класс интерактивной коммандной строки"""
    prompt = "[DNGN]:~$ "

    def do_add(self, arg):
        """Добавить в клетку с заданными координатами монстра с заданным именем 
        и числом очков здоровья. Если в этой клетке уже есть монстр с таким именем, 
        его число очков здоровья меняется на новое.
        """
        args = shlex.split(arg, comments=True)
        if len(args) != 8:
            print("(Not enough/Too many) arguments")
        else:
            Xy = [int(args[args.index("coords")+1]), int(args[args.index("coords")+2])]
            Field[Xy[0]][Xy[1]].addmonstr(args[args.index("name")+1],
                                          int(args[args.index("hp")+1]))
            print("Added {} at ({}, {}) hp {}".format(args[args.index("name")+1],
                                                      Xy[0], Xy[1], args[args.index("hp")+1]))

    def complete_add(self, text, allcommand, beg, end):
        return [s for s in ["monster", ] if s.startswith(text)]

    def do_show(self, arg):
        """Вывести про каждого монстра на отдельной строке информацию: его имя, 
        координаты, число очков здоровья.
        """
        args = shlex.split(arg, comments=True)
        if len(args) != 1:
            print("(Not enough/Too many) arguments")
        else:
            for x, j in enumerate(Field):
                for y, i in enumerate(j):
                    for m in i.monsters:
                        print(f"{m.name} at {x} {y} hp {m.hp}")

    def complete_show(self, text, allcommand, beg, end):
        return [s for s in ["monsters", ] if s.startswith(text)]

    def do_move(self, arg):
        """Подвинуть игрока на одну клетку в заданном направлении 
        (варианты: up, down, left, right), если это возможно с учетом границ поля; 
        up, down - смещение по оси Y; left, right - по оси X
        """
        args = shlex.split(arg, comments=True)
        if len(args) != 1:
            print("(Not enough/Too many) arguments")
        else:
            tmp = Pl1.coords
            Pl1.coords = [Pl1.coords[0] + int(args[0] == "right") - int(
                args[0] == "left"), Pl1.coords[1] + int(args[0] == "down") - int(args[0] == "up")]
            for i in Pl1.coords:
                if (i < 0) or (i > 9):
                    print("Cannot move")
                    Pl1.coords = tmp
                    break
            else:
                print(f"Player at ({Pl1.coords[0]} {Pl1.coords[1]})", end="")
                if (len(Field[Pl1.coords[0]][Pl1.coords[1]].monsters) > 0):
                    print(", encountered:")
                else:
                    print("")
                [print(f" - {i.name} {i.hp} hp")
                 for i in Field[Pl1.coords[0]][Pl1.coords[1]].monsters]

    def complete_move(self, text, allcommand, beg, end):
        return [s for s in ["up", "down", "left", "right"] if s.startswith(text)]

    def do_attack(self, arg):
        """Атаковать монстра с заданным именем, находящегося в той же клетке, где игрок.
        Атака списывает у монстра 10 очков здоровья;
        """
        args = shlex.split(arg, comments=True)
        PlField = Field[Pl1.coords[0]][Pl1.coords[1]]
        monstershere = [i.name for i in PlField.monsters]
        if len(args) != 1:
            print("(Not enough/Too many) arguments")
        elif args[0] in monstershere:
            PlField.monsters[monstershere.index(args[0])].hp -= 10
            if (PlField.monsters[monstershere.index(args[0])].hp <= 0):
                print(f"{args[0]} dies!")
                PlField.monsters.pop(monstershere.index(args[0]))
            else:
                monstrhp = PlField.monsters[monstershere.index(args[0])].hp
                print(f"{args[0]} lost 10 hp, now has {monstrhp} hp")
        else:
            print(f"No {args[0]} here")

    def complete_attack(self, text, allcommand, beg, end):
        PlField = Field[Pl1.coords[0]][Pl1.coords[1]]
        return [s for s in [i.name for i in PlField.monsters] if s.startswith(text)]

    def do_q(self, arg):
        """Экзитскам.
        """
        print("Exiting!")
        return True
