import sys
import pyfiglet
import gettext

translation = gettext.translation('task', 'po', fallback=True)
_, ngettext = translation.gettext, translation.ngettext


def solve(a, b):
    if (a != 0):
        return (-b / a)
    else:
        return None

if __name__ == "__main__":
    if len(sys.argv) == 3:
        res = solve(float(sys.argv[1]), float(sys.argv[2]))
        if res is None:
            print(pyfiglet.figlet_format(_("NO ROOTS"), font='graceful'))
        else:
            print(pyfiglet.figlet_format(_("Root: {}").format(res), font='graceful'))
    else:
        sys.exit("Wrong number of arguments.")

