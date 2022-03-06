import readline
import shlex
import cmd

class Player:
    coords = []
    def __init__(self, coords=[0, 0]):
        self.coords = coords

class Monster:
    name = 0
    hp = 0
    def __init__(self, name, hp=15):
        self.name = name;   self.hp = hp

class Cage:
    monsters = []   # Better use ditctionary
    def __init__(self, monstr_count):
        self.monsters = [Monster(f"Creep {i}") for i in range(monstr_count)]
        pass

    def addmonstr(self, name, hp):
        for ind, i in enumerate(self.monsters):
            if i.name == name:
                self.monsters.pop(ind)
        self.monsters.append(Monster(name, hp))


Field = [[Cage(0) for i in range(10)] for j in range(10)]
Pl1 = Player()

class Repl(cmd.Cmd):
    prompt = "[DNGN]:~$ "

    def do_add(self, arg):
        args = shlex.split(arg, comments=True)
        if len(args) != 8:
            print("(Not enough/Too many) arguments")
        else:
            Field[int(args[args.index("coords")+1])][int(args[args.index("coords")+2])].addmonstr(args[args.index("name")+1], int(args[args.index("hp")+1]))
            print("Added {} at ({}, {}) hp {}".format(args[args.index("name")+1], args[args.index("coords")+1], args[args.index("coords")+2], args[args.index("hp")+1]))

    def complete_add(self, text, allcommand, beg, end):
        return [s for s in ["monster",] if s.startswith(text)]

    def do_show(self, arg):
        args = shlex.split(arg, comments=True)
        if len(args) != 1:
            print("(Not enough/Too many) arguments")
        else:
            for x, j in enumerate(Field):
                for y, i in enumerate(j):
                    for m in i.monsters:
                        print(f"{m.name} at {x} {y} hp {m.hp}")
    
    def complete_show(self, text, allcommand, beg, end):
        return [s for s in ["monsters",] if s.startswith(text)]

    def do_move(self, arg):
        args = shlex.split(arg, comments=True)
        if len(args) != 1:
            print("(Not enough/Too many) arguments")
        else:
            tmp = Pl1.coords
            Pl1.coords = [Pl1.coords[0] + int(args[0]=="right") - int(args[0]=="left"), Pl1.coords[1] + int(args[0]=="down") - int(args[0]=="up")]
            for i in Pl1.coords:
                if (i < 0) or (i > 9):
                    print("Cannot move")
                    Pl1.coords = tmp
                    break
            else:
                print(f"Player at ({Pl1.coords[0]} {Pl1.coords[1]})", end = "")
                if (len(Field[Pl1.coords[0]][Pl1.coords[1]].monsters) > 0):
                    print(", encountered:")
                else:
                    print("")
                [print(f" - {i.name} {i.hp} hp") for i in Field[Pl1.coords[0]][Pl1.coords[1]].monsters]


    def complete_move(self, text, allcommand, beg, end):
        return [s for s in ["up", "down", "left", "right"] if s.startswith(text)]

    def do_attack(self, arg):
        args = shlex.split(arg, comments=True)
        monstershere = [i.name for i in Field[Pl1.coords[0]][Pl1.coords[1]].monsters]
        if len(args) != 1:
            print("(Not enough/Too many) arguments")
        elif args[0] in monstershere:
            Field[Pl1.coords[0]][Pl1.coords[1]].monsters[monstershere.index(args[0])].hp -= 10
            if (Field[Pl1.coords[0]][Pl1.coords[1]].monsters[monstershere.index(args[0])].hp <= 0):
                print(f"{args[0]} dies!")
                Field[Pl1.coords[0]][Pl1.coords[1]].monsters.pop(monstershere.index(args[0]))
            else:
                print(f"{args[0]} lost 10 hp, now has {Field[Pl1.coords[0]][Pl1.coords[1]].monsters[monstershere.index(args[0])].hp} hp")
        else:
            print(f"No {args[0]} here")            
    
    def complete_attack(self, text, allcommand, beg, end):
        return [s for s in [i.name for i in Field[Pl1.coords[0]][Pl1.coords[1]].monsters] if s.startswith(text)]

    def do_q(self, arg):
        print("Exiting!")
        return True


Repl().cmdloop()