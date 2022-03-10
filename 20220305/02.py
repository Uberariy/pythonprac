import readline
import shlex
import cmd

class repl(cmd.Cmd):
    prompt = "> "

    def do_perform(self, arg):
        """
Variants:
        perform 
        """
        args = shlex.split(arg, comments=True)
        if len(args) < 1:
            return
        if args[0] == "sing":
            print("-".join(args[1:]))
        elif args[0] == "show":
            print(" ".join(args[1:].upper()))
        else:
            print(f"Don't know how to {args[0]}")
    
    def complete_perfrom(self, prefix, allcommand, beg, end):
        return [s for s in ("sing", "show") if s.startswith(prefix)]

    def do_exit(self, arg):
        return True


repl().cmdloop()