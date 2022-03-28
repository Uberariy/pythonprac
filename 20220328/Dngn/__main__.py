import readline
import shlex
import cmd
from .gamecmd import Repl

if __name__ == '__main__':
	Repl().cmdloop()
