#!/usr/bin/env python3
# the entry point of the command interpreter

import cmd


class HBNBCommand(cmd.Cmd):
    """Entry point of the command interpreter for the AirBnB program.
    """
    prompt = "(hbnb)"

    def do_quit(self, arg):
        """Quit the program"""
        return True

    def do_EOF(self, arg):
        """Handles the End-Of-File condition """
        print()
        return True

    def emptyline(self):
        """overrided to do nothing"""
        pass

if __name__ == '__main__':
    HBNBCommand().cmdloop()
