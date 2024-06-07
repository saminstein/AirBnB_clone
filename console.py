#!/usr/bin/python3
"""
This module implements the cmd for the console
"""

import cmd as c
import os


class HBNBCommand(c.Cmd):
    """
    """
    prompt = "(hbnb) "


    def do_prompt(self, line):
        '''
        '''
        self.prompt = line

    def do_EOF(self, line):
        '''
        '''
        return True

    def do_quit(self, line):
        '''
        '''
        return True

if __name__ == '__main__':
    HBNBCommand().cmdloop()
