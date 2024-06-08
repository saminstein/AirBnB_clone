#!/usr/bin/python3
"""
This module defines the command interface that controls the console
"""

import cmd as c
import os


class HBNBCommand(c.Cmd):
    """implements the commandline intepereter
    """
    prompt = "(hbnb) "

    def do_EOF(self, line):
        """exits the program when ctrl + d is
        entered
        """
        print('')
        return True

    def do_quit(self, line):
        """Quit command to exit the program
        """
        return True

    def emptyline(self):
        """Called when an empty line is entered.
        it shoud do nothing
        """
        pass


if __name__ == '__main__':
    HBNBCommand().cmdloop()
